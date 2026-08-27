# LMS ↔ CRM ↔ Enterprise Data Integration Lab

A working, synthetic enterprise-integration reference implementation demonstrating how learning, employee, capability, CRM, and analytics systems can exchange governed events without blurring system-of-record boundaries.

> **Portfolio purpose:** This project demonstrates enterprise integration and data-architecture thinking relevant to technical leadership of a global learning-technology ecosystem.

> **Data boundary:** All employee IDs, roles, scores, workflows, events, timestamps, and system interactions are synthetic. This is an independent portfolio project and is not affiliated with, sponsored by, endorsed by, or an internal system of Jazz Pharmaceuticals or any other employer.

---

## 1. Executive Summary

Enterprise L&D platforms rarely operate in isolation. Identity arrives from HR systems. Learning assignments and completion live in an LMS or LXP. Capability signals may be computed elsewhere. Adoption can appear in CRM or workflow tools. Enterprise analytics need all of those signals without turning the analytics platform into the operational system of record.

This project models that problem as a small event-driven integration lab.

The application demonstrates:

- system-of-record ownership
- versioned event contracts
- REST API ingestion
- event routing
- idempotent processing
- correlation IDs
- bounded retries
- transient versus permanent failure
- dead-letter handling
- contract validation
- schema-version rejection
- traceable lineage
- delivery attempt history
- observability metrics
- synthetic end-to-end scenarios
- automated integration behavior tests

The core message is:

> **Enterprise integration is not merely connecting APIs. It is governing ownership, contracts, failure behavior, duplicate safety, compatibility, and observability across independently owned systems.**

---

## 2. Business / Capability Problem

A global learning ecosystem may need to answer questions such as:

- When a new employee is provisioned, how should learning eligibility be synchronized?
- When an employee changes roles, which system owns that fact?
- How should learning completion contribute to capability mastery?
- How should mastery inform operational tools without the LMS becoming the CRM?
- How can CRM adoption signals flow into learning-effectiveness analytics?
- What happens when a destination is temporarily unavailable?
- What happens when a delivery fails permanently?
- How do we prevent duplicate events from applying the same business action twice?
- How do we trace one employee journey across several systems?
- How do teams evolve event contracts without silently breaking consumers?

This demo makes those questions visible in working code.

---

## 3. Project Thesis

The design follows five principles:

1. **Define system ownership first.** Integration should connect systems, not erase domain boundaries.
2. **Treat events as contracts.** Every event has explicit type, version, required fields, ownership, and routing.
3. **Design for at-least-once delivery realities.** Duplicate safety is required, not optional.
4. **Make failure a product behavior.** Retries, exhausted failures, dead letters, and operator visibility are part of the architecture.
5. **Trace business journeys, not only individual requests.** Correlation IDs connect related events and attempts.

---

## 4. Current Status

**Status:** Implemented MVP  
**Version:** `0.1.0`  
**Framework:** FastAPI  
**Persistence:** SQLite  
**External services:** None required  
**Test status:** `11 passed`

The MVP is deliberately portable and deterministic for an interview setting. It models the integration control plane without requiring access to real HRIS, LMS, CRM, cloud-broker, or analytics credentials.

---

## 5. Supported Use

The project is suitable for:

- architecture demonstrations
- integration-pattern interviews
- API-contract discussions
- event-driven design discussions
- system-of-record discussions
- resilience / retry discussions
- observability demonstrations
- data-lineage demonstrations
- technical portfolio review

It is not intended for:

- real employee data
- patient data
- real CRM data
- production integrations
- regulated records
- production identity synchronization
- production learning records

---

## 6. Implemented Features

### Integration architecture

- HRIS → LMS / Data Platform
- HRIS role changes → LMS / Capability / Data Platform
- LMS learning assignment events
- LMS completion events → Capability / Data Platform
- Capability updates → CRM / Data Platform
- CRM adoption events → Data Platform
- analytics refresh events

### Reliability

- unique idempotency key
- duplicate suppression
- maximum three delivery attempts
- transient failure recovery
- permanent failure handling
- dead-letter queue
- per-attempt status history

### Governance

