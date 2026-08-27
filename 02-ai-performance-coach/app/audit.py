from __future__ import annotations

import json
import sqlite3
import uuid
from datetime import datetime, timezone
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "data" / "coach_audit.db"


def init_db() -> None:
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS audit_events (
                id TEXT PRIMARY KEY,
                created_at TEXT NOT NULL,
                user_id TEXT NOT NULL,
                role TEXT NOT NULL,
                question TEXT NOT NULL,
                status TEXT NOT NULL,
                confidence REAL NOT NULL,
                grounded INTEGER NOT NULL,
                citation_ids TEXT NOT NULL,
                guardrail_reasons TEXT NOT NULL
            )
            """
        )


def record_event(*, user_id: str, role: str, question: str, status: str, confidence: float,
                 grounded: bool, citation_ids: list[str], guardrail_reasons: list[str]) -> str:
    init_db()
    event_id = str(uuid.uuid4())
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute(
            """
            INSERT INTO audit_events
            (id, created_at, user_id, role, question, status, confidence, grounded, citation_ids, guardrail_reasons)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                event_id,
                datetime.now(timezone.utc).isoformat(),
                user_id,
                role,
                question,
                status,
                confidence,
                1 if grounded else 0,
                json.dumps(citation_ids),
                json.dumps(guardrail_reasons),
            ),
        )
    return event_id


def recent_events(limit: int = 25) -> list[dict]:
    init_db()
    with sqlite3.connect(DB_PATH) as conn:
        conn.row_factory = sqlite3.Row
        rows = conn.execute(
            "SELECT * FROM audit_events ORDER BY created_at DESC LIMIT ?", (limit,)
        ).fetchall()
    return [dict(row) for row in rows]
