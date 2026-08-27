from __future__ import annotations

import json
import sqlite3
from pathlib import Path
from typing import Any

DB_PATH = Path(__file__).resolve().parents[1] / "integration_lab.db"

SCHEMA = """
CREATE TABLE IF NOT EXISTS events (
    event_id TEXT PRIMARY KEY,
    event_type TEXT NOT NULL,
    schema_version TEXT NOT NULL,
    occurred_at TEXT NOT NULL,
    source_system TEXT NOT NULL,
    subject_id TEXT NOT NULL,
    correlation_id TEXT NOT NULL,
    idempotency_key TEXT NOT NULL UNIQUE,
    payload_json TEXT NOT NULL,
    processing_status TEXT NOT NULL,
    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS deliveries (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    event_id TEXT NOT NULL,
    destination_system TEXT NOT NULL,
    attempt INTEGER NOT NULL,
    status TEXT NOT NULL,
    error_message TEXT,
    correlation_id TEXT NOT NULL,
    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS dead_letters (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    event_id TEXT NOT NULL,
    destination_system TEXT NOT NULL,
    correlation_id TEXT NOT NULL,
    reason TEXT NOT NULL,
    payload_json TEXT NOT NULL,
    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX IF NOT EXISTS idx_events_correlation ON events(correlation_id);
CREATE INDEX IF NOT EXISTS idx_deliveries_correlation ON deliveries(correlation_id);
CREATE INDEX IF NOT EXISTS idx_dlq_correlation ON dead_letters(correlation_id);
"""


def connect() -> sqlite3.Connection:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db() -> None:
    with connect() as conn:
        conn.executescript(SCHEMA)


def reset_db() -> None:
    if DB_PATH.exists():
        DB_PATH.unlink()
    init_db()


def event_by_idempotency_key(key: str) -> dict[str, Any] | None:
    with connect() as conn:
        row = conn.execute("SELECT * FROM events WHERE idempotency_key = ?", (key,)).fetchone()
    return dict(row) if row else None


def insert_event(event: dict[str, Any], status: str) -> None:
    with connect() as conn:
        conn.execute(
            """
            INSERT INTO events (
                event_id,event_type,schema_version,occurred_at,source_system,subject_id,
                correlation_id,idempotency_key,payload_json,processing_status
            ) VALUES (?,?,?,?,?,?,?,?,?,?)
            """,
            (
                event["event_id"], event["event_type"], event["schema_version"],
                event["occurred_at"], event["source_system"], event["subject_id"],
                event["correlation_id"], event["idempotency_key"],
                json.dumps(event["payload"], sort_keys=True), status,
            ),
        )


def update_event_status(event_id: str, status: str) -> None:
    with connect() as conn:
        conn.execute("UPDATE events SET processing_status = ? WHERE event_id = ?", (status, event_id))


def record_delivery(event_id: str, destination: str, attempt: int, status: str, correlation_id: str, error: str | None = None) -> None:
    with connect() as conn:
        conn.execute(
            "INSERT INTO deliveries(event_id,destination_system,attempt,status,error_message,correlation_id) VALUES (?,?,?,?,?,?)",
            (event_id, destination, attempt, status, error, correlation_id),
        )


def record_dead_letter(event_id: str, destination: str, correlation_id: str, reason: str, payload: dict[str, Any]) -> None:
    with connect() as conn:
        conn.execute(
            "INSERT INTO dead_letters(event_id,destination_system,correlation_id,reason,payload_json) VALUES (?,?,?,?,?)",
            (event_id, destination, correlation_id, reason, json.dumps(payload, sort_keys=True)),
        )


def recent_events(limit: int = 50) -> list[dict[str, Any]]:
    with connect() as conn:
        rows = conn.execute("SELECT * FROM events ORDER BY created_at DESC, rowid DESC LIMIT ?", (limit,)).fetchall()
    result = []
    for row in rows:
        item = dict(row)
        item["payload"] = json.loads(item.pop("payload_json"))
        result.append(item)
    return result


def recent_deliveries(limit: int = 100) -> list[dict[str, Any]]:
    with connect() as conn:
        rows = conn.execute("SELECT * FROM deliveries ORDER BY id DESC LIMIT ?", (limit,)).fetchall()
    return [dict(r) for r in rows]


def dead_letters(limit: int = 100) -> list[dict[str, Any]]:
    with connect() as conn:
        rows = conn.execute("SELECT * FROM dead_letters ORDER BY id DESC LIMIT ?", (limit,)).fetchall()
    result = []
    for row in rows:
        item = dict(row)
        item["payload"] = json.loads(item.pop("payload_json"))
        result.append(item)
    return result


def lineage(correlation_id: str) -> dict[str, list[dict[str, Any]]]:
    with connect() as conn:
        events = conn.execute("SELECT * FROM events WHERE correlation_id = ? ORDER BY created_at, rowid", (correlation_id,)).fetchall()
        deliveries = conn.execute("SELECT * FROM deliveries WHERE correlation_id = ? ORDER BY id", (correlation_id,)).fetchall()
        dlq = conn.execute("SELECT * FROM dead_letters WHERE correlation_id = ? ORDER BY id", (correlation_id,)).fetchall()
    return {
        "events": [dict(r) for r in events],
        "deliveries": [dict(r) for r in deliveries],
        "dead_letters": [dict(r) for r in dlq],
    }


def metrics() -> dict[str, Any]:
    with connect() as conn:
        event_count = conn.execute("SELECT COUNT(*) FROM events").fetchone()[0]
        delivery_count = conn.execute("SELECT COUNT(*) FROM deliveries").fetchone()[0]
        success_count = conn.execute("SELECT COUNT(*) FROM deliveries WHERE status='SUCCESS'").fetchone()[0]
        retry_count = conn.execute("SELECT COUNT(*) FROM deliveries WHERE attempt > 1").fetchone()[0]
        dlq_count = conn.execute("SELECT COUNT(*) FROM dead_letters").fetchone()[0]
        duplicate_safe = conn.execute("SELECT COUNT(DISTINCT idempotency_key) FROM events").fetchone()[0]
    success_rate = round((success_count / delivery_count * 100), 1) if delivery_count else 100.0
    return {
        "events": event_count,
        "deliveries": delivery_count,
        "successful_deliveries": success_count,
        "delivery_success_rate": success_rate,
        "retry_attempts": retry_count,
        "dead_letters": dlq_count,
        "unique_idempotency_keys": duplicate_safe,
    }
