from __future__ import annotations

import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parents[1] / "data" / "capability_hub.db"


def connect() -> sqlite3.Connection:
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db() -> None:
    with connect() as conn:
        conn.executescript(
            """
            CREATE TABLE IF NOT EXISTS roles (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL UNIQUE,
                description TEXT NOT NULL
            );

            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                role_id INTEGER NOT NULL,
                region TEXT NOT NULL,
                manager TEXT NOT NULL,
                onboarding_pct INTEGER NOT NULL,
                adoption_pct INTEGER NOT NULL,
                FOREIGN KEY(role_id) REFERENCES roles(id)
            );

            CREATE TABLE IF NOT EXISTS capabilities (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                category TEXT NOT NULL,
                description TEXT NOT NULL
            );

            CREATE TABLE IF NOT EXISTS role_capabilities (
                role_id INTEGER NOT NULL,
                capability_id INTEGER NOT NULL,
                target_level INTEGER NOT NULL,
                PRIMARY KEY(role_id, capability_id),
                FOREIGN KEY(role_id) REFERENCES roles(id),
                FOREIGN KEY(capability_id) REFERENCES capabilities(id)
            );

            CREATE TABLE IF NOT EXISTS user_capabilities (
                user_id INTEGER NOT NULL,
                capability_id INTEGER NOT NULL,
                mastery_pct INTEGER NOT NULL,
                evidence_count INTEGER NOT NULL,
                PRIMARY KEY(user_id, capability_id),
                FOREIGN KEY(user_id) REFERENCES users(id),
                FOREIGN KEY(capability_id) REFERENCES capabilities(id)
            );

            CREATE TABLE IF NOT EXISTS learning_assets (
                id INTEGER PRIMARY KEY,
                title TEXT NOT NULL,
                asset_type TEXT NOT NULL,
                capability_id INTEGER NOT NULL,
                version TEXT NOT NULL,
                status TEXT NOT NULL,
                owner TEXT NOT NULL,
                last_reviewed TEXT NOT NULL,
                reusable INTEGER NOT NULL DEFAULT 1,
                FOREIGN KEY(capability_id) REFERENCES capabilities(id)
            );

            CREATE TABLE IF NOT EXISTS learning_assignments (
                user_id INTEGER NOT NULL,
                asset_id INTEGER NOT NULL,
                status TEXT NOT NULL,
                score INTEGER,
                due_date TEXT,
                PRIMARY KEY(user_id, asset_id),
                FOREIGN KEY(user_id) REFERENCES users(id),
                FOREIGN KEY(asset_id) REFERENCES learning_assets(id)
            );

            CREATE TABLE IF NOT EXISTS integration_events (
                id INTEGER PRIMARY KEY,
                event_type TEXT NOT NULL,
                source TEXT NOT NULL,
                destination TEXT NOT NULL,
                status TEXT NOT NULL,
                occurred_at TEXT NOT NULL,
                correlation_id TEXT NOT NULL
            );
            """
        )

        if conn.execute("SELECT COUNT(*) FROM roles").fetchone()[0] == 0:
            seed(conn)


