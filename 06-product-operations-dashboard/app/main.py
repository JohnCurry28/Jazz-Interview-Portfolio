from __future__ import annotations

from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse

from .analytics import derive_portfolio_metrics, executive_insights
from .data import SCENARIOS, apply_scenario, base_state

BASE = Path(__file__).resolve().parent
app = FastAPI(title="Enterprise Learning Product Operations Control Plane", version="0.6.0")


def payload(state: dict) -> dict:
    return {**state, "portfolio_metrics": derive_portfolio_metrics(state), "executive_insights": executive_insights(state)}


@app.get("/")
def index():
    return FileResponse(BASE / "static" / "index.html")


@app.get("/health")
def health():
    return {"status":"ok","service":"product-operations-control-plane"}


@app.get("/api/portfolio")
def portfolio():
    return payload(base_state())


@app.get("/api/products")
def products():
    return base_state()["products"]


@app.get("/api/roadmap")
def roadmap():
    return base_state()["roadmap"]


@app.get("/api/backlog")
def backlog():
    return base_state()["backlog"]


@app.get("/api/technical-debt")
def technical_debt():
    return base_state()["technical_debt"]


@app.get("/api/dependencies")
def dependencies():
    return base_state()["dependencies"]


@app.get("/api/architecture-decisions")
def architecture_decisions():
    return base_state()["architecture_decisions"]


@app.get("/api/slos")
def slos():
    return base_state()["slo_services"]


@app.get("/api/risks")
def risks():
    return base_state()["risks"]


@app.get("/api/scenarios")
def scenarios():
    return [{"id":k,"description":v["description"]} for k,v in SCENARIOS.items()]


@app.post("/api/scenarios/{name}")
def scenario(name: str):
    if name not in SCENARIOS:
        raise HTTPException(status_code=404, detail="Unknown scenario")
    return payload(apply_scenario(name))
