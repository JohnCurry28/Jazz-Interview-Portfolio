# Jazz Interview Portfolio

A portfolio of working enterprise learning-technology reference implementations designed to demonstrate technical leadership across **learning architecture, AI, RAG, APIs, integrations, analytics, governance, capability development, and product operations**.

> **Important:** This repository uses synthetic data and generic biopharma/commercial scenarios. It is an independent portfolio project and is **not affiliated with, sponsored by, endorsed by, or an internal system of Jazz Pharmaceuticals**. No proprietary, confidential, patient, employee, customer, partner, or regulated company data is included.

---

## 1. Portfolio Purpose

This repository was created to demonstrate how a senior learning-technology / technical L&D leader can move beyond traditional course development and think about enterprise learning as a connected product ecosystem.

The portfolio focuses on the technical questions that sit underneath modern enterprise L&D:

- How should roles map to capabilities?
- How should capabilities map to learning and evidence?
- How do we distinguish completion from demonstrated mastery?
- How do we measure adoption rather than only participation?
- How should an LMS interact with HRIS, CRM, content, and enterprise-data platforms?
- How should learning assets be versioned, governed, reused, reviewed, and retired?
- Where should AI and RAG fit into the architecture?
- How should enterprise AI be grounded, evaluated, authorized, and monitored?
- How do technical leads make build-vs-buy decisions?
- How do product roadmaps, technical debt, dependencies, SLOs, and vendor constraints become visible?

The goal is not to reproduce any company's internal platform. The goal is to make the architecture, engineering, product, and governance thinking visible through working reference implementations.

---

## 2. Portfolio Architecture

The projects are designed to become one coherent **Enterprise Learning Capability OS** rather than six unrelated demos.

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
│   ├── Capabilities
│   ├── Target Levels
│   ├── Mastery
│   └── Evidence
│
├── Learning
│   ├── Courses
│   ├── Simulations
│   ├── Workshops
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
│   ├── Content Systems
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
- onboarding
- capability mastery
- evidence counts
- adoption analytics
- manager readiness
- learning-asset governance
- versioning and lifecycle status
- API-backed UI
- integration-event monitoring
- correlation IDs
- synthetic HRIS / LMS / CRM / data interactions
- automated API tests

Core model:

```text
Role → Capability → Learning → Evidence → Adoption
```

See:

`01-global-learning-capability-hub/README.md`

for the complete technical documentation.

---

### 02 — AI Performance Coach / Enterprise RAG

**Status:** Planned

Purpose: demonstrate enterprise AI-enabled performance support using approved knowledge sources rather than an unrestricted chatbot.

Planned capabilities:

- role-aware retrieval
- approved-source RAG
- citations
- confidence / support indicators
- unsupported-answer refusal
- source filtering
- authorization-aware retrieval boundaries
- audit logging
- evaluation datasets
- hallucination testing
- prompt-injection testing
- human-escalation path

Target architecture:

```text
User
  ↓
Identity / Role Context
  ↓
API
  ↓
Orchestrator
  ├── Retrieval Tool
  ├── Learning Tool
  └── Capability Tool
        ↓
Validation / Policy Layer
        ↓
LLM
        ↓
Grounded Response
        ↓
Evaluation / Logging
```

---

### 03 — LMS ↔ CRM ↔ Enterprise Data Integration Lab

**Status:** Planned

Purpose: demonstrate integration patterns, API contracts, data movement, observability, and system-of-record boundaries.

Planned capabilities:

- HRIS provisioning event
- role change event
- learning assignment event
- completion event
- capability update event
- CRM adoption event
- analytics refresh
- idempotency
- correlation IDs
- retry logic
- dead-letter handling
- schema versioning
- contract validation
- data-lineage view

---

### 04 — Assessment Intelligence

**Status:** Planned adaptation of existing assessment-analytics work

Purpose: demonstrate how learning effectiveness can be measured beyond completion.

Planned capabilities:

- item difficulty
- discrimination
- reliability
- item-rest correlation
- capability mapping
- mastery signals
- cohort comparison
- completion vs. mastery vs. adoption analysis
- actionable item / curriculum recommendations

---

### 05 — Content Governance Agent

**Status:** Planned

Purpose: demonstrate governed content lifecycle and AI-assisted quality review.

Planned capabilities:

- metadata validation
- ownership validation
- source validation
- version check
- review-date check
- accessibility review support
- lifecycle-state recommendation
- duplicate / reuse detection
- retirement candidate identification
- human approval boundary
- audit history

---

### 06 — Product Operations Dashboard

**Status:** Planned

Purpose: demonstrate that enterprise learning technology should be managed as a product.

Planned capabilities:

- product roadmap
- backlog
- architecture decisions
- technical debt
- vendor dependencies
- release status
- incident / risk tracking
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
└── 01-global-learning-capability-hub/
    ├── app/
    │   ├── __init__.py
    │   ├── db.py
    │   ├── main.py
    │   ├── static/
    │   │   ├── app.js
    │   │   └── styles.css
    │   └── templates/
    │       └── index.html
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

