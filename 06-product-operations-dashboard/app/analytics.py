from __future__ import annotations

from collections import Counter


def derive_portfolio_metrics(state: dict) -> dict:
    products = state["products"]
    slos = state["slo_services"]
    backlog = state["backlog"]
    debt = state["technical_debt"]
    risks = state["risks"]
    deps = state["dependencies"]

    health_counts = Counter(p["health"] for p in products)
    p1_open = sum(1 for x in backlog if x["priority"] == "P1" and x["status"] != "DONE")
    high_debt = sum(1 for x in debt if x["severity"] == "HIGH" and x["status"] != "CLOSED")
    high_risks = sum(1 for x in risks if x["severity"] == "HIGH")
    critical_bad_deps = sum(1 for x in deps if x["criticality"] == "CRITICAL" and x["health"] != "GREEN")
    at_risk_slos = sum(1 for x in slos if x["status"] != "MEETING")
    avg_error_budget = round(sum(x["error_budget_remaining"] for x in slos) / len(slos), 1)

    score = 100
    score -= health_counts.get("RED", 0) * 18
    score -= health_counts.get("AMBER", 0) * 6
    score -= at_risk_slos * 10
    score -= critical_bad_deps * 12
    score -= min(high_risks * 2, 12)
    score -= min(p1_open, 4) * 2
    score = max(0, score)

    return {
        "portfolio_health_score": score,
        "green_products": health_counts.get("GREEN", 0),
        "amber_products": health_counts.get("AMBER", 0),
        "red_products": health_counts.get("RED", 0),
        "p1_open": p1_open,
        "high_technical_debt": high_debt,
        "high_risks": high_risks,
        "critical_dependency_issues": critical_bad_deps,
        "at_risk_slos": at_risk_slos,
        "avg_error_budget_remaining": avg_error_budget,
    }


def executive_insights(state: dict) -> list[dict]:
    m = derive_portfolio_metrics(state)
    k = state["cross_product_kpis"]
    insights = []

    if k["learning_completion"] - k["operational_adoption"] >= 25:
        insights.append({"severity":"HIGH","title":"Completion is not translating to adoption","detail":f"Completion is {k['learning_completion']:.1f}% while operational adoption is {k['operational_adoption']:.1f}%. Investigate workflow, reinforcement, usability, and role support before adding more training."})
    if k["governed_content_ready"] < 60:
        insights.append({"severity":"HIGH","title":"Governance readiness is below threshold","detail":"Tighten publication/RAG eligibility and burn down the review backlog before expanding content reuse."})
    if k["ai_grounded_answer_rate"] < 80:
        insights.append({"severity":"HIGH","title":"AI grounded-answer quality degraded","detail":"Pause knowledge expansion, run regression evaluation, review source eligibility, and consider rollback."})
    if m["at_risk_slos"]:
        insights.append({"severity":"HIGH","title":"One or more service SLOs are at risk","detail":"Protect the error budget and prioritize reliability work ahead of discretionary feature delivery."})
    if m["critical_dependency_issues"]:
        insights.append({"severity":"HIGH","title":"Critical dependency is unhealthy","detail":"Release decisions should account for dependency health; escalate ownership rather than masking the issue locally."})
    if m["p1_open"] >= 3:
        insights.append({"severity":"MEDIUM","title":"P1 backlog concentration is elevated","detail":"Review sequencing, ownership, and whether roadmap commitments exceed current technical capacity."})
    if not insights:
        insights.append({"severity":"LOW","title":"Portfolio is within current operating thresholds","detail":"Continue monitoring adoption, governance readiness, SLOs, dependencies, and technical debt."})
    return insights
