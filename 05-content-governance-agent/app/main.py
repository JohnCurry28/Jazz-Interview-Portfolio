from __future__ import annotations

from contextlib import asynccontextmanager
from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse

from . import db, service
from .models import AgentScanRequest, ReviewDecision

STATIC = Path(__file__).resolve().parent / "static"


@asynccontextmanager
async def lifespan(app: FastAPI):
    db.init_db()
    if not service.list_items():
        db.seed_db()
    yield


app = FastAPI(
    title="Enterprise Content Governance Agent",
    version="1.0.0",
    description="Synthetic content-governance reference implementation with human approval boundaries.",
    lifespan=lifespan,
)


@app.get("/", response_class=HTMLResponse)
def home():
    return (STATIC / "index.html").read_text(encoding="utf-8")


@app.get("/health")
def health():
    return {"status": "ok", "service": "content-governance-agent", "version": "1.0.0"}


@app.get("/api/dashboard")
def dashboard():
    return service.dashboard()


@app.get("/api/items")
def items():
    return service.list_items()


@app.get("/api/items/{item_id}")
def item(item_id: int):
    data = service.get_item(item_id)
    if not data:
        raise HTTPException(404, "Content item not found")
    return data


@app.post("/api/agent/scan")
def scan(req: AgentScanRequest):
    data = service.scan_item(req.item_id, req.actor)
    if not data:
        raise HTTPException(404, "Content item not found")
    return data


@app.post("/api/agent/scan-all")
def scan_all():
    return service.scan_all()


@app.post("/api/items/{item_id}/review")
def review(item_id: int, decision: ReviewDecision):
    data = service.review_action(item_id, decision.reviewer, decision.action, decision.note)
    if not data:
        raise HTTPException(404, "Content item not found")
    return data


@app.get("/api/items/{item_id}/versions")
def item_versions(item_id: int):
    if not service.get_item(item_id):
        raise HTTPException(404, "Content item not found")
    return service.versions(item_id)


@app.get("/api/audit")
def audit(limit: int = 100):
    return service.audit_log(limit)


@app.post("/api/reset")
def reset():
    db.reset_db()
    return {"status": "reset", "items": len(service.list_items())}
