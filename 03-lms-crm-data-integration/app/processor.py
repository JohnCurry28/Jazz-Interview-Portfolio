from __future__ import annotations

from typing import Any

from . import db
from .contracts import destinations_for, validate_event
from .models import PublishRequest, PublishResponse

MAX_ATTEMPTS = 3


def _delivery_should_fail(failure_mode: str, attempt: int) -> bool:
    if failure_mode == "none":
        return False
    if failure_mode == "transient":
        return attempt < MAX_ATTEMPTS
    return True


def publish(request: PublishRequest) -> PublishResponse:
    event = request.event
    errors = validate_event(event)
    if errors:
        return PublishResponse(
            accepted=False,
            status="REJECTED",
            event_id=event.event_id,
            correlation_id=event.correlation_id,
            deliveries=[],
            message="; ".join(errors),
        )

    existing = db.event_by_idempotency_key(event.idempotency_key)
    if existing:
        return PublishResponse(
            accepted=True,
            duplicate=True,
            status="DUPLICATE",
            event_id=existing["event_id"],
            correlation_id=existing["correlation_id"],
            deliveries=[],
            message="Duplicate idempotency key detected; event was not processed again.",
        )

    event_dict = event.model_dump(mode="json")
    db.insert_event(event_dict, "PROCESSING")

    deliveries: list[dict[str, Any]] = []
    dead_lettered = False
    for destination in destinations_for(event.event_type):
        delivered = False
        for attempt in range(1, MAX_ATTEMPTS + 1):
            if _delivery_should_fail(request.failure_mode, attempt):
                error = f"Synthetic {request.failure_mode} delivery failure"
                db.record_delivery(event.event_id, destination, attempt, "FAILED", event.correlation_id, error)
                deliveries.append({"destination": destination, "attempt": attempt, "status": "FAILED", "error": error})
                continue

            db.record_delivery(event.event_id, destination, attempt, "SUCCESS", event.correlation_id)
            deliveries.append({"destination": destination, "attempt": attempt, "status": "SUCCESS", "error": None})
            delivered = True
            break

        if not delivered:
            dead_lettered = True
            reason = f"Delivery failed after {MAX_ATTEMPTS} attempts"
            db.record_dead_letter(event.event_id, destination, event.correlation_id, reason, event.payload)

    final_status = "DEAD_LETTERED" if dead_lettered else "PROCESSED"
    db.update_event_status(event.event_id, final_status)
    return PublishResponse(
        accepted=True,
        duplicate=False,
        status=final_status,
        event_id=event.event_id,
        correlation_id=event.correlation_id,
        deliveries=deliveries,
        message=(
            "Event accepted but one or more destinations were moved to the dead-letter queue."
            if dead_lettered else
            "Event processed successfully across all configured destinations."
        ),
    )
