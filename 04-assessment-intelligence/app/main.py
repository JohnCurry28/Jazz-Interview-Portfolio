from __future__ import annotations

from collections import defaultdict
from contextlib import asynccontextmanager
from pathlib import Path

from fastapi import FastAPI, Query
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from .analytics import analyze
from .data import build_dataset

BASE = Path(__file__).resolve().parent


def build_state() -> dict:
    items, learners, responses = build_dataset()
    result = analyze(items, learners, responses)
    by_role: dict[str, list[dict]] = defaultdict(list)
    for learner in result["learners"]:
        by_role[learner["role"]].append(learner)
    cohorts = []
    for role, rows in sorted(by_role.items()):
        n = len(rows)
        cohorts.append({
            "role": role,
            "learners": n,
            "completion_rate": round(sum(x["completion_score"] for x in rows) / n, 4),
            "assessment_mean": round(sum(x["assessment_score"] for x in rows) / n, 4),
            "capability_mastery": round(sum(x["capability_mastery"] for x in rows) / n, 4),
            "adoption_rate": round(sum(x["adoption_score"] for x in rows) / n, 4),
            "business_outcome_index": round(sum(x["business_outcome_score"] for x in rows) / n, 4),
        })
    result["cohorts"] = cohorts
    return result


@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.analytics = build_state()
    yield


app = FastAPI(
    title="Enterprise Assessment Intelligence",
    version="1.0.0",
    description="Synthetic assessment-to-capability-to-adoption analytics reference implementation.",
    lifespan=lifespan,
)
app.mount("/static", StaticFiles(directory=BASE / "static"), name="static")


@app.get("/")
def index():
    return FileResponse(BASE / "static" / "index.html")


@app.get("/health")
def health():
    return {"status": "ok", "service": "assessment-intelligence", "version": "1.0.0"}


@app.get("/api/overview")
def overview():
    return app.state.analytics["overview"]


@app.get("/api/items")
def items(status: str | None = Query(default=None)):
    rows = app.state.analytics["items"]
    if status:
        rows = [x for x in rows if x["status"].lower() == status.lower()]
    return rows


@app.get("/api/capabilities")
def capabilities():
    return app.state.analytics["capabilities"]


@app.get("/api/cohorts")
def cohorts():
    return app.state.analytics["cohorts"]


@app.get("/api/learners")
def learners(risk_only: bool = False):
    rows = app.state.analytics["learners"]
    if risk_only:
        rows = [x for x in rows if x["completion_score"] >= 0.90 and (x["capability_mastery"] < 0.70 or x["adoption_score"] < 0.60)]
    return rows


@app.get("/api/insights")
def insights():
    return app.state.analytics["insights"]


@app.get("/api/metric-definitions")
def metric_definitions():
    return {
        "completion_rate": "Average LMS completion signal for required learning in the synthetic cohort.",
        "assessment_mean": "Mean proportion of assessment items answered correctly.",
        "capability_mastery": "Proportion of capability standards demonstrated through mapped assessment evidence.",
        "adoption_rate": "Synthetic CRM/workflow usage signal representing whether expected behavior is occurring in the flow of work.",
        "business_outcome_index": "Synthetic downstream operational quality index used only to demonstrate data linkage.",
        "difficulty": "Proportion of learners answering the item correctly; higher values indicate easier items.",
        "discrimination": "Upper 27% item success minus lower 27% item success.",
        "item_rest_correlation": "Correlation between item score and the learner's score on the remainder of the assessment.",
        "kr20_reliability": "Internal-consistency estimate for dichotomously scored assessment items.",
    }


@app.get("/api/data-lineage")
def data_lineage():
    return [
        {"signal": "Completion", "system_of_record": "LMS", "purpose": "Required learning completion and assignment state"},
        {"signal": "Assessment response", "system_of_record": "Assessment / LMS", "purpose": "Evidence used for item and mastery analytics"},
        {"signal": "Capability mastery", "system_of_record": "Capability analytics service", "purpose": "Derived evidence, not raw LMS completion"},
        {"signal": "Adoption", "system_of_record": "CRM / workflow platform", "purpose": "Observed operational behavior after enablement"},
        {"signal": "Business outcome", "system_of_record": "Enterprise data / BI", "purpose": "Downstream outcome signal used for aggregated analysis"},
    ]
