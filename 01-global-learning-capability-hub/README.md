# Global Learning Capability Hub

A working, synthetic enterprise learning-technology reference implementation that demonstrates how role-based learning, capability mastery, operational adoption, content governance, APIs, and enterprise data can be modeled as one coherent product.

> **Core design principle:** Completion is an output. Capability and adoption are outcomes.

> **Portfolio note:** This project is part of the `Jazz-Interview-Portfolio`, but it is intentionally generic and uses only synthetic users, synthetic learning content, synthetic business roles, and synthetic operational events. It is not a Jazz Pharmaceuticals application, does not reproduce a Jazz internal platform, and does not contain proprietary or confidential company data.

---

## 1. Executive Summary

The Global Learning Capability Hub is a FastAPI-based reference application built to demonstrate a product-oriented approach to enterprise Learning & Development technology.

Instead of organizing the system around a traditional course catalog, the application centers the data model on **roles and capabilities**. Learning assets are treated as one intervention used to build capability, evidence is used to represent demonstrated proficiency, and adoption signals are used to represent whether learning is translating into behavior or system use.

The conceptual flow is:

```text
Role
  ↓
Required Capability
  ↓
Learning Intervention
  ↓
Evidence of Proficiency
  ↓
Observed Adoption / Behavior
  ↓
Manager + Product Insight
```

The current MVP demonstrates:

- enterprise learning architecture
- role-based onboarding and learning pathways
- capability / competency modeling
- learner mastery and evidence tracking
- manager readiness and intervention-risk views
- learning-asset governance and lifecycle management
- API-based data access
- learning-completion writeback
- synthetic enterprise integration events
- correlation IDs for integration traceability
- operational dashboards
- Swagger / OpenAPI documentation
- automated API testing
- a clear path toward enterprise AI, RAG, analytics, and event-driven integration

The project is designed to support both a **business/product conversation** and a **technical architecture conversation** during an interview.

---

## 2. Why This Project Exists

Many learning systems report operational activity very well:

- enrollment
- completion
- score
- time spent
- certificate status

Those measures matter, but they do not necessarily answer the more important questions:

- Did the employee develop the required capability?
- Is the employee applying the capability?
- Is a tool or workflow actually being adopted?
- Does the manager know where intervention is needed?
- Are learning assets governed and reusable?
- Can learning data move reliably between HRIS, LMS, CRM, content, and analytics systems?
- Can the platform evolve without becoming a collection of disconnected point solutions?

This reference implementation was created to demonstrate how those questions can be represented technically.

---

## 3. Product Thesis

The application is based on five architectural ideas.

### 3.1 Roles should drive capability requirements

The system first asks:

> What does this role need to be able to do?

A Sales Representative, Marketing Manager, CX / Omnichannel Specialist, and People Manager do not need identical capability targets.

### 3.2 Capabilities should drive interventions

The platform does not assume that a course is always the solution.

A capability may be supported by:

- course
- simulation
- workshop
- microlearning
- job aid
- coaching
- workflow support
- AI-enabled performance support

### 3.3 Evidence should matter more than completion alone

A completed course is one signal. Demonstrated proficiency is another.

The data model therefore stores `mastery_pct` and `evidence_count` separately from learning-assignment status.

### 3.4 Adoption should be visible

A learner may complete onboarding while still showing weak CRM, workflow, or capability adoption.

The manager experience intentionally surfaces this difference.

### 3.5 Learning content should be governed like a product asset

Enterprise assets should have:

- ownership
- version
- lifecycle state
- review dates
- capability mapping
- reusability
- retirement logic

This prevents learning content from becoming an ungoverned set of duplicate files and disconnected courses.

---

## 4. Current Project Status

**Version:** `0.1.0`

**Status:** Working MVP / interview reference implementation

**Runtime:** FastAPI + Jinja2 + vanilla JavaScript + SQLite

**Test status:** Core API tests implemented for health, overview, learner capability, and governance endpoints.

### Implemented

