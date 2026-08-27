from __future__ import annotations

from contextlib import asynccontextmanager
from pathlib import Path
from typing import Any

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel, Field

from .db import connect, init_db

BASE_DIR = Path(__file__).resolve().parent


@asynccontextmanager
async def lifespan(_: FastAPI):
    init_db()
    yield


app = FastAPI(
    title="Global Learning Capability Hub",
    description="Synthetic enterprise learning capability reference implementation.",
    version="0.1.0",
    lifespan=lifespan,
)
app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")
templates = Jinja2Templates(directory=BASE_DIR / "templates")


class CompletionPayload(BaseModel):
    user_id: int
    asset_id: int
    score: int = Field(ge=0, le=100)


def rows(query: str, params: tuple[Any, ...] = ()) -> list[dict[str, Any]]:
    with connect() as conn:
        return [dict(r) for r in conn.execute(query, params).fetchall()]


def row(query: str, params: tuple[Any, ...] = ()) -> dict[str, Any] | None:
    result = rows(query, params)
    return result[0] if result else None


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/health")
def health():
    return {"status": "ok", "service": "global-learning-capability-hub"}


@app.get("/api/roles")
def get_roles():
    return rows("SELECT * FROM roles ORDER BY id")


@app.get("/api/users")
def get_users():
    return rows(
        """
        SELECT u.id, u.name, r.name AS role, u.region, u.manager,
               u.onboarding_pct, u.adoption_pct
        FROM users u JOIN roles r ON r.id = u.role_id
        ORDER BY u.id
        """
    )


@app.get("/api/users/{user_id}")
def get_user(user_id: int):
    user = row(
        """
        SELECT u.id, u.name, u.role_id, r.name AS role, r.description AS role_description,
               u.region, u.manager, u.onboarding_pct, u.adoption_pct
        FROM users u JOIN roles r ON r.id = u.role_id
        WHERE u.id = ?
        """,
        (user_id,),
    )
    if not user:
        raise HTTPException(404, "User not found")
    return user


@app.get("/api/users/{user_id}/capabilities")
def get_user_capabilities(user_id: int):
    if not row("SELECT id FROM users WHERE id = ?", (user_id,)):
        raise HTTPException(404, "User not found")
    return rows(
        """
        SELECT c.id, c.name, c.category, c.description, rc.target_level,
               COALESCE(uc.mastery_pct, 0) AS mastery_pct,
               COALESCE(uc.evidence_count, 0) AS evidence_count
        FROM users u
        JOIN role_capabilities rc ON rc.role_id = u.role_id
        JOIN capabilities c ON c.id = rc.capability_id
        LEFT JOIN user_capabilities uc ON uc.user_id = u.id AND uc.capability_id = c.id
        WHERE u.id = ?
        ORDER BY c.id
        """,
        (user_id,),
    )


@app.get("/api/users/{user_id}/learning-path")
def get_learning_path(user_id: int):
    if not row("SELECT id FROM users WHERE id = ?", (user_id,)):
        raise HTTPException(404, "User not found")
    return rows(
        """
        SELECT la.id, la.title, la.asset_type, c.name AS capability,
               la.version, la.status AS governance_status,
               COALESCE(a.status, 'Recommended') AS learning_status,
               a.score, a.due_date
        FROM users u
        JOIN role_capabilities rc ON rc.role_id = u.role_id
        JOIN capabilities c ON c.id = rc.capability_id
        JOIN learning_assets la ON la.capability_id = c.id AND la.status != 'Retire'
        LEFT JOIN learning_assignments a ON a.user_id = u.id AND a.asset_id = la.id
        WHERE u.id = ?
        ORDER BY CASE COALESCE(a.status, 'Recommended')
                   WHEN 'In Progress' THEN 1 WHEN 'Assigned' THEN 2
                   WHEN 'Recommended' THEN 3 WHEN 'Completed' THEN 4 ELSE 5 END,
                 la.id
        """,
        (user_id,),
    )