def seed(conn: sqlite3.Connection) -> None:
    roles = [
        (1, "Sales Representative", "Field commercial role focused on compliant customer engagement and execution."),
        (2, "Marketing Manager", "Brand and campaign role coordinating strategy, content, channels, and measurement."),
        (3, "CX / Omnichannel Specialist", "Customer-experience role orchestrating channels, journeys, data, and activation."),
        (4, "People Manager", "Leader responsible for team readiness, coaching, adoption, and capability growth."),
    ]
    conn.executemany("INSERT INTO roles VALUES (?, ?, ?)", roles)

    capabilities = [
        (1, "Product & Disease-State Knowledge", "Commercial", "Apply approved product and disease-state knowledge appropriately."),
        (2, "CRM Execution", "Digital", "Use CRM workflows consistently and capture high-quality interaction data."),
        (3, "Omnichannel Engagement", "Digital", "Select and orchestrate appropriate channels based on customer needs."),
        (4, "Data Literacy", "Data", "Interpret dashboards, metrics, and evidence to improve decisions."),
        (5, "AI-Enabled Ways of Working", "AI", "Use approved AI tools responsibly to improve productivity and decision quality."),
        (6, "Compliance & Governance", "Governance", "Apply policy, approval, privacy, and content-governance requirements."),
        (7, "Coaching & Capability Leadership", "Leadership", "Diagnose capability gaps and coach teams toward measurable adoption."),
    ]
    conn.executemany("INSERT INTO capabilities VALUES (?, ?, ?, ?)", capabilities)

    role_caps = [
        (1,1,4),(1,2,4),(1,3,3),(1,4,3),(1,5,2),(1,6,4),
        (2,1,3),(2,2,3),(2,3,4),(2,4,4),(2,5,3),(2,6,4),
        (3,2,4),(3,3,5),(3,4,4),(3,5,4),(3,6,4),
        (4,2,3),(4,3,3),(4,4,4),(4,5,3),(4,6,4),(4,7,5),
    ]
    conn.executemany("INSERT INTO role_capabilities VALUES (?, ?, ?)", role_caps)

    users = [
        (1,"Alex Morgan",1,"US East","Dana Brooks",82,68),
        (2,"Priya Shah",2,"US Central","Dana Brooks",94,81),
        (3,"Mateo Ruiz",3,"US West","Elena Park",76,74),
        (4,"Jordan Lee",4,"US East","Elena Park",100,88),
        (5,"Taylor Kim",1,"US Central","Jordan Lee",61,53),
        (6,"Morgan Reed",1,"US West","Jordan Lee",89,72),
    ]
    conn.executemany("INSERT INTO users VALUES (?, ?, ?, ?, ?, ?, ?)", users)

    user_caps = [
        (1,1,84,3),(1,2,72,4),(1,3,63,2),(1,4,70,2),(1,5,48,1),(1,6,90,4),
        (2,1,78,2),(2,2,82,4),(2,3,88,5),(2,4,91,4),(2,5,73,2),(2,6,94,4),
        (3,2,85,4),(3,3,93,5),(3,4,79,3),(3,5,82,3),(3,6,89,4),
        (4,2,87,4),(4,3,83,4),(4,4,92,5),(4,5,78,3),(4,6,96,5),(4,7,90,6),
        (5,1,67,2),(5,2,55,2),(5,3,49,1),(5,4,61,2),(5,5,35,1),(5,6,80,3),
        (6,1,91,4),(6,2,77,3),(6,3,71,3),(6,4,74,2),(6,5,59,2),(6,6,92,4),
    ]
    conn.executemany("INSERT INTO user_capabilities VALUES (?, ?, ?, ?)", user_caps)

    assets = [
        (1,"Product & Disease-State Foundations","Course",1,"3.2","Approved","Commercial Learning", "2026-07-10",1),
        (2,"CRM Workflow Essentials","Simulation",2,"2.4","Approved","Digital Enablement", "2026-08-02",1),
        (3,"Omnichannel Journey Design","Workshop",3,"1.8","Approved","CX Excellence", "2026-07-29",1),
        (4,"Data Literacy for Commercial Teams","Microlearning",4,"4.1","Approved","Analytics COE", "2026-08-12",1),
        (5,"Responsible Enterprise AI","Course",5,"2.0","Approved","AI Enablement", "2026-08-15",1),
        (6,"Content, Privacy & Approval Governance","Course",6,"5.3","Approved","Compliance Learning", "2026-08-04",1),
        (7,"Manager Coaching Lab","Simulation",7,"1.5","In Review","Leadership Development", "2026-08-20",1),
        (8,"Legacy CRM Quick Guide","Job Aid",2,"7.9","Retire", "Platform Operations", "2025-12-15",0),
    ]
    conn.executemany("INSERT INTO learning_assets VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", assets)

    assignments = [
        (1,1,"Completed",88,"2026-08-15"),(1,2,"Completed",79,"2026-08-18"),(1,3,"In Progress",None,"2026-09-05"),(1,4,"Completed",82,"2026-08-22"),(1,5,"Assigned",None,"2026-09-12"),(1,6,"Completed",95,"2026-08-20"),
        (2,1,"Completed",86,"2026-08-10"),(2,2,"Completed",91,"2026-08-12"),(2,3,"Completed",94,"2026-08-20"),(2,4,"Completed",96,"2026-08-22"),(2,5,"In Progress",None,"2026-09-01"),(2,6,"Completed",97,"2026-08-18"),
        (5,1,"Completed",72,"2026-08-20"),(5,2,"In Progress",None,"2026-08-30"),(5,3,"Assigned",None,"2026-09-10"),(5,4,"Assigned",None,"2026-09-15"),(5,5,"Assigned",None,"2026-09-20"),(5,6,"Completed",84,"2026-08-19"),
    ]
    conn.executemany("INSERT INTO learning_assignments VALUES (?, ?, ?, ?, ?)", assignments)

    events = [
        (1,"USER_PROVISIONED","HRIS","Learning Hub","Success","2026-08-26 08:01","c-1001"),
        (2,"LEARNING_ASSIGNED","Capability Engine","LMS","Success","2026-08-26 08:03","c-1002"),
        (3,"COURSE_COMPLETED","LMS","Learning Hub","Success","2026-08-26 09:17","c-1003"),
        (4,"CAPABILITY_UPDATED","Learning Hub","CRM Profile","Success","2026-08-26 09:18","c-1003"),
        (5,"ADOPTION_EVENT","CRM","Analytics Platform","Success","2026-08-26 10:22","c-1004"),
        (6,"CONTENT_PUBLISHED","Content Repository","LMS","Success","2026-08-26 11:05","c-1005"),
        (7,"DATA_SYNC","Learning Hub","Enterprise Data","Warning","2026-08-26 11:44","c-1006"),
    ]
    conn.executemany("INSERT INTO integration_events VALUES (?, ?, ?, ?, ?, ?, ?)", events)
    conn.commit()