- [x] Executive / product overview
- [x] Learner persona selector
- [x] Role-based capability requirements
- [x] Capability mastery view
- [x] Evidence-count display
- [x] Personalized learning path
- [x] Manager readiness dashboard
- [x] Adoption-risk classification
- [x] Learning-asset governance table
- [x] Version / status / owner / review metadata
- [x] Integration event log
- [x] Correlation IDs
- [x] REST API endpoints
- [x] Completion writeback endpoint
- [x] SQLite seed data
- [x] Swagger / OpenAPI explorer
- [x] Automated tests
- [x] Responsive front-end layout
- [x] Interview walkthrough documentation
- [x] Architecture documentation

### Planned

- [ ] enterprise authentication / SSO simulation
- [ ] RBAC / ABAC authorization model
- [ ] API gateway pattern
- [ ] event queue / message-bus simulation
- [ ] retry / dead-letter processing
- [ ] integration contract schemas
- [ ] richer audit logging
- [ ] structured telemetry / observability
- [ ] PostgreSQL production profile
- [ ] migration framework
- [ ] AI Performance Coach / RAG module
- [ ] assessment intelligence module
- [ ] content-governance AI agent
- [ ] product-operations / technical-debt dashboard

---

## 5. Supported and Prohibited Use

### Appropriate use

This project is appropriate for:

- interview demonstration
- architecture discussion
- learning-platform prototyping
- API / data-model discussion
- enterprise L&D product-thinking examples
- synthetic capability analytics
- demonstration of build-vs-buy and integration reasoning

### Not intended for

This project is **not** intended to be used as:

- a production pharmaceutical learning platform
- a validated regulated-content system
- a system containing patient data
- a system containing employee PII
- a replacement for formal LMS, CRM, HRIS, or quality platforms
- a representation of any employer's internal architecture
- a compliance or legal decision system

All sample data is synthetic.

---

## 6. Feature Overview

### 6.1 Executive / Product Overview

The Overview page displays six headline indicators:

- active users
- average onboarding progress
- average mastery
- average adoption
- reusable learning assets
- integration health

It also visualizes the core model:

```text
Role Profile → Capability → Learning → Evidence → Adoption
```

This view is designed to frame the application as an enterprise capability product rather than a traditional LMS dashboard.

### 6.2 Learner Experience

The learner view allows switching among synthetic personas.

For each learner, the system displays:

- role
- region
- manager
- onboarding progress
- average capability mastery
- adoption percentage
- role-required capabilities
- target capability level
- capability category
- current mastery
- evidence-event count
- mapped learning assets
- learning status
- score
- due date
- asset version

The learning path is built from the learner's role requirements and mapped learning assets.

### 6.3 Manager Readiness

The manager view compares team members across:

- onboarding
- capability mastery
- adoption
- intervention risk

Current demo risk logic is intentionally simple:

```text
adoption < 60     → High
adoption 60–74    → Medium
adoption >= 75    → Low
```

This is a demonstration heuristic, not a production decision rule.

The business concept is more important than the current thresholds: **high completion does not automatically imply capability or adoption**.

### 6.4 Governance

The governance view treats content as managed product assets.

Each learning asset contains:

- title
- asset type
- mapped capability
- version
- governance status
- owner
- last-reviewed date
- reusable flag

The seeded dataset includes:

- approved assets
- an asset in review
- a retirement candidate

This allows the interview discussion to include lifecycle management rather than only content creation.

### 6.5 Integration Health

The integration view presents synthetic events moving across systems such as:

```text
HRIS / Identity
      ↓
Learning Hub
      ↔
LMS / Content
      ↔
CRM
      ↓
Enterprise Data
      ↓
Analytics
```

The seeded events include:

- `USER_PROVISIONED`
- `LEARNING_ASSIGNED`
- `COURSE_COMPLETED`
- `CAPABILITY_UPDATED`
- `ADOPTION_EVENT`
- `CONTENT_PUBLISHED`
- `DATA_SYNC`

Each event contains:

- source
- destination
- status
- timestamp
- correlation ID

A warning event is deliberately included so the demo does not represent only a happy-path integration scenario.

### 6.6 API Explorer

