# Architecture — Enterprise Learning Integration Lab

## Reference Architecture

```text
                    ┌──────────────────┐
                    │       HRIS       │
                    │ Identity + Role  │
                    └────────┬─────────┘
                             │ employee.provisioned / role_changed
                             ▼
                 ┌────────────────────────┐
                 │  Integration Contract  │
                 │ validation + routing   │
                 │ idempotency + tracing  │
                 └───────────┬────────────┘
                             │
                ┌────────────┼──────────────┐
                ▼            ▼              ▼
          ┌──────────┐ ┌────────────┐ ┌──────────────┐
          │   LMS    │ │ Capability │ │ Data Platform │
          │ Learning │ │  Mastery   │ │  Analytics    │
          └────┬─────┘ └─────┬──────┘ └──────────────┘
               │             │
     learning.completed      │ capability.updated
               │             ▼
               └──────► ┌──────────┐
                         │   CRM    │
                         │ Adoption │
                         └────┬─────┘
                              │ crm.adoption_recorded
                              ▼
                       ┌──────────────┐
                       │ Data Platform│
                       └──────────────┘
```

## Architectural Principles

1. **Systems have explicit ownership boundaries.** Integration does not redefine the source of truth.
2. **Events are governed contracts.** Each event type has a schema version, required fields, source, destination routing, correlation ID, and idempotency key.
3. **Idempotency is enforced before downstream delivery.** A repeated idempotency key returns `DUPLICATE` and produces no additional downstream attempts.
4. **Retries are bounded.** Transient failures retry up to three attempts; permanent failures exhaust the same policy and then enter a dead-letter queue.
5. **Every event is traceable.** A correlation ID binds related events, attempts, and dead letters into one lineage view.
6. **Failure is observable.** The application preserves attempt history and operator-visible dead-letter records.
7. **Version rejection happens before routing.** Unsupported event versions do not reach downstream systems.
8. **The demo keeps broker behavior deterministic.** Production architecture would normally use a managed event broker and durable consumers rather than synchronous in-process delivery.

## System of Record Matrix

| Domain | Authoritative System | Why |
|---|---|---|
| Employee identity | HRIS | Employment identity lifecycle originates here. |
| Employment role | HRIS | Role changes should not be inferred by learning systems. |
| Learning assignment | LMS | The LMS owns assigned learning state. |
| Learning completion | LMS | Completion evidence originates from the learning platform. |
| Capability mastery | Capability Service | Mastery aggregates evidence beyond completion. |
| Commercial workflow adoption | CRM | Operational adoption is observed where the work occurs. |
| Cross-system analytics | Data Platform | Enterprise reporting combines sources without replacing them. |

## Event Processing Sequence

```text
Producer
  │
  ├─ Create event envelope
  │    ├─ event_id
  │    ├─ event_type
  │    ├─ schema_version
  │    ├─ correlation_id
  │    ├─ idempotency_key
  │    └─ payload
  │
  ▼
Contract Validation
  │
  ├─ unsupported version → REJECTED
  ├─ missing required fields → REJECTED
  └─ valid
       │
       ▼
Idempotency Check
  │
  ├─ already processed → DUPLICATE
  └─ new
       │
       ▼
Route Lookup
       │
       ▼
Delivery Attempt
       │
       ├─ success → record SUCCESS
       │
       └─ failure → retry up to 3 attempts
                        │
                        ├─ eventually succeeds → PROCESSED
                        └─ exhausted → DEAD_LETTERED
```

## Production Evolution

The MVP would evolve toward:

- managed event broker such as Kafka, EventBridge, Pub/Sub, Service Bus, or equivalent
- durable consumer groups
- outbox/inbox pattern where transactional guarantees are needed
- schema registry
- signed service identities
- centralized secrets management
- OpenTelemetry traces and metrics
- distributed retry policy and DLQ tooling
- replay tooling with authorization and audit controls
- PII minimization and field-level data contracts
- regional/privacy-aware data routing
- managed relational/event storage
- contract tests between producer and consumer teams
- CI/CD gates for schema compatibility
