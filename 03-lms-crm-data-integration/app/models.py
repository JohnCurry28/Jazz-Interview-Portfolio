from __future__ import annotations

from datetime import datetime, timezone
from typing import Any, Literal

from pydantic import BaseModel, Field

SystemName = Literal["HRIS", "LMS", "CAPABILITY", "CRM", "DATA_PLATFORM"]
EventType = Literal[
    "employee.provisioned",
    "employee.role_changed",
    "learning.assigned",
    "learning.completed",
    "capability.updated",
    "crm.adoption_recorded",
    "analytics.refreshed",
]


class EventEnvelope(BaseModel):
    event_id: str
    event_type: EventType
    schema_version: str = "1.0"
    occurred_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    source_system: SystemName
    subject_id: str
    correlation_id: str
    idempotency_key: str
    payload: dict[str, Any]


class PublishRequest(BaseModel):
    event: EventEnvelope
    failure_mode: Literal["none", "transient", "permanent"] = "none"


class PublishResponse(BaseModel):
    accepted: bool
    duplicate: bool = False
    status: Literal["PROCESSED", "DUPLICATE", "DEAD_LETTERED", "REJECTED"]
    event_id: str
    correlation_id: str
    deliveries: list[dict[str, Any]] = []
    message: str


class ScenarioResponse(BaseModel):
    scenario: str
    correlation_id: str
    events_created: int
    deliveries: int
    dlq_count: int
    notes: list[str]
