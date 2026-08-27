# Jazz Interview Portfolio

A portfolio of working enterprise learning-technology reference implementations designed to demonstrate technical leadership across **learning architecture, AI, RAG, APIs, integrations, analytics, governance, capability development, and product operations**.

> **Important:** This repository uses synthetic data and generic biopharma/commercial scenarios. It is an independent portfolio project and is **not affiliated with, sponsored by, endorsed by, or an internal system of Jazz Pharmaceuticals**. No proprietary, confidential, patient, employee, customer, partner, or regulated company data is included.

---

## 1. Portfolio Purpose

This repository demonstrates how a senior learning-technology / technical L&D leader can treat enterprise learning as a connected product ecosystem rather than a collection of isolated courses.

The portfolio makes several technical questions inspectable through working code:

- How should roles map to capabilities, learning, evidence, and adoption?
- How should the LMS interact with HRIS, CRM, enterprise-data, and AI services?
- How should systems of record be separated from integration mechanisms?
- How should APIs and events be governed as contracts?
- How should retries, duplicates, schema changes, failures, and dead letters be handled?
- How should enterprise AI be grounded, authorized, evaluated, and monitored?
- How should learning effectiveness be measured beyond completion?
- How should content be versioned, governed, reviewed, reused, and retired?
- How should a learning-technology capability be operated as a product?

The goal is not to reproduce any company's internal platform. The goal is to make architecture, engineering, product, data, AI, and governance thinking visible.

---

## 2. Portfolio Architecture

The six projects are designed to converge into one **Enterprise Learning Capability OS**.

```text
ENTERPRISE LEARNING CAPABILITY OS
│
├── Experience
│   ├── Learner
│   ├── Manager
│   ├── Product Owner
│   └── Platform / Admin
│
├── Capability
│   ├── Roles
│   ├── Target Capabilities
│   ├── Mastery
│   └── Evidence
│
├── Learning
│   ├── Courses
│   ├── Simulations
│   ├── Microlearning
│   └── Performance Support
│
├── Intelligence
│   ├── Assessment Analytics
│   ├── Adoption Analytics
│   ├── AI Performance Coach
│   └── RAG / Evaluation
│
├── Integration
│   ├── HRIS / Identity
│   ├── LMS / LXP
│   ├── CRM
│   ├── Capability Service
│   └── Enterprise Data / BI
│
├── Governance
│   ├── Content Lifecycle
│   ├── Versioning
│   ├── Review / Approval
│   ├── Accessibility
│   └── AI Governance
│
└── Product Operations
    ├── Roadmap
    ├── Backlog
    ├── Technical Debt
    ├── Dependencies
    ├── SLOs
    └── Platform Health
```

---

## 3. Portfolio Roadmap

### 01 — Global Learning Capability Hub

**Status:** Implemented MVP

A working FastAPI application demonstrating:

- role-based capability pathways
- onboarding progress
- capability mastery
- evidence counts
- adoption analytics
- manager readiness
- reusable learning assets
- learning-asset governance
- lifecycle/version metadata
- API-backed UI
- integration-event monitoring
- synthetic enterprise learning data
- automated API tests

Core model:

```text
Role → Capability → Learning → Evidence → Adoption
```

Documentation: `01-global-learning-capability-hub/README.md`

---

### 02 — Enterprise AI Performance Coach / RAG

**Status:** Implemented MVP

A working enterprise performance-support reference implementation demonstrating:

- role-aware knowledge access
- authorization before retrieval
- approved-source grounding
- versioned citations
- transparent retrieval relevance
- evidence threshold
- unsupported-answer refusal
- prompt-injection blocking
- sensitive-data request blocking
- `ANSWERED` / `REFUSED` / `BLOCKED` response states
- deterministic grounded synthesis
- provider-independent AI boundary
- audit logging
- human-escalation concepts
- AI evaluation strategy
- automated safety and behavior regression tests

Core control flow:

```text
User / Role
    ↓
Guardrails
    ↓
Authorized Knowledge
    ↓
Retrieval
    ↓
Evidence Threshold
    ├── insufficient → REFUSE
    └── sufficient
            ↓
      Grounded Synthesis
            ↓
   Citations + Next Action
            ↓
         Audit Event
```

Documentation:

- `02-ai-performance-coach/README.md`
- `02-ai-performance-coach/ARCHITECTURE.md`
- `02-ai-performance-coach/EVALUATION.md`
- `02-ai-performance-coach/DEMO_WALKTHROUGH.md`

---

### 03 — LMS ↔ CRM ↔ Enterprise Data Integration Lab

**Status:** Implemented MVP

A working FastAPI integration reference implementation demonstrating:

- explicit system-of-record boundaries
- HRIS provisioning and role ownership
- LMS assignment and completion events
- capability-update events
- CRM adoption events
- enterprise-data refresh flow
- versioned event envelopes
- contract validation
- schema-version rejection
- explicit event routing
- idempotency keys and duplicate suppression
- correlation IDs
- bounded retry behavior
- transient failure recovery
- permanent failure handling
- dead-letter queue
- delivery attempt history
- event lineage
- monitoring dashboard
- Swagger/OpenAPI contracts
- automated failure-path and integration tests

