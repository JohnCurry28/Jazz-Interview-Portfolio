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
- How can assessment evidence be connected to capability and operational adoption without overstating causality?
- How should content be versioned, governed, reviewed, reused, and retired?
- How should a learning-technology capability be operated as a product?

The goal is not to reproduce any company's internal platform. The goal is to make architecture, engineering, product, data, AI, analytics, and governance thinking visible.

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

A working FastAPI application demonstrating role-based capability pathways, onboarding progress, capability mastery, evidence counts, adoption analytics, manager readiness, reusable learning assets, governance, API-backed UI, integration-event monitoring, and automated tests.

Core model:

```text
Role → Capability → Learning → Evidence → Adoption
```

Documentation: `01-global-learning-capability-hub/README.md`

---

### 02 — Enterprise AI Performance Coach / RAG

**Status:** Implemented MVP

A working enterprise performance-support reference implementation demonstrating role-aware knowledge access, authorization before retrieval, approved-source grounding, citations, evidence thresholds, refusal, prompt-injection blocking, sensitive-data blocking, audit logging, AI evaluation, and regression tests.

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

A working FastAPI integration reference implementation demonstrating explicit system-of-record boundaries, HRIS provisioning, LMS assignment/completion events, capability updates, CRM adoption events, enterprise-data refresh, versioned event envelopes, contract validation, schema rejection, idempotency, correlation IDs, retries, transient recovery, permanent failure handling, dead-letter queues, delivery history, event lineage, and automated integration tests.

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

Documentation:

- `03-lms-crm-data-integration/README.md`
- `03-lms-crm-data-integration/ARCHITECTURE.md`
- `03-lms-crm-data-integration/EVENT_CATALOG.md`
- `03-lms-crm-data-integration/DEMO_WALKTHROUGH.md`

---

### 04 — Enterprise Assessment Intelligence

**Status:** Implemented MVP

A working assessment-to-capability analytics reference implementation demonstrating:

- deterministic synthetic learner data
- 96 synthetic employees
- four role cohorts
- four enterprise capabilities
- 12 capability-mapped assessment items
- item difficulty
- upper/lower 27% discrimination
- item-rest correlation
- KR-20 reliability
- transparent item-review rules
- capability mastery
- role cohort comparison
- high-completion transfer-gap detection
- CRM/workflow adoption signals
- downstream business-outcome signals
- descriptive correlations
- system-of-record lineage
- FastAPI/Swagger endpoints
- interactive dashboard
- automated regression tests

Core evidence model:

```text
Completion
    ↓
Assessment Evidence
    ↓
Capability Mastery
    ↓
Operational Adoption
    ↓
Business Insight
```

The demo deliberately contains a flawed item (`Q09`) so the psychometric engine has real evidence to flag rather than presenting an unrealistically perfect synthetic assessment.

Documentation:

- `04-assessment-intelligence/README.md`
- `04-assessment-intelligence/ARCHITECTURE.md`
- `04-assessment-intelligence/METRICS.md`
- `04-assessment-intelligence/DEMO_WALKTHROUGH.md`

---

### 05 — Content Governance Agent

**Status:** Planned

Target capabilities include metadata validation, ownership validation, source validation, version/review-date checks, accessibility review support, lifecycle-state recommendation, duplicate/reuse detection, retirement candidates, human approval boundaries, and audit history.

---

### 06 — Product Operations Dashboard

**Status:** Planned

Target capabilities include product roadmap, backlog, architecture decisions, technical debt, vendor dependencies, release status, incident/risk tracking, integration health, SLOs, adoption KPIs, and platform-health indicators.

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
├── 03-lms-crm-data-integration/
│   ├── app/
│   ├── tests/
│   ├── ARCHITECTURE.md
│   ├── DEMO_WALKTHROUGH.md
│   ├── EVENT_CATALOG.md
│   ├── README.md
│   ├── pyproject.toml
│   └── requirements.txt
│
└── 04-assessment-intelligence/
    ├── app/
    │   ├── __init__.py
    │   ├── analytics.py
    │   ├── data.py
    │   ├── main.py
    │   └── static/index.html
    ├── tests/test_api.py
    ├── ARCHITECTURE.md
    ├── DEMO_WALKTHROUGH.md
    ├── METRICS.md
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

### Data and analytics architecture

- relational/domain modeling
- role/capability relationships
- psychometric evidence
- operational learning data
- CRM adoption signals
- business-outcome signals
- event persistence
- cross-system analytical boundaries

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
- integration-contract governance
- assessment-review governance

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
Technology should follow capability and workflow requirements rather than forcing every problem into one system.