- explicit schema version
- required field validation
- unsupported-version rejection
- system-of-record catalog
- event-contract catalog
- explicit source system
- explicit destinations

### Observability

- correlation ID
- event stream
- delivery-attempt history
- DLQ view
- lineage endpoint
- dashboard metrics
- API documentation

---

## 7. Reference Architecture

```text
HRIS
 │  identity / role
 ▼
Integration Contract Layer
 │  validate • idempotency • route • trace
 ├──────────────────────────────┐
 ▼                              ▼
LMS                        Data Platform
 │ learning completion           ▲
 ▼                               │
Capability ───────► CRM ─────────┘
 mastery          adoption
```

A more detailed version is in [`ARCHITECTURE.md`](ARCHITECTURE.md).

---

## 8. System-of-Record Boundaries

| Domain | System of Record |
|---|---|
| Employee identity | HRIS |
| Employment role | HRIS |
| Learning assignment | LMS |
| Learning completion | LMS |
| Capability mastery | Capability Service |
| Commercial workflow adoption | CRM |
| Cross-system analytics | Data Platform |

This is one of the most important architectural choices in the demo.

The integration layer **does not become the system of record**. It validates and transports facts owned by other domains.

---

## 9. Runtime Processing Flow

```text
Event received
  ↓
Pydantic envelope validation
  ↓
Contract validation
  ├─ Unsupported schema → REJECTED
  ├─ Missing required field → REJECTED
  └─ Valid
       ↓
Idempotency check
  ├─ Seen key → DUPLICATE
  └─ New
       ↓
Persist event
       ↓
Resolve destinations
       ↓
Delivery attempt
  ├─ Success → SUCCESS
  └─ Failure
       ↓
Retry up to 3 attempts
  ├─ Eventually success → PROCESSED
  └─ Exhausted → DEAD_LETTERED
```

---

## 10. Event Envelope

Every event contains:

```json
{
  "event_id": "unique-message-id",
  "event_type": "learning.completed",
  "schema_version": "1.0",
  "occurred_at": "2026-08-26T20:00:00Z",
  "source_system": "LMS",
  "subject_id": "EMP-1042",
  "correlation_id": "business-journey-id",
  "idempotency_key": "stable-business-operation-key",
  "payload": {
    "employee_id": "EMP-1042",
    "learning_asset_id": "CRM-ONBOARD-101",
    "completed_at": "2026-08-26T20:00:00Z",
    "score": 92
  }
}
```

See [`EVENT_CATALOG.md`](EVENT_CATALOG.md) for every implemented event.

---

## 11. Why `event_id`, `correlation_id`, and `idempotency_key` Are Different

These identifiers solve different problems.

### `event_id`

Identifies one emitted message.

### `correlation_id`

Connects multiple messages and delivery attempts belonging to the same business journey.

Example:

```text
Provision employee
→ assign learning
→ complete learning
→ update capability
→ observe CRM adoption
```

All can share one correlation ID while remaining separate events.

### `idempotency_key`

Protects the business operation from being applied twice.

A duplicate producer retry could use a different event ID but the same idempotency key. The integration layer should suppress the repeated business operation.

---

## 12. Event Catalog

Implemented event types:

1. `employee.provisioned`
2. `employee.role_changed`
3. `learning.assigned`
4. `learning.completed`
5. `capability.updated`
6. `crm.adoption_recorded`
7. `analytics.refreshed`

The API exposes the active catalog at:

```text
GET /api/contracts
```

---

## 13. Routing Model

| Event | Destination(s) |
|---|---|
| `employee.provisioned` | LMS, Data Platform |
| `employee.role_changed` | LMS, Capability, Data Platform |
| `learning.assigned` | Data Platform |
| `learning.completed` | Capability, Data Platform |
| `capability.updated` | CRM, Data Platform |
| `crm.adoption_recorded` | Data Platform |
| `analytics.refreshed` | none |

The routing table is deliberately explicit in code rather than hidden inside UI behavior.

---

## 14. Idempotency Strategy

The SQLite event store enforces a uniqueness constraint on `idempotency_key`.

If the same business operation is published again:

```text
First delivery → PROCESSED
Second delivery with same key → DUPLICATE
Downstream deliveries on second event → 0
```

This models a core distributed-systems requirement: producers and networks can retry; consumers should remain safe.

---

## 15. Retry Strategy

The MVP uses a bounded retry budget:

```text
MAX_ATTEMPTS = 3
```

The demo supports three failure modes:

- `none` — immediate success
- `transient` — fails attempts 1 and 2, succeeds on attempt 3
- `permanent` — fails all attempts and enters the DLQ

Production retry design would additionally consider:

- exponential backoff
- jitter
- error classification
- destination-specific policies
- circuit breaking
- broker redelivery semantics
- retry-after headers
- rate limits

---

## 16. Dead-Letter Queue

When the retry budget is exhausted, the demo stores:

- event ID
- destination system
- correlation ID
- failure reason
- original payload
- creation timestamp

The UI exposes these records rather than treating failure as silent data loss.

A production DLQ requires controlled replay, authorization, audit logging, and data-retention rules.

---

## 17. Schema Versioning

The current catalog supports:

```text
1.0
```

An event with an unsupported version is rejected before it is persisted or delivered.

This is intentionally visible in the tests because schema compatibility is a team contract, not just a serialization detail.

Production architecture would likely use:

- schema registry
- compatibility policy
- consumer contract tests
- additive-change conventions
- formal deprecation windows
- dual-read/dual-write migration where required

---

## 18. Contract Validation

Each event type has a required payload-field set.

Example:

`learning.completed` requires:

- `employee_id`
- `learning_asset_id`
- `completed_at`
- `score`

Missing fields produce `REJECTED` before downstream routing.

This protects downstream systems from receiving malformed domain events.

---

## 19. Correlation and Data Lineage

Every event and delivery attempt stores the same business correlation ID.

The endpoint:

```text
GET /api/lineage/{correlation_id}
```

returns:

- events
- delivery attempts
- dead letters

The dashboard renders that as a timeline.

This is the foundation for answering questions such as:

> “Why did this employee's CRM adoption signal never appear in analytics?”

without manually searching five unrelated logs.

---

## 20. Data Model

SQLite tables:

### `events`

Stores accepted domain events and current processing state.

### `deliveries`

Stores each downstream delivery attempt separately.

### `dead_letters`

Stores exhausted failures requiring operator attention.

The demo intentionally separates the event from delivery attempts because one event can have multiple destinations and multiple attempts per destination.

---

## 21. API Surface

### Health

```text
GET /health
```

### Publish an event

```text
POST /api/events
```

### Event history

```text
GET /api/events
```

### Delivery history

```text
GET /api/deliveries
```

### Dead letters

```text
GET /api/dead-letters
```

### Correlation lineage

```text
GET /api/lineage/{correlation_id}
```

### Contract catalog

```text
GET /api/contracts
```

### System-of-record map

```text
GET /api/system-of-record
```

### Metrics

```text
GET /api/metrics
```

### Reset synthetic lab

```text
POST /api/demo/reset
```

### Run scenario

```text
POST /api/demo/scenarios/{scenario}
```

Swagger is available at:

```text
/docs
```

---

## 22. Built-in Demo Scenarios

### `happy-path`

Creates a six-event employee journey:

```text
Provision
→ Assignment
→ Completion
→ Capability
→ CRM Adoption
→ Analytics Refresh
```

### `duplicate`

Publishes the same business event twice and demonstrates idempotent suppression.

### `retry-success`

Generates transient failures that recover on attempt 3.

### `dead-letter`

Generates permanent failures that exhaust retries and enter the DLQ.

---

## 23. Repository Structure

```text
03-lms-crm-data-integration/
│
├── app/
│   ├── __init__.py
│   ├── contracts.py
│   ├── db.py
│   ├── main.py
│   ├── models.py
│   ├── processor.py
│   ├── scenarios.py
│   └── static/
│       └── index.html
│
├── tests/
│   └── test_api.py
│
├── .gitignore
├── ARCHITECTURE.md
├── DEMO_WALKTHROUGH.md
├── EVENT_CATALOG.md
├── README.md
├── pyproject.toml
└── requirements.txt
```