Core reliability model:

```text
Producer
   ↓
Contract Validation
   ↓
Idempotency Check
   ↓
Event Routing
   ↓
Delivery Attempt
   ├── success → PROCESSED
   └── failure → bounded retry
                    ├── recovery → PROCESSED
                    └── exhausted → DEAD_LETTERED
```

System ownership model:

```text
HRIS           → identity + role
LMS            → assignment + completion
Capability     → mastery
CRM            → operational adoption
Data Platform  → cross-system analytics
```

Documentation:

- `03-lms-crm-data-integration/README.md`
- `03-lms-crm-data-integration/ARCHITECTURE.md`
- `03-lms-crm-data-integration/EVENT_CATALOG.md`
- `03-lms-crm-data-integration/DEMO_WALKTHROUGH.md`

---

### 04 — Assessment Intelligence

**Status:** Planned adaptation of existing assessment-analytics work

Target capabilities:

- item difficulty
- discrimination
- reliability
- item-rest correlation
- capability mapping
- mastery signals
- cohort comparison
- completion vs. mastery vs. adoption analysis
- actionable item and curriculum recommendations

---

### 05 — Content Governance Agent

**Status:** Planned

Target capabilities:

- metadata validation
- ownership validation
- source validation
- version check
- review-date check
- accessibility review support
- lifecycle-state recommendation
- duplicate/reuse detection
- retirement candidate identification
- human approval boundary
- audit history

---

### 06 — Product Operations Dashboard

**Status:** Planned

Target capabilities:

- product roadmap
- backlog
- architecture decisions
- technical debt
- vendor dependencies
- release status
- incident/risk tracking
- integration health
- SLOs
- adoption KPIs
- platform-health indicators

---

## 4. Current Repository Structure

```text
Jazz-Interview-Portfolio/
│
├── README.md
├── .gitignore
│
├── 01-global-learning-capability-hub/
│   ├── app/
│   ├── tests/
│   ├── ARCHITECTURE.md
│   ├── DEMO_WALKTHROUGH.md
│   ├── README.md
│   ├── pyproject.toml
│   └── requirements.txt
│
├── 02-ai-performance-coach/
│   ├── app/
│   ├── data/knowledge/
│   ├── tests/
│   ├── ARCHITECTURE.md
│   ├── DEMO_WALKTHROUGH.md
│   ├── EVALUATION.md
│   ├── README.md
│   ├── pyproject.toml
│   └── requirements.txt
│
└── 03-lms-crm-data-integration/
    ├── app/
    │   ├── __init__.py
    │   ├── contracts.py
    │   ├── db.py
    │   ├── main.py
    │   ├── models.py
    │   ├── processor.py
    │   ├── scenarios.py
    │   └── static/index.html
    ├── tests/test_api.py
    ├── ARCHITECTURE.md
    ├── DEMO_WALKTHROUGH.md
    ├── EVENT_CATALOG.md
    ├── README.md
    ├── pyproject.toml
    └── requirements.txt
```

---

## 5. Technical Themes Demonstrated

### Enterprise learning architecture

- LMS/LXP boundaries
- capability models
- role-based learning
- reusable content architecture
- learning-data flows
- adoption and performance signals
- product-oriented platform thinking

### APIs and integrations

- REST APIs
- domain events
- system-of-record decisions
- contract validation
- schema versioning
- correlation IDs
- retries
- idempotency
- dead-letter handling
- data lineage
- production broker evolution

### Data architecture

- relational modeling
- role/capability relationships
- operational learning data
- CRM adoption signals
- event persistence
- delivery-attempt history
- analytical data boundaries

### AI / RAG

- retrieval grounding
- approved-source boundaries
- role-aware authorization
- provider abstraction
- refusal behavior
- citations
- prompt-injection testing
- auditability
- evaluation design

### Governance

- content versioning
- lifecycle management
- ownership
- review dates
- accessibility
- enterprise AI governance
- integration contract governance

### Product operations

- roadmaps
- backlogs
- technical debt
- dependencies
- SLOs
- platform health
- measurable adoption

---

## 6. Engineering Principles

### Model the business problem before choosing the platform

Technology should follow the capability and workflow requirements rather than forcing every problem into one system.

### Completion is not the final outcome

Learning completion is useful operational data, but capability, adoption, performance, and business outcomes require additional evidence.

### Systems should have explicit boundaries

HRIS, LMS, capability, CRM, content, analytics, and AI services should not be treated as one undifferentiated platform.

### Integration does not redefine ownership

The integration layer transports governed facts. It does not become the authoritative source for identity, learning, mastery, or CRM adoption.

### APIs and events are contracts