FastAPI automatically generates OpenAPI documentation.

When the application is running:

- Swagger UI: `http://127.0.0.1:8000/docs`
- OpenAPI document: `http://127.0.0.1:8000/openapi.json`

This is an important part of the technical interview demonstration because it shows that the user interface is backed by real endpoints rather than static mockups.

---

## 7. Architecture Overview

```text
                           USERS
                             │
              ┌──────────────┼──────────────┐
              │              │              │
           Learner        Manager        Product/Admin
              │              │              │
              └──────────────┼──────────────┘
                             ▼
                 Learning Capability Hub
                             │
       ┌─────────────────────┼─────────────────────┐
       │                     │                     │
   Experience            Capability          Governance
   LMS / LXP             Roles / Skills      Assets / Versions
   Onboarding            Pathways            Review / Reuse
       │                     │                     │
       └─────────────────────┼─────────────────────┘
                             ▼
                     API / Event Layer
                             │
       ┌────────────┬────────┼─────────┬───────────┐
       ▼            ▼        ▼         ▼           ▼
     HRIS         LMS      CRM     Content       Data / BI
   Identity      Events   Adoption  Repository   Analytics
```

### Logical architecture layers

1. **Experience layer** — learner, manager, product-owner, and platform-administration experiences.
2. **Capability layer** — roles, capabilities, target levels, mastery, and evidence.
3. **Learning layer** — courses, simulations, workshops, microlearning, job aids, assignments, and scores.
4. **Governance layer** — asset version, owner, status, review date, reuse, and retirement.
5. **Integration layer** — REST APIs now; event-driven contracts planned.
6. **Data layer** — SQLite for portability in the reference implementation.
7. **Analytics layer** — onboarding, mastery, adoption, risk, product health, and later assessment intelligence.
8. **AI layer (planned)** — role-aware RAG, coaching, evaluation, grounding, refusal behavior, and auditability.

See [`ARCHITECTURE.md`](./ARCHITECTURE.md) for additional architecture rationale and production considerations.

---

## 8. Request and Data Flow

### Read workflow

```text
Browser
   ↓
Vanilla JavaScript fetch()
   ↓
FastAPI route
   ↓
Parameterized SQLite query
   ↓
Python dictionary serialization
   ↓
JSON response
   ↓
Browser rendering
```

### Completion workflow

```text
Client
  ↓
POST /api/learning/completions
  ↓
Pydantic validation
  ↓
Validate user + asset
  ↓
Insert/update learning assignment
  ↓
Derive synthetic mastery signal
  ↓
Insert/update user capability evidence
  ↓
Create integration event
  ↓
Commit transaction
  ↓
Return recorded status
```

This endpoint is deliberately useful in an interview because it shows how one learning event can update multiple bounded pieces of product state.

---

## 9. Repository Structure

```text
01-global-learning-capability-hub/
│
├── app/
│   ├── __init__.py
│   ├── db.py
│   ├── main.py
│   │
│   ├── static/
│   │   ├── app.js
│   │   └── styles.css
│   │
│   └── templates/
│       └── index.html
│
├── data/
│   └── capability_hub.db        # generated locally; ignored by Git
│
├── tests/
│   ├── conftest.py
│   └── test_api.py
│
├── .gitignore
├── ARCHITECTURE.md
├── DEMO_WALKTHROUGH.md
├── README.md
├── pyproject.toml
└── requirements.txt
```

### Important files

| File | Responsibility |
|---|---|
| `app/main.py` | FastAPI application, routes, request validation, query orchestration, completion writeback |
| `app/db.py` | SQLite connection, schema creation, seed data |
| `app/templates/index.html` | Application shell and dashboard views |
| `app/static/app.js` | API calls, navigation, view rendering, client-side UI logic |
| `app/static/styles.css` | Responsive visual design and status styles |
| `tests/test_api.py` | API smoke / behavior tests |
| `ARCHITECTURE.md` | Logical layers, integration rationale, production-hardening discussion |
| `DEMO_WALKTHROUGH.md` | Rehearsable interview demonstration script |
| `requirements.txt` | Python dependencies |
| `pyproject.toml` | Project metadata and pytest configuration |

