from __future__ import annotations

from datetime import date

from .governance import governance_score, risk_level


def recommend(item: dict, checks: list[dict], duplicate_similarity: float) -> dict:
    failed = {c["check_name"] for c in checks if c["status"] == "FAIL"}
    warnings = {c["check_name"] for c in checks if c["status"] == "WARN"}
    score = governance_score(checks, duplicate_similarity)
    risk = risk_level(score, checks, duplicate_similarity)

    reasons: list[str] = []
    actions: list[str] = []

    if "Ownership" in failed:
        reasons.append("No accountable content owner is assigned.")
        actions.append("Assign an accountable owner before approval or publication.")
    if "Source Authority" in failed:
        reasons.append("The source is not approved for governed enterprise use.")
        actions.append("Validate the source authority or retire the asset.")
    if "Review Date" in failed:
        reasons.append("The review date is overdue.")
        actions.append("Route to content owner review before continued use.")
    elif "Review Date" in warnings:
        actions.append("Schedule the upcoming content review.")
    if "Accessibility" in failed or "Accessibility" in warnings:
        reasons.append("Accessibility checks are incomplete.")
        actions.append("Resolve accessibility findings before approval or publication.")
    if duplicate_similarity >= 0.82:
        reasons.append("A highly similar governed asset already exists.")
        actions.append("Evaluate reuse, consolidation, or retirement instead of publishing a duplicate.")
    elif duplicate_similarity >= 0.68:
        actions.append("Review the duplicate candidate before creating another reusable asset.")

    current = item["lifecycle_state"]
    if current == "PUBLISHED" and ("Review Date" in failed or risk == "HIGH"):
        proposed = "REVIEW_REQUIRED"
    elif current in {"DRAFT", "TECHNICAL_REVIEW"} and risk == "LOW":
        proposed = "CONTENT_OWNER_REVIEW"
    elif current == "CONTENT_OWNER_REVIEW" and risk == "LOW":
        proposed = "APPROVED"
    elif current == "MONITORED" and risk == "LOW":
        proposed = "MONITORED"
    else:
        proposed = current

    if not reasons:
        reasons.append("No blocking governance issue was detected by the automated checks.")
    if not actions:
        actions.append("Maintain normal monitoring and review cadence.")

    return {
        "governance_score": score,
        "risk_level": risk,
        "proposed_state": proposed,
        "reasons": reasons,
        "recommended_actions": actions,
        "human_approval_required": proposed in {"APPROVED", "PUBLISHED", "RETIRED"},
        "generated_on": date.today().isoformat(),
        "agent_boundary": "Recommendation only. The agent cannot approve, publish, or retire content.",
    }