Enterprise integration requires ownership, schemas, compatibility, observability, retries, idempotency, and security—not only connectivity.

### Failure must be visible

Retries, dead letters, correlation, and operator workflows are architectural requirements, not afterthoughts.

### Authorization exists outside the model

AI instructions are not an access-control mechanism. Restricted content is filtered before retrieval and model context construction.

### Refusal is valid product behavior

If approved evidence is insufficient, the AI system should abstain rather than generate a plausible unsupported answer.

### Reference architecture is not production architecture

Each project documents what is simplified in the MVP and what would need to change for secure, scalable enterprise deployment.

---

## 7. Synthetic Data Policy

All demonstrations use synthetic information.

The repository intentionally excludes:

- real employee data
- patient data
- customer data
- clinical data
- proprietary commercial data
- internal company documents
- confidential employer materials
- credentials
- production API keys
- private endpoints

Generic role names and commercial-learning scenarios are used only to make the architecture understandable.

---

## 8. Security and Production Boundaries

The demos are not presented as production-ready pharmaceutical systems.

Production deployments may require:

- SSO/OIDC
- OAuth 2.x
- RBAC/ABAC
- API gateway
- service-to-service identity
- encryption in transit and at rest
- secrets management
- centralized observability
- threat modeling
- CI/CD quality gates
- privacy and retention controls
- validated content-governance workflows
- incident response
- environment separation
- managed databases
- backup/recovery
- formal data contracts
- schema compatibility controls
- legal/compliance/privacy/security review

Each demo README documents its specific production-hardening path.

---

## 9. Testing and Evaluation Standard

Every implemented module includes tests appropriate to its architecture.

For deterministic applications:

- endpoint tests
- validation tests
- boundary tests
- data-flow tests
- failure-path tests
- integration-contract tests
- duplicate/idempotency tests where relevant

For AI/RAG applications:

- retrieval relevance
- authorization-boundary tests
- groundedness
- citation accuracy
- unsupported-answer refusal accuracy
- prompt-injection resistance
- sensitive-data handling
- conflict handling
- knowledge freshness
- continuous regression evaluation

The goal is to demonstrate that testing and evaluation are part of engineering, not a demo afterthought.

---

## 10. README Documentation Standard

Each implemented demo follows the same detailed, production-style documentation standard used for the NASDAQ Agent V2 project.

README coverage should include:

1. executive summary
2. business/capability problem
3. project thesis
4. current status
5. supported and prohibited use
6. implemented features
7. architecture
8. runtime/data flow
9. repository structure
10. technology stack
11. data model
12. API/event/tool contracts
13. setup
14. environment/configuration
15. run instructions
16. reset/seed behavior
17. tests
18. evaluation strategy
19. security/privacy
20. observability
21. production hardening
22. accessibility where relevant
23. known limitations
24. troubleshooting
25. interview demo walkthrough
26. architecture-defense questions
27. roadmap
28. ownership/review
29. disclaimer

The intention is for the repository to be understandable to a hiring manager or technical reviewer without requiring a live explanation from the author.

---

## 11. Running the Implemented Demos

### Demo 01

```bash
cd 01-global-learning-capability-hub
python -m venv .venv
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### Demo 02

```bash
cd 02-ai-performance-coach
python -m venv .venv
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### Demo 03

```bash
cd 03-lms-crm-data-integration
python -m venv .venv
pip install -r requirements.txt
uvicorn app.main:app --reload
```

For each demo:

- App: `http://127.0.0.1:8000`
- Swagger: `http://127.0.0.1:8000/docs`
- Tests: `pytest -q`

Use each demo's README for complete setup, architecture, API, testing, troubleshooting, and interview guidance.

---

## 12. Portfolio Development Approach

The modules are being added incrementally rather than built as disconnected proof-of-concepts.

```text
Capability Hub
     ↓
AI Performance Coach
     ↓
Enterprise Integration Layer
     ↓
Assessment Intelligence
     ↓
Content Governance Agent
     ↓
Product Operations Dashboard
     ↓
Integrated Enterprise Learning Capability OS
```

This lets later demos reuse concepts such as:

- user identity
- roles
- capabilities
- learning assets
- evidence
- adoption
- integration events
- governance metadata
- analytics
- AI evaluation

---

## 13. Interview Positioning

The portfolio supports one central technical-lead message:

> Modern enterprise L&D is not simply a collection of courses inside an LMS. It is a product ecosystem connecting role requirements, capability, learning, evidence, adoption, enterprise systems, data, governance, reliability, and increasingly AI.

The code exists to make that thinking inspectable.

---

## 14. Project Owner

**John Curry**

Personal technical portfolio / interview reference implementation.

---

## 15. Disclaimer

This repository is an independent portfolio project.

It is not affiliated with, endorsed by, sponsored by, or an internal product of Jazz Pharmaceuticals or any other pharmaceutical company.

All names, roles, metrics, content, capability scores, events, and system interactions used in the demos are synthetic.