---

## 24. Technology Stack

- **Python 3.11+**
- **FastAPI** — typed REST API and Swagger/OpenAPI
- **Pydantic** — envelope/data validation
- **SQLite** — portable event/delivery/DLQ persistence
- **Vanilla HTML/CSS/JavaScript** — dependency-light monitoring UI
- **pytest** — regression and integration-behavior testing

The stack is intentionally small so the architecture can be inspected without infrastructure setup distracting from the integration concepts.

---

## 25. Installation

```bash
git clone https://github.com/JohnCurry28/Jazz-Interview-Portfolio.git
cd Jazz-Interview-Portfolio/03-lms-crm-data-integration
python -m venv .venv
```

Activate the environment.

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

macOS/Linux:

```bash
source .venv/bin/activate
```

Install:

```bash
pip install -r requirements.txt
```

---

## 26. Running the Application

```bash
uvicorn app.main:app --reload
```

Open:

```text
http://127.0.0.1:8000
```

Swagger:

```text
http://127.0.0.1:8000/docs
```

---

## 27. Reset Behavior

The application creates `integration_lab.db` locally.

To reset using the API:

```text
POST /api/demo/reset
```

The database file is intentionally excluded from Git.

---

## 28. Automated Tests

Run:

```bash
pytest -q
```

Current result:

```text
11 passed
```

Coverage includes:

- health check
- correct destination routing
- idempotent duplicate suppression
- transient retry recovery
- permanent failure → DLQ
- unsupported schema rejection
- missing-field contract rejection
- system-of-record boundaries
- happy-path lineage
- contract catalog
- unknown correlation behavior

---

## 29. Failure Testing Philosophy

The project intentionally tests failure paths because successful API calls are the easy part of integration engineering.

Key questions are:

- What if the same message arrives twice?
- What if a consumer is down temporarily?
- What if it never recovers?
- What if the producer sends an incompatible version?
- What if a required field is missing?
- Can an operator trace the business journey afterward?

---

## 30. Observability

The MVP exposes:

- event count
- delivery count
- successful deliveries
- delivery success rate
- retry attempts
- dead-letter count
- unique idempotency keys
- event stream
- attempt stream
- DLQ records
- correlation lineage

Production observability would add:

- structured logs
- distributed traces
- OpenTelemetry
- queue lag
- consumer lag
- p50/p95/p99 delivery latency
- retry rate by destination
- DLQ alerting
- SLOs / error budgets
- dashboards and alert routing

---

## 31. Security and Privacy Boundaries

The demo contains no real credentials or real personal data.

Production architecture would require:

- OIDC/OAuth 2.x
- workload/service identity
- API gateway
- mTLS or equivalent service trust where appropriate
- least-privilege authorization
- secrets manager
- encrypted transport and storage
- field minimization
- retention policies
- audit logs
- privacy classification
- environment segregation
- incident response
- security review

The integration layer should transport only data needed by each consumer.

---

## 32. PII Minimization

The synthetic event examples include an email only to make HRIS provisioning understandable.

A production architecture should ask:

> Does this consumer actually need the employee's email, or only an immutable enterprise identity key?

Minimizing propagated fields reduces privacy exposure and coupling.

---

## 33. Build vs. Buy Considerations

This repository does not imply that an enterprise should custom-build its own broker or integration platform.

A Tech Lead would evaluate:

- existing enterprise integration platform
- iPaaS capabilities
- managed event broker
- vendor-native LMS/CRM connectors
- API gateway
- data platform ingestion capabilities
- organizational support model
- observability tooling
- security standards
- total cost of ownership
- lock-in and portability

The reference implementation exists to demonstrate architecture and decision criteria, not to prescribe a specific vendor.

---

## 34. Production Hardening

The MVP uses synchronous in-process delivery simulation for portability.

A production architecture would likely introduce:

```text
Producer
  ↓
Transactional Outbox / API Gateway
  ↓
Managed Event Broker
  ↓
Durable Consumer
  ↓
Destination Adapter
  ↓
Target System
```

Additional hardening:

