from __future__ import annotations

import json
import sqlite3
from contextlib import contextmanager
from datetime import date, timedelta
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent.parent / "governance.db"


@contextmanager
def conn():
    c = sqlite3.connect(DB_PATH)
    c.row_factory = sqlite3.Row
    try:
        yield c
        c.commit()
    finally:
        c.close()


def init_db():
    with conn() as c:
        c.executescript(
            """
            CREATE TABLE IF NOT EXISTS content_items (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                content_type TEXT NOT NULL,
                owner TEXT NOT NULL,
                source_authority TEXT NOT NULL,
                version TEXT NOT NULL,
                review_due_date TEXT NOT NULL,
                body TEXT NOT NULL,
                alt_text_complete INTEGER NOT NULL,
                captions_complete INTEGER NOT NULL,
                heading_order_valid INTEGER NOT NULL,
                descriptive_links INTEGER NOT NULL,
                approved_source INTEGER NOT NULL,
                lifecycle_state TEXT NOT NULL,
                created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
                updated_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
            );
            CREATE TABLE IF NOT EXISTS governance_checks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                item_id INTEGER NOT NULL,
                check_name TEXT NOT NULL,
                status TEXT NOT NULL,
                detail TEXT NOT NULL,
                score REAL NOT NULL,
                created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
            );
            CREATE TABLE IF NOT EXISTS duplicate_candidates (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                item_id INTEGER NOT NULL,
                candidate_item_id INTEGER NOT NULL,
                similarity REAL NOT NULL,
                created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
            );
            CREATE TABLE IF NOT EXISTS audit_log (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                item_id INTEGER,
                actor TEXT NOT NULL,
                event_type TEXT NOT NULL,
                detail TEXT NOT NULL,
                created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
            );
            CREATE TABLE IF NOT EXISTS versions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                item_id INTEGER NOT NULL,
                version TEXT NOT NULL,
                snapshot_json TEXT NOT NULL,
                created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
            );
            """
        )


def reset_db():
    if DB_PATH.exists():
        DB_PATH.unlink()
    init_db()
    seed_db()


def _insert_item(c, item: dict):
    cur = c.execute(
        """
        INSERT INTO content_items (
            title, content_type, owner, source_authority, version, review_due_date, body,
            alt_text_complete, captions_complete, heading_order_valid, descriptive_links,
            approved_source, lifecycle_state
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            item["title"], item["content_type"], item["owner"], item["source_authority"],
            item["version"], item["review_due_date"], item["body"],
            int(item["alt_text_complete"]), int(item["captions_complete"]),
            int(item["heading_order_valid"]), int(item["descriptive_links"]),
            int(item["approved_source"]), item["lifecycle_state"],
        ),
    )
    item_id = cur.lastrowid
    c.execute(
        "INSERT INTO versions (item_id, version, snapshot_json) VALUES (?, ?, ?)",
        (item_id, item["version"], json.dumps(item)),
    )
    return item_id


def seed_db():
    today = date.today()
    items = [
        {
            "title": "Commercial CRM Workflow Guide",
            "content_type": "Performance Support",
            "owner": "Commercial Capability Team",
            "source_authority": "CRM Product Owner",
            "version": "2.3",
            "review_due_date": (today + timedelta(days=120)).isoformat(),
            "body": "Approved workflow guidance for documenting account interactions, completing required fields, and escalating workflow exceptions through established manager channels.",
            "alt_text_complete": True,
            "captions_complete": True,
            "heading_order_valid": True,
            "descriptive_links": True,
            "approved_source": True,
            "lifecycle_state": "PUBLISHED",
        },
        {
            "title": "Omnichannel Campaign Readiness Checklist",
            "content_type": "Checklist",
            "owner": "Omnichannel Enablement",
            "source_authority": "Campaign Governance Council",
            "version": "1.8",
            "review_due_date": (today - timedelta(days=18)).isoformat(),
            "body": "Checklist for channel readiness, required approvals, audience validation, content readiness, launch dependencies, monitoring, and escalation contacts.",
            "alt_text_complete": True,
            "captions_complete": True,
            "heading_order_valid": True,
            "descriptive_links": True,
            "approved_source": True,
            "lifecycle_state": "MONITORED",
        },
        {
            "title": "Responsible AI Use for Commercial Teams",
            "content_type": "Microlearning",
            "owner": "AI Enablement Team",
            "source_authority": "Enterprise AI Governance",
            "version": "1.4",
            "review_due_date": (today + timedelta(days=75)).isoformat(),
            "body": "Employees should use only approved AI tools, avoid sensitive or confidential information in prompts, validate important outputs, and escalate uncertainty through approved governance channels.",
            "alt_text_complete": False,
            "captions_complete": False,
            "heading_order_valid": True,
            "descriptive_links": False,
            "approved_source": True,
            "lifecycle_state": "TECHNICAL_REVIEW",
        },
        {
            "title": "CRM Workflow Quick Reference",
            "content_type": "Performance Support",
            "owner": "Regional Enablement",
            "source_authority": "CRM Product Owner",
            "version": "1.1",
            "review_due_date": (today + timedelta(days=90)).isoformat(),
            "body": "Approved workflow guidance for documenting account interactions, completing required fields, and escalating workflow exceptions through established manager channels.",
            "alt_text_complete": True,
            "captions_complete": True,
            "heading_order_valid": True,
            "descriptive_links": True,
            "approved_source": True,
            "lifecycle_state": "DRAFT",
        },
        {
            "title": "Commercial Data Literacy Reporting Guide",
            "content_type": "Job Aid",
            "owner": "Commercial Analytics Enablement",
            "source_authority": "Enterprise Data Product Owner",
            "version": "1.2",
            "review_due_date": (today + timedelta(days=150)).isoformat(),
            "body": "Current guidance for interpreting approved commercial dashboards, validating metric definitions, distinguishing operational indicators from outcome measures, and escalating data-quality questions to the enterprise data product team.",
            "alt_text_complete": True,
            "captions_complete": True,
            "heading_order_valid": True,
            "descriptive_links": True,
            "approved_source": True,
            "lifecycle_state": "DRAFT",
        },
        {
            "title": "Legacy Field Enablement FAQ",
            "content_type": "FAQ",
            "owner": "",
            "source_authority": "Unknown",
            "version": "0.9",
            "review_due_date": (today - timedelta(days=240)).isoformat(),
            "body": "Legacy frequently asked questions assembled from historical field notes. Information has not been revalidated against current systems or operating guidance.",
            "alt_text_complete": True,
            "captions_complete": True,
            "heading_order_valid": False,
            "descriptive_links": False,
            "approved_source": False,
            "lifecycle_state": "REVIEW_REQUIRED",
        },
    ]
    with conn() as c:
        for item in items:
            _insert_item(c, item)
        c.execute(
            "INSERT INTO audit_log (actor, event_type, detail) VALUES (?, ?, ?)",
            ("system", "SEED", "Synthetic governance inventory initialized"),
        )
