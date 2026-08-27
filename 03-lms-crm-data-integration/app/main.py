from __future__ import annotations

from contextlib import asynccontextmanager
from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from . import db
from .contracts import SYSTEM_OF_RECORD, contract_catalog
from .models import PublishRequest, PublishResponse, ScenarioResponse
from .processor import publish
from .scenarios import run_scenario

BASE_DIR = Path(__file__).resolve().parent


@asynccontextmanager
async def lifespan(app: FastAPI):
    db.init_db()
    yield


app = FastAPI(
    title="Enterprise Learning Integration Lab",
    version="0.1.0",
    description="Synthetic reference implementation for LMS, CRM, HRIS, capability, and enterprise-data integration patterns.",
    lifespan=lifespan,
)
app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")


@app.get("/", include_in_schema=False)
def home() -> FileResponse:
    return FileResponse(BASE_DIR / "static" / "index.html")


@app.get("/health")
def health() -> dict:
    return {"status": "ok", "service": "enterprise-learning-integration-lab", "version": "0.1.0"}


@app.post("/api/events", response_model=PublishResponse)
def api_publish(request: PublishRequest) -> PublishResponse:
    return publish(request)


@app.get("/api/events")
def api_events(limit: int = 50) -> list[dict]:
    return db.recent_events(limit)


@app.get("/api/deliveries")
def api_deliveries(limit: int = 100) -> list[dict]:
    return db.recent_deliveries(limit)


@app.get("/api/dead-letters")
def api_dead_letters(limit: int = 100) -> list[dict]:
    return db.dead_letters(limit)


@app.get("/api/lineage/{correlation_id}")
def api_lineage(correlation_id: str) -> dict:
    data = db.lineage(correlation_id)
    if not data["events"] and not data["deliveries"] and not data["dead_letters"]:
        raise HTTPException(status_code=404, detail="Correlation ID not found")
    return data


@app.get("/api/contracts")
def api_contracts() -> list[dict]:
    return contract_catalog()


@app.get("/api/system-of-record")
def api_system_of_record() -> dict:
    return SYSTEM_OF_RECORD


@app.get("/api/metrics")
def api_metrics() -> dict:
    return db.metrics()


@app.post("/api/demo/reset")
def api_reset() -> dict:
    db.reset_db()
    return {"status": "reset"}


@app.post("/api/demo/scenarios/{scenario}", response_model=ScenarioResponse)
def api_scenario(scenario: str) -> ScenarioResponse:
    try:
        return run_scenario(scenario)
    except ValueError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc
