from __future__ import annotations

from datetime import datetime, timezone
from uuid import uuid4

from . import db
from .models import EventEnvelope, PublishRequest, ScenarioResponse
from .processor import publish


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _event(event_type: str, source: str, subject_id: str, correlation_id: str, payload: dict, suffix: str) -> EventEnvelope:
    return EventEnvelope(
        event_id=str(uuid4()),
        event_type=event_type,
        schema_version="1.0",
        source_system=source,
        subject_id=subject_id,
        correlation_id=correlation_id,
        idempotency_key=f"{correlation_id}:{suffix}",
        payload=payload,
    )


def run_scenario(name: str) -> ScenarioResponse:
    correlation_id = str(uuid4())
    employee_id = "EMP-1042"
    notes: list[str] = []
    requests: list[PublishRequest] = []

    if name == "happy-path":
        requests = [
            PublishRequest(event=_event("employee.provisioned", "HRIS", employee_id, correlation_id, {
                "employee_id": employee_id, "email": "alex.rivera@example.test", "role_code": "COMMERCIAL_FIELD", "region": "US-EAST"
            }, "provision")),
            PublishRequest(event=_event("learning.assigned", "LMS", employee_id, correlation_id, {
                "employee_id": employee_id, "learning_asset_id": "CRM-ONBOARD-101", "due_date": "2026-09-15"
            }, "assignment")),
            PublishRequest(event=_event("learning.completed", "LMS", employee_id, correlation_id, {
                "employee_id": employee_id, "learning_asset_id": "CRM-ONBOARD-101", "completed_at": _now(), "score": 92
            }, "completion")),
            PublishRequest(event=_event("capability.updated", "CAPABILITY", employee_id, correlation_id, {
                "employee_id": employee_id, "capability_code": "CRM-WORKFLOW", "mastery_level": 3, "evidence_source": "learning.completed"
            }, "capability")),
            PublishRequest(event=_event("crm.adoption_recorded", "CRM", employee_id, correlation_id, {
                "employee_id": employee_id, "workflow_code": "OMNI-PLAN", "adoption_signal": "USED_IN_LAST_7_DAYS", "observed_at": _now()
            }, "adoption")),
            PublishRequest(event=_event("analytics.refreshed", "DATA_PLATFORM", employee_id, correlation_id, {
                "dataset": "learning_capability_adoption", "refreshed_at": _now(), "record_count": 1
            }, "analytics")),
        ]
        notes.append("Demonstrates a complete cross-system journey from HRIS provisioning through learning, capability, CRM adoption, and analytics refresh.")
    elif name == "retry-success":
        requests = [PublishRequest(event=_event("learning.completed", "LMS", employee_id, correlation_id, {
            "employee_id": employee_id, "learning_asset_id": "DATA-101", "completed_at": _now(), "score": 88
        }, "retry"), failure_mode="transient")]
        notes.append("Each destination fails twice and succeeds on the third attempt, demonstrating bounded retry behavior.")
    elif name == "dead-letter":
        requests = [PublishRequest(event=_event("capability.updated", "CAPABILITY", employee_id, correlation_id, {
            "employee_id": employee_id, "capability_code": "OMNI-PLANNING", "mastery_level": 2, "evidence_source": "manager_observation"
        }, "dlq"), failure_mode="permanent")]
        notes.append("Permanent synthetic delivery failures are retried three times, then moved to the dead-letter queue for operator review.")
    elif name == "duplicate":
        event = _event("learning.completed", "LMS", employee_id, correlation_id, {
            "employee_id": employee_id, "learning_asset_id": "CRM-201", "completed_at": _now(), "score": 95
        }, "duplicate")
        requests = [PublishRequest(event=event), PublishRequest(event=event)]
        notes.append("The second publish reuses the same idempotency key and is suppressed before downstream delivery.")
    else:
        raise ValueError(f"Unknown scenario: {name}")

    delivery_count_before = len(db.recent_deliveries(10000))
    dlq_before = len(db.dead_letters(10000))
    for request in requests:
        publish(request)
    delivery_count_after = len(db.recent_deliveries(10000))
    dlq_after = len(db.dead_letters(10000))
    lineage = db.lineage(correlation_id)
    return ScenarioResponse(
        scenario=name,
        correlation_id=correlation_id,
        events_created=len(lineage["events"]),
        deliveries=delivery_count_after - delivery_count_before,
        dlq_count=dlq_after - dlq_before,
        notes=notes,
    )
