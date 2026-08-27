from __future__ import annotations

from typing import Any

from .models import EventEnvelope

SUPPORTED_SCHEMA_VERSIONS = {"1.0"}

REQUIRED_FIELDS: dict[str, set[str]] = {
    "employee.provisioned": {"employee_id", "email", "role_code", "region"},
    "employee.role_changed": {"employee_id", "previous_role", "new_role"},
    "learning.assigned": {"employee_id", "learning_asset_id", "due_date"},
    "learning.completed": {"employee_id", "learning_asset_id", "completed_at", "score"},
    "capability.updated": {"employee_id", "capability_code", "mastery_level", "evidence_source"},
    "crm.adoption_recorded": {"employee_id", "workflow_code", "adoption_signal", "observed_at"},
    "analytics.refreshed": {"dataset", "refreshed_at", "record_count"},
}

ROUTES: dict[str, list[str]] = {
    "employee.provisioned": ["LMS", "DATA_PLATFORM"],
    "employee.role_changed": ["LMS", "CAPABILITY", "DATA_PLATFORM"],
    "learning.assigned": ["DATA_PLATFORM"],
    "learning.completed": ["CAPABILITY", "DATA_PLATFORM"],
    "capability.updated": ["CRM", "DATA_PLATFORM"],
    "crm.adoption_recorded": ["DATA_PLATFORM"],
    "analytics.refreshed": [],
}

SYSTEM_OF_RECORD = {
    "employee_identity": "HRIS",
    "employment_role": "HRIS",
    "learning_assignment": "LMS",
    "learning_completion": "LMS",
    "capability_mastery": "CAPABILITY",
    "commercial_workflow_adoption": "CRM",
    "cross-system_analytics": "DATA_PLATFORM",
}


def validate_event(event: EventEnvelope) -> list[str]:
    errors: list[str] = []
    if event.schema_version not in SUPPORTED_SCHEMA_VERSIONS:
        errors.append(
            f"Unsupported schema_version {event.schema_version!r}; supported versions: {sorted(SUPPORTED_SCHEMA_VERSIONS)}"
        )
    required = REQUIRED_FIELDS[event.event_type]
    missing = sorted(field for field in required if field not in event.payload)
    if missing:
        errors.append(f"Missing required payload fields: {', '.join(missing)}")
    return errors


def destinations_for(event_type: str) -> list[str]:
    return list(ROUTES[event_type])


def contract_catalog() -> list[dict[str, Any]]:
    return [
        {
            "event_type": event_type,
            "schema_version": "1.0",
            "required_payload_fields": sorted(REQUIRED_FIELDS[event_type]),
            "destinations": ROUTES[event_type],
        }
        for event_type in REQUIRED_FIELDS
    ]
