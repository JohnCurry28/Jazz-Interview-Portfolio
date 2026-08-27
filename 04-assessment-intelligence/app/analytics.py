from __future__ import annotations

from collections import defaultdict
from math import sqrt
from statistics import mean, variance


def pearson(xs: list[float], ys: list[float]) -> float | None:
    if len(xs) != len(ys) or len(xs) < 3:
        return None
    mx, my = mean(xs), mean(ys)
    dx = [x - mx for x in xs]
    dy = [y - my for y in ys]
    denom = sqrt(sum(x * x for x in dx) * sum(y * y for y in dy))
    if denom == 0:
        return None
    return sum(x * y for x, y in zip(dx, dy)) / denom


def kr20(matrix: list[list[int]]) -> float | None:
    if not matrix or len(matrix) < 3 or len(matrix[0]) < 2:
        return None
    k = len(matrix[0])
    totals = [sum(row) for row in matrix]
    try:
        total_variance = variance(totals)
    except Exception:
        return None
    if total_variance <= 0:
        return None
    pq_sum = 0.0
    for j in range(k):
        p = mean(row[j] for row in matrix)
        pq_sum += p * (1 - p)
    value = (k / (k - 1)) * (1 - (pq_sum / total_variance))
    return max(-1.0, min(1.0, value))


def item_status(p: float, disc: float | None, item_rest: float | None) -> tuple[str, str]:
    disc_v = disc if disc is not None else 0.0
    rest_v = item_rest if item_rest is not None else 0.0
    if disc_v < 0 or rest_v < 0:
        return "REVIEW", "Negative discrimination signal; inspect keying, ambiguity, alignment, or scoring before reuse."
    if p < 0.45:
        return "DIFFICULT", "Low success rate; confirm prerequisite learning, wording, and content alignment before changing difficulty."
    if p > 0.90 and disc_v < 0.15:
        return "MONITOR", "Very easy item with limited separation; retain only if it verifies essential baseline knowledge."
    if 0.30 <= p <= 0.90 and disc_v >= 0.20 and rest_v >= 0.20:
        return "GOOD", "Item is functioning as useful evidence of capability in this cohort."
    return "MONITOR", "Mixed statistical evidence; review with the content owner and collect more administrations before revising."