---

## 10. Technology Stack

### Backend

- Python 3.11+
- FastAPI
- Pydantic
- Uvicorn
- SQLite

### Frontend

- Jinja2 template rendering
- semantic HTML
- vanilla JavaScript
- CSS
- Fetch API

### Testing

- pytest
- FastAPI `TestClient`
- HTTPX dependency

### Why this stack

The goal of the MVP is portability, transparency, and interview readability.

A reviewer can inspect the full application without needing a large framework or cloud account.

The stack is intentionally simple enough to explain in a technical interview while still demonstrating:

- API contracts
- typed request validation
- persistence
- data relationships
- transactional updates
- front-end/API separation
- testability

---

## 11. Database and Data Model

The demo database is created automatically on startup.

### Core tables

#### `roles`
Defines enterprise role profiles.

Fields include:

- `id`
- `name`
- `description`

#### `users`
Synthetic employee/persona records.

Fields include:

- `id`
- `name`
- `role_id`
- `region`
- `manager`
- `onboarding_pct`
- `adoption_pct`

#### `capabilities`
Defines business, digital, data, AI, governance, and leadership capabilities.

#### `role_capabilities`
Many-to-many mapping between roles and capabilities plus target proficiency level.

#### `user_capabilities`
Stores current synthetic mastery and evidence count for a learner/capability pair.

#### `learning_assets`
Governed learning objects mapped to capabilities.

#### `learning_assignments`
Learner-to-asset relationship containing status, score, and due date.

#### `integration_events`
Synthetic trace of enterprise events across systems.

### Relationship model

```text
roles
  │
  ├────< users
  │
  └────< role_capabilities >──── capabilities
                                  │
                                  ├────< user_capabilities >──── users
                                  │
                                  └────< learning_assets
                                           │
                                           └────< learning_assignments >──── users

integration_events
  └──── independent synthetic operational trace
```

### Important modeling decision

`learning_assets` are **not** the parent object of the entire architecture.

The center of the product model is:

```text
Role ↔ Capability
```

Learning content is attached to that capability model.

This creates a clearer path toward adaptive learning, manager coaching, AI performance support, capability analytics, and reuse across multiple curricula.

---

## 12. Synthetic Domain Model

### Seeded roles

- Sales Representative
- Marketing Manager
- CX / Omnichannel Specialist
- People Manager

### Seeded capabilities

- Product & Disease-State Knowledge
- CRM Execution
- Omnichannel Engagement
- Data Literacy
- AI-Enabled Ways of Working
- Compliance & Governance
- Coaching & Capability Leadership

### Seeded learning asset types

- Course
- Simulation
- Workshop
- Microlearning
- Job Aid

The terminology is intentionally generic and designed only to demonstrate enterprise capability architecture.

---

## 13. API Reference

### Health

#### `GET /health`

Returns application health.

Example:

```json
{
  "status": "ok",
  "service": "global-learning-capability-hub"
}
```

### Roles

#### `GET /api/roles`

Returns the synthetic role catalog.

### Users

#### `GET /api/users`

Returns all synthetic personas and top-level onboarding/adoption information.

#### `GET /api/users/{user_id}`

Returns role and profile context for one persona.

Returns HTTP `404` when the user does not exist.

### Capability

#### `GET /api/users/{user_id}/capabilities`

Returns required capabilities for the learner's role and combines:

- target level
- current mastery
- evidence count
- capability metadata

### Learning Path

#### `GET /api/users/{user_id}/learning-path`

Returns the role-mapped learning assets for the selected user.

The current sort order prioritizes:

1. In Progress
2. Assigned
3. Recommended
4. Completed

Retired assets are excluded.

### Product Overview

#### `GET /api/dashboard/overview`

Aggregates:

- active users
- onboarding average
- adoption average
- mastery average
- evidence events
- active assets
- reusable assets
- items in review
- retirement candidates
- integration-event counts
- successful integration events

### Manager Dashboard

#### `GET /api/dashboard/manager`