- durable queues/topics
- consumer groups
- transactional outbox/inbox where required
- schema registry
- contract compatibility tests
- poison-message controls
- authorized replay
- exponential backoff + jitter
- circuit breaker
- rate limiting
- disaster recovery
- backup and retention policy
- managed database
- CI/CD gates

---

## 35. Known Limitations

The MVP intentionally simplifies:

- broker infrastructure
- asynchronous concurrency
- real downstream HTTP clients
- OAuth/service identities
- replay workflow
- schema registry
- encryption controls
- real observability stack
- regional deployment
- high availability
- distributed transactions
- eventual-consistency conflict resolution

These are documented boundaries, not hidden assumptions.

---

## 36. Troubleshooting

### App will not start

Confirm dependencies:

```bash
pip install -r requirements.txt
```

### Port already in use

```bash
uvicorn app.main:app --reload --port 8010
```

### Database state is confusing

Use:

```text
POST /api/demo/reset
```

or delete `integration_lab.db` while the app is stopped.

### Import errors

Run Uvicorn from the demo root where the `app/` directory exists.

---

## 37. Interview Demo Sequence

Recommended sequence:

1. Explain system-of-record boundaries.
2. Run **Happy Path**.
3. Click one event and show correlation lineage.
4. Open `/api/contracts` in Swagger.
5. Run **Show Idempotency**.
6. Run **Show Retry Recovery**.
7. Run **Show Dead Letter**.
8. Explain how the synchronous MVP becomes a broker-backed production architecture.

Full script: [`DEMO_WALKTHROUGH.md`](DEMO_WALKTHROUGH.md).

---

## 38. Architecture-Defense Questions

### Why not have the LMS own capability mastery?

Because capability may include evidence beyond course completion, including practice, manager observation, assessment, workflow behavior, and other operational evidence. Separating the domain prevents LMS completion semantics from becoming the entire capability model.

### Why send capability to CRM?

The demo illustrates a potential role-aware operational signal, not a recommendation to write training records into CRM. The exact payload and use case would depend on privacy, business requirements, and the target CRM architecture.

### Why not integrate every system directly with every other system?

Point-to-point integration creates tight coupling, duplicated transformation logic, inconsistent failure handling, and difficult observability. Governed APIs/events and an integration layer reduce those problems.

### Why use idempotency when there is already an event ID?

Because duplicate business operations can be emitted with different message IDs. Idempotency protects the operation, not only the transport message.

### Why a dead-letter queue?

Because permanent failure should become observable operator work rather than silent loss or infinite retry loops.

### Why not exactly-once delivery?

Exactly-once semantics across distributed heterogeneous systems are difficult and often expensive. A practical design often uses at-least-once delivery plus idempotent consumers and clear reconciliation.

---

## 39. Roadmap

Potential next iterations:

- real asynchronous broker adapter
- Kafka/EventBridge/Azure Service Bus adapter interface
- outbox pattern
- replay endpoint with approval control
- destination-specific retry policies
- exponential backoff
- schema migration demo `1.0 → 1.1`
- contract compatibility tests
- OpenTelemetry traces
- real data-lineage graph
- consumer lag metrics
- role-change workflow
- connection to Demo 01 capability hub
- connection to Demo 04 analytics

---

## 40. Technical Lead Talking Points

This demo is intended to support statements such as:

> “I separate the source of truth from the integration mechanism.”

> “I treat API and event schemas as governed contracts between teams.”

> “I assume retries and duplicate delivery will happen, so idempotency is part of the design.”

> “A failed integration isn't complete until it is observable, triageable, and safely replayable.”

> “Correlation IDs let us trace a business outcome across multiple technical systems.”

> “I would choose the actual broker, iPaaS, or native connector based on enterprise standards and build-vs-buy economics; the architectural principles remain the same.”

---

## 41. Project Owner

**John Curry**  
Personal technical portfolio / interview reference implementation.

---

## 42. Disclaimer

This is an independent synthetic portfolio project.

It is not affiliated with, sponsored by, endorsed by, or an internal system of Jazz Pharmaceuticals or any other pharmaceutical company.

No real employee, patient, customer, commercial, clinical, or regulated company data is included.
