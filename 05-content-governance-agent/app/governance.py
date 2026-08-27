from __future__ import annotations

import math
import re
from collections import Counter
from datetime import date

from .models import CheckStatus


def _tokens(text: str) -> Counter:
    words = re.findall(r"[a-z0-9]+", text.lower())
    stop = {"the", "a", "an", "and", "or", "for", "to", "of", "in", "on", "with", "through", "is", "are"}
    return Counter(w for w in words if w not in stop and len(w) > 2)


def cosine_similarity(a: str, b: str) -> float:
    va, vb = _tokens(a), _tokens(b)
    if not va or not vb:
        return 0.0
    dot = sum(va[k] * vb.get(k, 0) for k in va)
    na = math.sqrt(sum(v * v for v in va.values()))
    nb = math.sqrt(sum(v * v for v in vb.values()))
    return dot / (na * nb) if na and nb else 0.0


def evaluate_item(item: dict) -> list[dict]:
    checks: list[dict] = []

    def add(name: str, status: CheckStatus, detail: str, score: float):
        checks.append({"check_name": name, "status": status.value, "detail": detail, "score": score})

    owner = (item.get("owner") or "").strip()
    add(
        "Ownership",
        CheckStatus.PASS if owner else CheckStatus.FAIL,
        "Named accountable owner is present." if owner else "No accountable owner is assigned.",
        1.0 if owner else 0.0,
    )

    approved = bool(item.get("approved_source"))
    add(
        "Source Authority",
        CheckStatus.PASS if approved else CheckStatus.FAIL,
        "Source is marked approved and attributable." if approved else "Source is not approved for governed use.",
        1.0 if approved else 0.0,
    )

    due = date.fromisoformat(item["review_due_date"])
    delta = (due - date.today()).days
    if delta < 0:
        add("Review Date", CheckStatus.FAIL, f"Review is overdue by {abs(delta)} days.", 0.0)
    elif delta <= 30:
        add("Review Date", CheckStatus.WARN, f"Review is due in {delta} days.", 0.5)
    else:
        add("Review Date", CheckStatus.PASS, f"Review is current for {delta} more days.", 1.0)

    accessibility = [
        ("Alt Text", bool(item.get("alt_text_complete"))),
        ("Captions / Transcript", bool(item.get("captions_complete"))),
        ("Heading Order", bool(item.get("heading_order_valid"))),
        ("Descriptive Links", bool(item.get("descriptive_links"))),
    ]
    passed = sum(v for _, v in accessibility)
    status = CheckStatus.PASS if passed == 4 else (CheckStatus.WARN if passed >= 3 else CheckStatus.FAIL)
    missing = [name for name, ok in accessibility if not ok]
    add(
        "Accessibility",
        status,
        "Accessibility metadata checks passed." if not missing else "Missing or invalid: " + ", ".join(missing),
        passed / 4,
    )

    version_ok = bool(re.match(r"^\d+\.\d+$", item.get("version", "")))
    add(
        "Version Metadata",
        CheckStatus.PASS if version_ok else CheckStatus.FAIL,
        "Semantic content version is present." if version_ok else "Version must use major.minor format.",
        1.0 if version_ok else 0.0,
    )

    body_len = len((item.get("body") or "").strip())
    add(
        "Content Substance",
        CheckStatus.PASS if body_len >= 80 else CheckStatus.WARN,
        f"Body contains {body_len} characters.",
        1.0 if body_len >= 80 else 0.5,
    )

    return checks


def governance_score(checks: list[dict], duplicate_similarity: float = 0.0) -> float:
    base = sum(c["score"] for c in checks) / max(len(checks), 1)
    duplicate_penalty = 0.15 if duplicate_similarity >= 0.82 else (0.07 if duplicate_similarity >= 0.68 else 0.0)
    return max(0.0, round((base - duplicate_penalty) * 100, 1))


def risk_level(score: float, checks: list[dict], duplicate_similarity: float) -> str:
    hard_fail = any(c["status"] == "FAIL" and c["check_name"] in {"Ownership", "Source Authority"} for c in checks)
    if hard_fail or score < 60:
        return "HIGH"
    if score < 82 or duplicate_similarity >= 0.68 or any(c["status"] == "FAIL" for c in checks):
        return "MEDIUM"
    return "LOW"