Returns learner readiness plus current synthetic intervention-risk classification.

### Governance

#### `GET /api/governance/assets`

Returns governed learning assets including version, owner, review date, status, and reuse flag.

### Integration Events

#### `GET /api/integrations/events`

Returns synthetic integration events in reverse chronological order.

### Completion Writeback

#### `POST /api/learning/completions`

Records a completion and generates related capability/evidence and integration-state changes.

Request:

```json
{
  "user_id": 1,
  "asset_id": 5,
  "score": 91
}
```

Validation:

- `user_id` must reference a valid user
- `asset_id` must reference a valid asset
- `score` must be between `0` and `100`

Current synthetic mastery calculation:

```text
new_mastery = min(100, round(score * 0.85 + 12))
```

If the user already has mastery evidence for the capability, the current value is averaged with the new derived value and the evidence count increments.

This is demonstration logic only. A production mastery model should be grounded in a formal assessment and capability-measurement framework.

---

## 14. Front-End Behavior

The application uses a single-page dashboard shell with multiple client-rendered views.

### Navigation

- Overview
- Learner Experience
- Manager Readiness
- Governance
- Integration Health
- API Explorer

### Browser data loading

`app/static/app.js` loads the views through the FastAPI endpoints.

At startup, it requests:

- overview metrics
- users
- manager dashboard
- governance assets
- integration events

Learner-specific capability and path data are loaded when the persona changes.

### Error handling

The current client wrapper throws when a response is not successful and surfaces a general browser alert if initial demo data fails to load.

Production UX would replace this with structured error states, retry behavior, telemetry, and user-safe messages.

---

## 15. Local Setup

### Prerequisites

- Python 3.11 or newer
- `pip`
- terminal / PowerShell
- modern browser

Git is recommended but not required to run the application after download.

### 1. Clone the portfolio

```bash
git clone https://github.com/JohnCurry28/Jazz-Interview-Portfolio.git
cd Jazz-Interview-Portfolio/01-global-learning-capability-hub
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the environment

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Windows Command Prompt:

```cmd
.venv\Scripts\activate.bat
```

macOS / Linux:

```bash
source .venv/bin/activate
```

### 4. Upgrade pip

```bash
python -m pip install --upgrade pip
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Start the application

```bash
uvicorn app.main:app --reload
```

### 7. Open the application

```text
http://127.0.0.1:8000
```

### 8. Open Swagger

```text
http://127.0.0.1:8000/docs
```

---

## 16. Environment Variables

Version `0.1.0` does **not** require environment variables because:

- all data is synthetic
- there is no external API dependency
- there are no credentials
- there is no LLM provider yet
- there is no external database

Future modules should move secrets and environment-specific configuration into environment variables or a secrets manager.

A future `.env.example` may include values such as:

```text
DATABASE_URL=
OIDC_ISSUER=
OIDC_CLIENT_ID=
API_GATEWAY_URL=
LLM_PROVIDER=
VECTOR_STORE_URL=
```

No real credentials should ever be committed to the repository.

---

## 17. Database Initialization and Reset

The SQLite database is created automatically by `init_db()` during FastAPI lifespan startup.

The local database path is:

```text
data/capability_hub.db
```

The database file is ignored by Git.

### Reset demo data

Stop the app, delete the generated database, and restart:

Windows PowerShell:

```powershell
Remove-Item .\data\capability_hub.db
uvicorn app.main:app --reload
```

macOS / Linux:

```bash
rm data/capability_hub.db
uvicorn app.main:app --reload
```

The schema and seed data will be recreated automatically.

---

## 18. Testing

Run:

```bash
pytest -q
```

### Current automated tests

#### Health test

Verifies:

- HTTP 200
- `status == "ok"`

#### Overview test

Verifies:

- dashboard endpoint responds successfully
- seeded active-user data is present
- adoption metric is returned

#### Learner capability test

Verifies:

- learner capability endpoint responds successfully
- the seeded learner has expected capability records

#### Governance test

Verifies:

- governance endpoint responds successfully
- the dataset includes an `In Review` lifecycle state