def analyze(items: list[dict], learners: list[dict], responses: list[dict]) -> dict:
    learner_ids = [x["learner_id"] for x in learners]
    item_ids = [x["item_id"] for x in items]
    item_lookup = {x["item_id"]: x for x in items}
    response_map = {(r["learner_id"], r["item_id"]): int(r["correct"]) for r in responses}

    matrix = [[response_map[(lid, iid)] for iid in item_ids] for lid in learner_ids]
    totals = {lid: sum(response_map[(lid, iid)] for iid in item_ids) for lid in learner_ids}
    k = len(item_ids)

    ranked = sorted(learner_ids, key=lambda lid: totals[lid], reverse=True)
    group_n = max(1, round(len(ranked) * 0.27))
    upper = set(ranked[:group_n])
    lower = set(ranked[-group_n:])

    item_results = []
    for iid in item_ids:
        vals = [response_map[(lid, iid)] for lid in learner_ids]
        p = mean(vals)
        upper_p = mean(response_map[(lid, iid)] for lid in upper)
        lower_p = mean(response_map[(lid, iid)] for lid in lower)
        disc = upper_p - lower_p
        rest = [totals[lid] - response_map[(lid, iid)] for lid in learner_ids]
        item_rest = pearson([float(v) for v in vals], [float(v) for v in rest])
        status, recommendation = item_status(p, disc, item_rest)
        item_results.append({
            **item_lookup[iid],
            "n": len(vals),
            "difficulty": round(p, 4),
            "upper_27": round(upper_p, 4),
            "lower_27": round(lower_p, 4),
            "discrimination": round(disc, 4),
            "item_rest_correlation": round(item_rest, 4) if item_rest is not None else None,
            "status": status,
            "recommendation": recommendation,
        })

    capability_items: dict[str, list[str]] = defaultdict(list)
    for item in items:
        capability_items[item["capability"]].append(item["item_id"])

    capability_results = []
    learner_capability_scores: dict[str, dict[str, float]] = defaultdict(dict)
    for cap, ids in capability_items.items():
        per_learner = []
        for lid in learner_ids:
            score = mean(response_map[(lid, iid)] for iid in ids)
            learner_capability_scores[lid][cap] = score
            per_learner.append(score)
        avg_score = mean(per_learner)
        mastery_rate = mean(1.0 if s >= (2/3) else 0.0 for s in per_learner)
        adoption_vals = [float(x["adoption_score"]) for x in learners if x["primary_capability"] == cap]
        business_vals = [float(x["business_outcome_score"]) for x in learners if x["primary_capability"] == cap]
        capability_results.append({
            "capability": cap,
            "items": len(ids),
            "average_assessment_score": round(avg_score, 4),
            "mastery_rate": round(mastery_rate, 4),
            "adoption_score": round(mean(adoption_vals), 4) if adoption_vals else None,
            "business_outcome_score": round(mean(business_vals), 4) if business_vals else None,
        })

    learner_rows = []
    for learner in learners:
        lid = learner["learner_id"]
        assessment_score = totals[lid] / k
        mastery = mean(1.0 if score >= (2/3) else 0.0 for score in learner_capability_scores[lid].values())
        learner_rows.append({**learner, "assessment_score": round(assessment_score, 4), "capability_mastery": round(mastery, 4)})

    completion = mean(float(x["completion_score"]) for x in learners)
    mastery = mean(x["capability_mastery"] for x in learner_rows)
    adoption = mean(float(x["adoption_score"]) for x in learners)
    business = mean(float(x["business_outcome_score"]) for x in learners)
    mastery_vals = [x["capability_mastery"] for x in learner_rows]
    adoption_vals = [float(x["adoption_score"]) for x in learners]
    business_vals = [float(x["business_outcome_score"]) for x in learners]

    flagged = [x for x in item_results if x["status"] in {"REVIEW", "DIFFICULT"}]
    largest_gap = max(capability_results, key=lambda c: c["mastery_rate"] - (c["adoption_score"] or 0.0))
    insights = [
        {"type": "OUTCOME_CHAIN", "headline": "Completion is not the endpoint", "detail": f"Completion is {completion:.0%}, while demonstrated mastery is {mastery:.0%} and operational adoption is {adoption:.0%}."},
        {"type": "CAPABILITY_GAP", "headline": f"Largest mastery-to-adoption gap: {largest_gap['capability']}", "detail": f"Mastery is {largest_gap['mastery_rate']:.0%}; adoption is {(largest_gap['adoption_score'] or 0):.0%}. Investigate workflow friction, manager reinforcement, incentives, or tooling before prescribing more training."},
        {"type": "ITEM_QUALITY", "headline": f"{len(flagged)} items need targeted review", "detail": "Psychometric flags are evidence for expert review, not automatic proof that an item is invalid."},
        {"type": "BUSINESS_LINK", "headline": "Link learning signals to operational outcomes", "detail": f"Mastery/adoption correlation is {pearson(mastery_vals, adoption_vals) or 0:.2f}; adoption/business-outcome correlation is {pearson(adoption_vals, business_vals) or 0:.2f} in this synthetic cohort."},
    ]

    reliability = kr20(matrix)
    mastery_adoption = pearson(mastery_vals, adoption_vals)
    adoption_business = pearson(adoption_vals, business_vals)
    return {
        "overview": {
            "learners": len(learners),
            "items": len(items),
            "completion_rate": round(completion, 4),
            "assessment_mean": round(mean(totals.values()) / k, 4),
            "capability_mastery": round(mastery, 4),
            "adoption_rate": round(adoption, 4),
            "business_outcome_index": round(business, 4),
            "kr20_reliability": round(reliability, 4) if reliability is not None else None,
            "mastery_adoption_correlation": round(mastery_adoption, 4) if mastery_adoption is not None else None,
            "adoption_business_correlation": round(adoption_business, 4) if adoption_business is not None else None,
        },
        "items": item_results,
        "capabilities": sorted(capability_results, key=lambda x: x["capability"]),
        "learners": learner_rows,
        "insights": insights,
    }
