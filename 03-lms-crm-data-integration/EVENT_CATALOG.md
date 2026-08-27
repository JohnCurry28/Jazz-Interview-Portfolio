# Event Catalog

All event examples are synthetic and use schema version `1.0`.

## `employee.provisioned`

**Owner/source:** HRIS  
**Destinations:** LMS, Data Platform  
**Required payload:** `employee_id`, `email`, `role_code`, `region`

Purpose: create or synchronize an eligible employee identity and initial role context.

## `employee.role_changed`

**Owner/source:** HRIS  
**Destinations:** LMS, Capability, Data Platform  
**Required payload:** `employee_id`, `previous_role`, `new_role`

Purpose: trigger reassignment/recalculation without allowing downstream systems to become the role authority.

## `learning.assigned`

**Owner/source:** LMS  
**Destination:** Data Platform  
**Required payload:** `employee_id`, `learning_asset_id`, `due_date`

Purpose: expose assignment activity for reporting and downstream readiness analysis.

## `learning.completed`

**Owner/source:** LMS  
**Destinations:** Capability, Data Platform  
**Required payload:** `employee_id`, `learning_asset_id`, `completed_at`, `score`

Purpose: contribute learning evidence to capability computation and analytics.

## `capability.updated`

**Owner/source:** Capability Service  
**Destinations:** CRM, Data Platform  
**Required payload:** `employee_id`, `capability_code`, `mastery_level`, `evidence_source`

Purpose: share a governed mastery state with operational and analytical consumers.

## `crm.adoption_recorded`

**Owner/source:** CRM  
**Destination:** Data Platform  
**Required payload:** `employee_id`, `workflow_code`, `adoption_signal`, `observed_at`

Purpose: show whether capability is appearing in the operational system where work occurs.

## `analytics.refreshed`

**Owner/source:** Data Platform  
**Destinations:** none in the MVP  
**Required payload:** `dataset`, `refreshed_at`, `record_count`

Purpose: close the demonstration loop by recording analytical refresh state.

## Envelope Contract

Every event uses:

```json
{
  "event_id": "uuid",
  "event_type": "learning.completed",
  "schema_version": "1.0",
  "occurred_at": "2026-08-26T20:00:00Z",
  "source_system": "LMS",
  "subject_id": "EMP-1042",
  "correlation_id": "uuid",
  "idempotency_key": "business-stable-key",
  "payload": {}
}
```

### Why both `event_id` and `idempotency_key`?

`event_id` identifies one produced message. `idempotency_key` identifies the underlying business operation for duplicate suppression. A producer can accidentally generate a second message with a different message ID for the same business action; the idempotency key is what protects consumers from reapplying it.