### Planned test expansion

- POST completion success
- invalid user
- invalid asset
- score validation
- learning-path ordering
- retired-asset exclusion
- mastery update behavior
- evidence-count increment
- integration-event creation
- database reset / seed idempotency
- manager-risk boundary tests
- browser-level end-to-end tests

---

## 19. Evaluation Strategy

For this demo, evaluation is currently deterministic and test-based rather than model-based.

As the platform adds the AI Performance Coach, evaluation should expand to include:

- retrieval hit rate
- recall@K
- precision@K
- source-filter accuracy
- no-result behavior
- answer correctness
- faithfulness / groundedness
- citation accuracy
- completeness
- conflicting-source handling
- unsupported-answer refusal accuracy
- role / authorization retrieval boundaries
- prompt-injection resistance

The goal is to treat AI evaluation as part of the product architecture rather than as an afterthought.

---

## 20. Integration Design

The MVP uses synchronous REST APIs and synthetic event records.

A production enterprise architecture would likely use a combination of:

### Request / response APIs

Good for:

- user/profile lookup
- role lookup
- capability lookup
- learning assignment creation
- status queries

### Events

Good for:

- user provisioned
- role changed
- learning assigned
- learning completed
- assessment completed
- capability changed
- content published
- content retired
- CRM adoption observed

### Production integration controls

- correlation IDs
- idempotency keys
- retry policies
- exponential backoff
- dead-letter queues
- schema versioning
- consumer contracts
- payload validation
- service authentication
- event replay
- observability
- ownership / escalation paths

### Example future flow

```text
HRIS
  │ USER_PROVISIONED / ROLE_CHANGED
  ▼
Integration Layer
  ▼
Capability Service
  │
  ├── assigns required capabilities
  └── requests learning-path update
       ▼
      LMS
       │ COURSE_COMPLETED
       ▼
Event Bus
  ├── Capability Service
  ├── Data Platform
  └── Analytics

CRM
  │ ADOPTION_EVENT
  ▼
Data Platform
  ▼
Capability Analytics
  ▼
Manager Dashboard
```

---

## 21. Security, Privacy, and Governance

The current demo does not contain authentication because it contains no real user or business data.

That is **not** the recommended production design.

### Production security controls

A hardened enterprise version should include:

- enterprise SSO
- OIDC / OAuth 2.x
- role-based access control
- attribute-based authorization where appropriate
- least privilege
- API gateway
- service-to-service authentication
- secrets management
- encryption in transit
- encryption at rest
- audit logging
- security event monitoring
- dependency scanning
- SAST / DAST
- vulnerability management
- threat modeling
- secure SDLC

### Data protection

Production design should explicitly define:

- PII classification
- data minimization
- retention
- deletion
- regional residency
- access review
- log redaction
- backup handling
- analytics de-identification where appropriate

### Regulated-content boundary

This project does not claim to implement pharmaceutical approval or compliance workflows.

Any production design would require governance rules to be defined jointly with the organization's:

- legal
- privacy
- security
- quality
- regulatory
- compliance
- medical / scientific
- business content owners

---

## 22. Observability and Reliability

The event table demonstrates traceability through `correlation_id`, but production observability should be significantly richer.

Recommended production signals:

- structured logs
- distributed traces
- request IDs
- correlation IDs
- latency
- error rate
- event-delivery success
- retry count
- queue depth
- dead-letter volume
- failed data-contract validation
- API availability
- database health
- external dependency health

Recommended operating model:

```text
Monitor
  ↓
Detect
  ↓
Correlate
  ↓
Diagnose
  ↓
Recover
  ↓
Review
  ↓
Improve architecture / backlog
```

---

## 23. Production Hardening

Before production use, the reference implementation would need substantial changes.

### Application

- separate API routers / service layer / repository layer
- dependency injection
- typed response models
- centralized exception handling
- structured logging
- configuration management
- health / readiness / liveness separation

### Database

- PostgreSQL or another managed relational database
- formal migrations
- indexes
- backups
- high availability
- recovery objectives
- connection pooling
- retention rules