### Completion is not the final outcome
Learning completion is useful operational data, but capability, adoption, performance, and business outcomes require additional evidence.

### Assessment is evidence, not truth
Item statistics and scores support decisions but do not replace validity evidence, SME judgment, governance, or operational observation.

### Systems should have explicit boundaries
HRIS, LMS, capability, CRM, content, analytics, and AI services should not be treated as one undifferentiated platform.

### Integration does not redefine ownership
The integration layer transports governed facts. It does not become the authoritative source for identity, learning, mastery, adoption, or business outcomes.

### APIs and events are contracts
Enterprise integration requires ownership, schemas, compatibility, observability, retries, idempotency, and security—not only connectivity.

### Failure must be visible
Retries, dead letters, correlation, and operator workflows are architectural requirements, not afterthoughts.

### Authorization exists outside the model
AI instructions are not an access-control mechanism. Restricted content is filtered before retrieval and model context construction.

### Refusal is valid product behavior
If approved evidence is insufficient, the AI system should abstain rather than generate a plausible unsupported answer.

### Correlation is not causation
Cross-system analytics can reveal useful patterns without justifying causal claims the evidence does not support.

### Reference architecture is not production architecture
Each project documents what is simplified in the MVP and what would need to change for secure, scalable enterprise deployment.

---

## 7. Synthetic Data Policy

All demonstrations use synthetic information. The repository intentionally excludes real employee data, patient data, customer data, clinical data, proprietary commercial data, confidential employer materials, credentials, production API keys, and private endpoints.

Generic role names and commercial-learning scenarios are used only to make the architecture understandable.

---

## 8. Security and Production Boundaries

The demos are not presented as production-ready pharmaceutical systems.

Production deployments may require SSO/OIDC, OAuth, RBAC/ABAC, API gateway, service identity, encryption, secrets management, centralized observability, threat modeling, CI/CD gates, privacy/retention controls, incident response, environment separation, managed databases, backup/recovery, formal data contracts, schema compatibility controls, assessment governance, and legal/compliance/privacy/security review.

Each demo README documents its specific production-hardening path.

---

## 9. Testing and Evaluation Standard

Every implemented module includes tests appropriate to its architecture.

For deterministic applications this includes endpoint, validation, boundary, data-flow, failure-path, integration-contract, duplicate/idempotency, psychometric, and lineage tests where applicable.

For AI/RAG applications this additionally includes retrieval relevance, authorization boundaries, groundedness, citation accuracy, unsupported-answer refusal, prompt-injection resistance, sensitive-data handling, conflict handling, knowledge freshness, and continuous regression evaluation.

The goal is to demonstrate that testing and evaluation are part of engineering, not a demo afterthought.

---

## 10. README Documentation Standard

Each implemented demo follows the same detailed, production-style documentation standard used for the NASDAQ Agent V2 project.

README coverage includes executive summary, business/capability problem, thesis, status, supported/prohibited use, features, architecture, data flow, repository structure, technology stack, data model, API/event contracts, setup, configuration, run instructions, tests, evaluation strategy, security/privacy, observability, production hardening, accessibility, known limitations, troubleshooting, interview walkthrough, architecture-defense questions, roadmap, ownership, and disclaimer.

---

## 11. Running the Implemented Demos

Each implemented project follows the same basic pattern:

```bash
cd <demo-folder>
python -m venv .venv
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Implemented folders:

```text
01-global-learning-capability-hub
02-ai-performance-coach
03-lms-crm-data-integration
04-assessment-intelligence
```

For each demo:

- App: `http://127.0.0.1:8000`
- Swagger: `http://127.0.0.1:8000/docs`
- Tests: `pytest -q`

Use each demo's README for complete setup, architecture, testing, troubleshooting, and interview guidance.

---

## 12. Portfolio Development Approach

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

Later demos reuse concepts such as identity, roles, capabilities, learning assets, evidence, adoption, integration events, governance metadata, analytics, and AI evaluation.

---

## 13. Interview Positioning

The portfolio supports one central technical-lead message:

> Modern enterprise L&D is not simply a collection of courses inside an LMS. It is a product ecosystem connecting role requirements, capability, learning, evidence, adoption, enterprise systems, data, governance, reliability, analytics, and increasingly AI.

The code exists to make that thinking inspectable.

---

## 14. Project Owner

**John Curry**

Personal technical portfolio / interview reference implementation.

---

## 15. Disclaimer

This repository is an independent portfolio project.

It is not affiliated with, endorsed by, sponsored by, or an internal product of Jazz Pharmaceuticals or any other pharmaceutical company.

All names, roles, metrics, content, capability scores, events, assessments, and system interactions used in the demos are synthetic.