@app.get("/api/dashboard/overview")
def get_overview():
    metrics = row(
        """
        SELECT COUNT(*) AS active_users,
               ROUND(AVG(onboarding_pct), 1) AS onboarding_pct,
               ROUND(AVG(adoption_pct), 1) AS adoption_pct
        FROM users
        """
    ) or {}
    caps = row(
        """
        SELECT ROUND(AVG(mastery_pct), 1) AS mastery_pct,
               SUM(evidence_count) AS evidence_events
        FROM user_capabilities
        """
    ) or {}
    assets = row(
        """
        SELECT COUNT(*) AS active_assets,
               SUM(CASE WHEN reusable = 1 THEN 1 ELSE 0 END) AS reusable_assets,
               SUM(CASE WHEN status = 'In Review' THEN 1 ELSE 0 END) AS in_review,
               SUM(CASE WHEN status = 'Retire' THEN 1 ELSE 0 END) AS retire_candidates
        FROM learning_assets
        """
    ) or {}
    integrations = row(
        """
        SELECT COUNT(*) AS total_events,
               SUM(CASE WHEN status = 'Success' THEN 1 ELSE 0 END) AS successful_events
        FROM integration_events
        """
    ) or {}
    return {**metrics, **caps, **assets, **integrations}


@app.get("/api/dashboard/manager")
def get_manager_dashboard():
    return rows(
        """
        SELECT u.id, u.name, r.name AS role, u.region, u.onboarding_pct, u.adoption_pct,
               ROUND(AVG(uc.mastery_pct), 1) AS mastery_pct,
               CASE
                 WHEN u.adoption_pct < 60 THEN 'High'
                 WHEN u.adoption_pct < 75 THEN 'Medium'
                 ELSE 'Low'
               END AS intervention_risk
        FROM users u
        JOIN roles r ON r.id = u.role_id
        LEFT JOIN user_capabilities uc ON uc.user_id = u.id
        GROUP BY u.id
        ORDER BY u.adoption_pct ASC
        """
    )


@app.get("/api/governance/assets")
def get_governance_assets():
    return rows(
        """
        SELECT la.id, la.title, la.asset_type, c.name AS capability, la.version,
               la.status, la.owner, la.last_reviewed, la.reusable
        FROM learning_assets la
        JOIN capabilities c ON c.id = la.capability_id
        ORDER BY CASE la.status WHEN 'In Review' THEN 1 WHEN 'Retire' THEN 2 ELSE 3 END, la.id
        """
    )


@app.get("/api/integrations/events")
def get_integration_events():
    return rows("SELECT * FROM integration_events ORDER BY id DESC")


@app.post("/api/learning/completions")
def record_completion(payload: CompletionPayload):
    with connect() as conn:
        user = conn.execute("SELECT id FROM users WHERE id = ?", (payload.user_id,)).fetchone()
        asset = conn.execute("SELECT id, capability_id FROM learning_assets WHERE id = ?", (payload.asset_id,)).fetchone()
        if not user or not asset:
            raise HTTPException(404, "User or learning asset not found")

        conn.execute(
            """
            INSERT INTO learning_assignments(user_id, asset_id, status, score, due_date)
            VALUES (?, ?, 'Completed', ?, NULL)
            ON CONFLICT(user_id, asset_id) DO UPDATE SET status='Completed', score=excluded.score
            """,
            (payload.user_id, payload.asset_id, payload.score),
        )
        new_mastery = min(100, round(payload.score * 0.85 + 12))
        conn.execute(
            """
            INSERT INTO user_capabilities(user_id, capability_id, mastery_pct, evidence_count)
            VALUES (?, ?, ?, 1)
            ON CONFLICT(user_id, capability_id)
            DO UPDATE SET mastery_pct = ROUND((mastery_pct + excluded.mastery_pct) / 2.0),
                          evidence_count = evidence_count + 1
            """,
            (payload.user_id, asset["capability_id"], new_mastery),
        )
        conn.execute(
            """
            INSERT INTO integration_events(event_type, source, destination, status, occurred_at, correlation_id)
            VALUES ('COURSE_COMPLETED', 'Learning Hub', 'Enterprise Data', 'Success', datetime('now'), hex(randomblob(6)))
            """
        )
        conn.commit()
    return {"status": "recorded", "user_id": payload.user_id, "asset_id": payload.asset_id}