### Integration

- API gateway
- message broker / event bus
- retries
- dead-letter processing
- idempotency
- schema registry / contracts
- replay strategy

### Delivery

- Docker image
- CI/CD
- automated quality gates
- infrastructure as code
- environment promotion
- deployment rollback
- release notes

### Operations

- SLOs
- dashboards
- alerting
- incident ownership
- runbooks
- on-call / escalation path
- post-incident review

---

## 24. Accessibility and UX

The interface is responsive and uses semantic HTML patterns where practical, but version `0.1.0` has not undergone a formal WCAG conformance audit.

A production version should include:

- keyboard-navigation verification
- focus-state review
- screen-reader testing
- contrast testing
- ARIA only where necessary
- accessible tables
- accessible status communication
- reduced-motion considerations
- automated and manual accessibility testing

---

## 25. Known Limitations

The following are deliberate MVP limitations:

1. SQLite is local and single-instance.
2. No authentication or authorization is implemented.
3. Adoption percentage is synthetic rather than sourced from a CRM.
4. Mastery calculations are illustrative.
5. Manager risk is a simple threshold heuristic.
6. Integrations are represented as event records rather than live enterprise connections.
7. The UI does not yet perform completion writeback directly.
8. No background worker or event broker is included.
9. No distributed tracing system is connected.
10. No formal regulated-content workflow is implemented.
11. No AI service is included in this first module.
12. No infrastructure or cloud deployment is included in version `0.1.0`.

These limitations are useful interview discussion points because they establish clear boundaries between a reference implementation and production architecture.

---

## 26. Troubleshooting

### `ModuleNotFoundError`

Confirm the virtual environment is active and install requirements:

```bash
pip install -r requirements.txt
```

### `uvicorn` command not found

Run:

```bash
python -m uvicorn app.main:app --reload
```

### Port 8000 already in use

Run on another port:

```bash
uvicorn app.main:app --reload --port 8001
```

Then open:

```text
http://127.0.0.1:8001
```

### Demo data does not look correct

Delete the local database and restart the app. See **Database Initialization and Reset** above.

### Front end loads but no data appears

Check:

1. browser developer console
2. FastAPI terminal output
3. `http://127.0.0.1:8000/health`
4. `http://127.0.0.1:8000/docs`
5. individual API endpoints

### Tests cannot import `app`

Run pytest from the project root:

```bash
pytest -q
```

`pyproject.toml` configures the project root on the Python path.

---

## 27. Interview Demo Walkthrough

A strong demo is approximately 4–6 minutes.

### Step 1 — Frame the problem

Say:

> I built this as a reference implementation of how I think about enterprise L&D as a product rather than a course repository. The central model is Role → Capability → Learning → Evidence → Adoption.

### Step 2 — Overview

Show the KPI cards and architecture tiles.

Key message:

> Course completion is useful operational data, but it is not the final outcome. I want to know whether people developed the required capability and whether that capability is showing up in adoption or performance signals.

### Step 3 — Learner Experience

Change personas.

Show how:

- role changes requirements
- target levels vary
- mastery is independent from completion
- learning is mapped to capability

### Step 4 — Manager Readiness

Show learners with different adoption levels.

Key message:

> If onboarding completion is high but adoption is low, I would not automatically prescribe another course. The cause could be coaching, workflow friction, system usability, incentives, or a genuine capability gap.

### Step 5 — Governance

Show:

- versions
- owners
- review dates
- reusable assets
- in-review content
- retirement candidates

Key message:

> At enterprise scale, content requires lifecycle governance, not just publishing.

### Step 6 — Integration Health

Show event types, sources, destinations, and correlation IDs.

Key message:

> The LMS should not be an island. Identity may originate in HRIS, learning activity in an LMS, adoption in CRM, and analytics in the enterprise data platform.

### Step 7 — Swagger

Open `/docs`.

Show that the dashboard is backed by working endpoints.

Key message:

> The interface is a real API-backed application, not a static visual prototype.

See [`DEMO_WALKTHROUGH.md`](./DEMO_WALKTHROUGH.md) for the condensed rehearsal script.

