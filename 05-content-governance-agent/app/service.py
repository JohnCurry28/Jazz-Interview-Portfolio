from __future__ import annotations

import json
from sqlite3 import Row

from . import db
from .agent import recommend
from .governance import cosine_similarity, evaluate_item


def row_dict(r: Row | None):
    return dict(r) if r is not None else None


def get_item(item_id: int):
    with db.conn() as c:
        return row_dict(c.execute("SELECT * FROM content_items WHERE id = ?", (item_id,)).fetchone())


def list_items():
    with db.conn() as c:
        return [dict(r) for r in c.execute("SELECT * FROM content_items ORDER BY id").fetchall()]


def _best_duplicate(item: dict):
    candidates = []
    for other in list_items():
        if other["id"] == item["id"]:
            continue
        sim = cosine_similarity(item["title"] + " " + item["body"], other["title"] + " " + other["body"])
        candidates.append((sim, other))
    candidates.sort(key=lambda x: x[0], reverse=True)
    return candidates[0] if candidates else (0.0, None)


def scan_item(item_id: int, actor: str = "governance-agent"):
    item = get_item(item_id)
    if not item:
        return None
    checks = evaluate_item(item)
    best_similarity, candidate = _best_duplicate(item)
    recommendation = recommend(item, checks, best_similarity)

    with db.conn() as c:
        c.execute("DELETE FROM governance_checks WHERE item_id = ?", (item_id,))
        c.execute("DELETE FROM duplicate_candidates WHERE item_id = ?", (item_id,))
        for check in checks:
            c.execute(
                "INSERT INTO governance_checks (item_id, check_name, status, detail, score) VALUES (?, ?, ?, ?, ?)",
                (item_id, check["check_name"], check["status"], check["detail"], check["score"]),
            )
        if candidate and best_similarity >= 0.50:
            c.execute(
                "INSERT INTO duplicate_candidates (item_id, candidate_item_id, similarity) VALUES (?, ?, ?)",
                (item_id, candidate["id"], best_similarity),
            )
        c.execute(
            "INSERT INTO audit_log (item_id, actor, event_type, detail) VALUES (?, ?, ?, ?)",
            (item_id, actor, "AGENT_SCAN", json.dumps(recommendation)),
        )

    return {
        "item": item,
        "checks": checks,
        "duplicate": None if not candidate else {
            "candidate_item_id": candidate["id"],
            "candidate_title": candidate["title"],
            "similarity": round(best_similarity, 3),
        },
        "recommendation": recommendation,
    }


def scan_all():
    return [scan_item(i["id"]) for i in list_items()]


def dashboard():
    scans = scan_all()
    items = [s["item"] for s in scans]
    review_queue = [
        s for s in scans
        if s["recommendation"]["risk_level"] in {"HIGH", "MEDIUM"}
        or s["item"]["lifecycle_state"] == "REVIEW_REQUIRED"
    ]
    duplicates = [s for s in scans if s["duplicate"] and s["duplicate"]["similarity"] >= 0.68]
    return {
        "summary": {
            "content_assets": len(items),
            "published": sum(i["lifecycle_state"] == "PUBLISHED" for i in items),
            "review_queue": len(review_queue),
            "high_risk": sum(s["recommendation"]["risk_level"] == "HIGH" for s in scans),
            "duplicate_flags": len(duplicates),
            "average_governance_score": round(sum(s["recommendation"]["governance_score"] for s in scans) / len(scans), 1),
        },
        "items": scans,
        "review_queue": review_queue,
        "duplicates": duplicates,
    }


def review_action(item_id: int, reviewer: str, action: str, note: str):
    item = get_item(item_id)
    if not item:
        return None
    scan = scan_item(item_id)
    proposed = scan["recommendation"]["proposed_state"]
    risk = scan["recommendation"]["risk_level"]

    next_state = item["lifecycle_state"]
    allowed = True
    reason = ""

    if action == "APPROVE":
        if risk != "LOW":
            allowed = False
            reason = "Approval blocked because governance risk is not LOW."
        else:
            next_state = "APPROVED"
    elif action == "PUBLISH":
        if item["lifecycle_state"] != "APPROVED" or risk != "LOW":
            allowed = False
            reason = "Publication requires an APPROVED asset with LOW governance risk."
        else:
            next_state = "PUBLISHED"
    elif action == "REQUEST_CHANGES":
        next_state = "TECHNICAL_REVIEW"
    elif action == "REJECT":
        next_state = "REVIEW_REQUIRED"
    elif action == "RETIRE":
        next_state = "RETIRED"

    with db.conn() as c:
        c.execute(
            "INSERT INTO audit_log (item_id, actor, event_type, detail) VALUES (?, ?, ?, ?)",
            (item_id, reviewer, "HUMAN_DECISION", json.dumps({"action": action, "note": note, "allowed": allowed, "reason": reason, "agent_proposed": proposed})),
        )
        if allowed:
            c.execute(
                "UPDATE content_items SET lifecycle_state = ?, updated_at = CURRENT_TIMESTAMP WHERE id = ?",
                (next_state, item_id),
            )

    return {"allowed": allowed, "next_state": next_state, "reason": reason, "human_authority": True}


def audit_log(limit: int = 100):
    with db.conn() as c:
        return [dict(r) for r in c.execute("SELECT * FROM audit_log ORDER BY id DESC LIMIT ?", (limit,)).fetchall()]


def versions(item_id: int):
    with db.conn() as c:
        return [dict(r) for r in c.execute("SELECT * FROM versions WHERE item_id = ? ORDER BY id DESC", (item_id,)).fetchall()]