Additional numbered modules will be added as they are implemented.

---

## 5. Technical Themes Demonstrated

Across the portfolio, the projects are intended to demonstrate competence in:

### Enterprise learning architecture

- LMS / LXP boundaries
- capability models
- role-based learning
- reusable content architecture
- learning-data flows
- product-oriented platform thinking

### APIs and integrations

- REST APIs
- events
- webhooks
- system-of-record decisions
- contract validation
- correlation IDs
- retries
- idempotency
- dead-letter handling
- data lineage

### Data architecture

- relational modeling
- role / capability relationships
- operational learning data
- analytics data
- CRM adoption signals
- evidence and mastery

### AI / RAG

- retrieval grounding
- tool orchestration
- role-aware context
- model evaluation
- refusal behavior
- citations
- prompt-injection testing
- auditability
- human review

### Governance

- content versioning
- lifecycle management
- ownership
- review dates
- reusable assets
- accessibility
- enterprise AI governance

### Product operations

- roadmaps
- backlogs
- technical debt
- dependencies
- SLOs
- product health
- measurable adoption

---

## 6. Engineering Principles

The portfolio follows several principles.

### Model the business problem before choosing the platform

Technology should follow the capability and workflow requirements rather than forcing every problem into one system.

### Completion is not the final outcome

Course completion is useful operational data, but capability, adoption, performance, and business outcomes require additional signals.

### Systems should have explicit boundaries

HRIS, LMS, CRM, content systems, analytics, and AI services should not be treated as one undifferentiated platform.

### APIs and events should be governed contracts

Enterprise integrations require more than “connecting systems.” They require ownership, schemas, observability, retries, versioning, and security.

### AI must operate inside enterprise controls

AI should not bypass identity, authorization, approved knowledge sources, content governance, or audit requirements.

### Reference architecture is not production architecture

Each project explicitly documents what is simplified in the MVP and what would need to change for a secure, scalable, production deployment.

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

Production deployments would require, depending on the module:

- SSO / OIDC
- OAuth 2.x
- RBAC / ABAC
- API gateway
- service-to-service authentication
- encryption in transit and at rest
- secrets management
- structured audit logging
- centralized observability
- threat modeling
- vulnerability management
- CI/CD quality gates
- privacy / retention controls
- validated content-governance workflows
- incident-response procedures
- environment separation
- managed databases
- backup / recovery
- formal data contracts
- legal / compliance / privacy / security review

The README inside each demo documents its specific production-hardening path.

---

## 9. Testing and Evaluation Standard

Every implemented module should include tests appropriate to its architecture.

For deterministic applications, this includes:

- endpoint tests
- validation tests
- boundary tests
- data-flow tests
- failure-path tests
- integration-contract tests where applicable

For AI / RAG applications, this will additionally include:

- retrieval hit rate
- recall@K
- precision@K
- filtering accuracy
- no-result behavior
- answer correctness
- faithfulness
- citation accuracy
- completeness
- conflict handling
- unsupported-answer refusal accuracy
- authorization-boundary tests
- prompt-injection resistance

The goal is to demonstrate that AI evaluation is part of engineering, not merely a demo afterthought.

---

## 10. README Documentation Standard

Each project README is intentionally detailed and production-style.

Every implemented demo should document:

1. executive summary
2. business / capability problem
3. project thesis
4. current status
5. supported and prohibited use
6. implemented features
7. architecture
8. runtime / data flow
9. repository structure
10. technology stack
11. data model
12. API or tool contracts
13. setup
14. environment variables
15. run instructions
16. reset / seed behavior
17. tests
18. evaluation strategy
19. security / privacy
20. observability
21. production hardening
22. accessibility where relevant
23. known limitations
24. troubleshooting
25. interview demo walkthrough
26. architecture-defense questions
27. roadmap
28. ownership / review
29. disclaimer

The intention is for the repository to be understandable to both a hiring manager and a technical reviewer without requiring a live explanation from the author.

---

## 11. Running the Current Demo

From the repository root:

```bash
cd 01-global-learning-capability-hub
python -m venv .venv
```

Activate the environment and install dependencies:

```bash
pip install -r requirements.txt
```

Run:

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

Tests:

```bash
pytest -q
```

For full setup, architecture, API, troubleshooting, testing, and interview guidance, use the README inside `01-global-learning-capability-hub/`.

---

## 12. Portfolio Development Approach

The remaining modules will be added incrementally rather than built as disconnected proof-of-concepts.

The intended evolution is:

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

This allows later demos to reuse shared concepts such as:

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

The portfolio is designed to support one central technical-lead message:

> Modern enterprise L&D is not simply a collection of courses inside an LMS. It is a product ecosystem connecting role requirements, capability, learning, evidence, adoption, enterprise systems, data, governance, and increasingly AI.

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