---

## 28. Architecture Questions to Be Ready For

### Why FastAPI?

FastAPI provides concise typed APIs, Pydantic validation, automatic OpenAPI documentation, asynchronous capability when needed, and a strong fit for service-oriented Python prototypes.

### Why SQLite?

For a demo it minimizes setup and makes the data model portable and inspectable. It is not the recommended production data platform.

### Why not make the LMS the system of record for capability?

An LMS is excellent at learning delivery and completion data, but capability may need to incorporate signals from assessment, CRM, performance systems, manager evaluation, workflow tools, and enterprise analytics. The architecture should therefore avoid assuming one platform owns every dimension of capability.

### Why REST instead of events?

The MVP uses REST for simplicity. A production architecture would use both synchronous APIs and event-driven integration based on use case.

### How would you handle a vendor LMS?

Define the capability contract first, then integrate through supported APIs, webhooks, bulk exchange, LTI/xAPI where appropriate, or an enterprise integration layer. Avoid coupling downstream systems directly to vendor-specific internal data structures where possible.

### Where would AI fit?

The AI layer should sit behind governed enterprise interfaces and consume approved sources, identity/role context, capability data, and learning assets through controlled retrieval and tools. It should not bypass authorization or content-governance boundaries.

---

## 29. Roadmap

This project is intended to become one module within a broader Enterprise Learning Capability OS portfolio.

### Phase 1 — Current

**Global Learning Capability Hub**

- roles
- capability
- learning
- evidence
- adoption
- governance
- integration visibility

### Phase 2

**AI Performance Coach / Enterprise RAG**

- approved-source retrieval
- citations
- role-aware context
- unsupported-answer refusal
- evaluation
- audit logging
- prompt-injection testing

### Phase 3

**LMS ↔ CRM ↔ Enterprise Data Integration Lab**

- richer event schemas
- webhooks
- message processing
- retries
- dead-letter flows
- mapping
- data lineage
- contract tests

### Phase 4

**Assessment Intelligence**

- item difficulty
- discrimination
- reliability
- item-rest correlation
- capability mapping
- completion vs. mastery vs. adoption

### Phase 5

**Content Governance Agent**

- metadata validation
- source / owner validation
- review date
- version
- accessibility checks
- lifecycle recommendation
- human approval boundary

### Phase 6

**Product Operations Dashboard**

- roadmap
- backlog
- architecture decisions
- technical debt
- vendor dependencies
- SLOs
- product health
- adoption KPI trends

---

## 30. Engineering Principles Demonstrated

This project is intended to demonstrate the following engineering/product behaviors:

- model the business problem before choosing the tool
- separate capability from content
- use APIs as explicit contracts
- design for observable integrations
- distinguish outputs from outcomes
- maintain clear governance ownership
- use reusable assets instead of unnecessary duplication
- make system boundaries visible
- state MVP limitations clearly
- distinguish reference architecture from production architecture
- design a path toward security, scale, AI, and analytics rather than bolting them on later

---

## 31. Ownership and Review

**Project owner:** John Curry

This is a personal portfolio/reference implementation.

Recommended review cadence during active development:

- update README when architecture changes
- update `ARCHITECTURE.md` when system boundaries change
- update `DEMO_WALKTHROUGH.md` when interview flow changes
- update tests when behavior changes
- keep synthetic seed data aligned with demonstrated use cases

---

## 32. Disclaimer

This project is an independent technical portfolio demonstration.

It is not affiliated with, endorsed by, sponsored by, or an internal product of Jazz Pharmaceuticals or any other pharmaceutical company.

All names, roles, metrics, learning content, capability scores, operational events, and system interactions are synthetic.

No confidential employer, partner, student, patient, clinical, customer, or proprietary data is included.

---

## 33. Final Design Principle

> **Completion is an output. Capability and adoption are outcomes.**

That principle is the conceptual center of the Global Learning Capability Hub and the reason the architecture is organized around roles, capability, evidence, adoption, governance, and enterprise integration rather than around a course catalog alone.
