from __future__ import annotations

from datetime import datetime, timezone
from uuid import uuid4

from fastapi.testclient import TestClient

from app import db
from app.main import app

client = TestClient(app)


def setup_function():
    db.reset_db()


def event_payload(event_type="learning.completed", schema_version="1.0", idem=None):
    corr = str(uuid4())
    return {
        "event": {
            "event_id": str(uuid4()),
            "event_type": event_type,
            "schema_version": schema_version,
            "occurred_at": datetime.now(timezone.utc).isoformat(),
            "source_system": "LMS",
            "subject_id": "EMP-TEST",
            "correlation_id": corr,
            "idempotency_key": idem or f"{corr}:completion",
            "payload": {
                "employee_id": "EMP-TEST",
                "learning_asset_id": "CRM-101",
                "completed_at": datetime.now(timezone.utc).isoformat(),
                "score": 91,
            },
        },
        "failure_mode": "none",
    }


def test_health():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json()["status"] == "ok"


def test_happy_event_routes_to_two_destinations():
    r = client.post("/api/events", json=event_payload())
    assert r.status_code == 200
    body = r.json()
    assert body["status"] == "PROCESSED"
    assert len(body["deliveries"]) == 2
    assert {x["destination"] for x in body["deliveries"]} == {"CAPABILITY", "DATA_PLATFORM"}


def test_duplicate_idempotency_key_is_suppressed():
    payload = event_payload(idem="stable-key-1")
    first = client.post("/api/events", json=payload).json()
    second_payload = event_payload(idem="stable-key-1")
    second = client.post("/api/events", json=second_payload).json()
    assert first["status"] == "PROCESSED"
    assert second["status"] == "DUPLICATE"
    assert second["duplicate"] is True
    assert client.get("/api/metrics").json()["events"] == 1


def test_transient_failure_recovers_on_third_attempt():
    payload = event_payload()
    payload["failure_mode"] = "transient"
    body = client.post("/api/events", json=payload).json()
    assert body["status"] == "PROCESSED"
    attempts = [d for d in body["deliveries"] if d["destination"] == "CAPABILITY"]
    assert [d["status"] for d in attempts] == ["FAILED", "FAILED", "SUCCESS"]


def test_permanent_failure_moves_to_dead_letter_queue():
    payload = event_payload()
    payload["failure_mode"] = "permanent"
    body = client.post("/api/events", json=payload).json()
    assert body["status"] == "DEAD_LETTERED"
    dlq = client.get("/api/dead-letters").json()
    assert len(dlq) == 2


def test_unsupported_schema_is_rejected_before_delivery():
    body = client.post("/api/events", json=event_payload(schema_version="2.0")).json()
    assert body["status"] == "REJECTED"
    assert body["accepted"] is False
    assert client.get("/api/metrics").json()["events"] == 0


def test_missing_required_contract_field_is_rejected():
    payload = event_payload()
    del payload["event"]["payload"]["score"]
    body = client.post("/api/events", json=payload).json()
    assert body["status"] == "REJECTED"
    assert "score" in body["message"]


def test_system_of_record_boundaries_are_explicit():
    body = client.get("/api/system-of-record").json()
    assert body["employee_identity"] == "HRIS"
    assert body["learning_completion"] == "LMS"
    assert body["commercial_workflow_adoption"] == "CRM"


def test_happy_path_scenario_produces_lineage():
    result = client.post("/api/demo/scenarios/happy-path").json()
    assert result["events_created"] == 6
    trace = client.get(f"/api/lineage/{result['correlation_id']}")
    assert trace.status_code == 200
    assert len(trace.json()["events"]) == 6


def test_contract_catalog_exposes_version_and_destinations():
    contracts = client.get("/api/contracts").json()
    item = next(x for x in contracts if x["event_type"] == "learning.completed")
    assert item["schema_version"] == "1.0"
    assert "score" in item["required_payload_fields"]
    assert item["destinations"] == ["CAPABILITY", "DATA_PLATFORM"]


def test_unknown_lineage_returns_404():
    r = client.get("/api/lineage/does-not-exist")
    assert r.status_code == 404
