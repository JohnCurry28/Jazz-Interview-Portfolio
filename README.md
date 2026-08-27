# Jazz Interview Portfolio

A portfolio of six working enterprise learning-technology reference implementations demonstrating technical leadership across **learning architecture, AI/RAG, APIs, integrations, assessment intelligence, analytics, content governance, reliability, data architecture, and product operations**.

> **Important:** This repository uses synthetic data and generic biopharma/commercial scenarios. It is an independent portfolio project and is **not affiliated with, sponsored by, endorsed by, or an internal system of Jazz Pharmaceuticals**. No proprietary, confidential, patient, employee, customer, partner, or regulated company data is included.

---

## 1. Portfolio Purpose

This repository demonstrates how a Senior Manager / Learning & Development Technical Lead can treat enterprise learning as a connected product ecosystem rather than a collection of isolated courses, tools, or LMS projects.

The portfolio makes the technical questions underneath modern enterprise L&D inspectable through working code:

- How should roles map to capabilities, learning, evidence, and adoption?
- How should an LMS interact with HRIS, CRM, enterprise data, content repositories, and AI services?
- How should systems of record remain explicit when multiple platforms exchange data?
- How should APIs and events be governed as versioned contracts?
- How should retries, duplicates, schema changes, failures, and dead letters be handled?
- How should enterprise AI be grounded, authorized, evaluated, and monitored?
- How should learning effectiveness be measured beyond completion?
- How should psychometric evidence connect to capability and operational adoption without overstating causality?
- How should content be owned, versioned, reviewed, made accessible, reused, approved, monitored, and retired?
- Where should automated intelligence stop and accountable human governance begin?
- How should the entire learning-technology capability be operated as a product?

The goal is not to reproduce any company's internal platform. The goal is to make **architecture, engineering, product, data, AI, analytics, reliability, and governance thinking visible**.

---

## 2. Enterprise Learning Capability OS

The six projects form one coherent reference architecture:

```text
                         ┌──────────────────────────────┐
                         │ 06 Product Operations       │
                         │ Executive / Tech Lead Plane │
                         └──────────────┬───────────────┘
                                        │
        ┌───────────────────────────────┼──────────────────────────────┐
        │                               │                              │
        ▼                               ▼                              ▼
01 Capability Hub              04 Assessment Intelligence     05 Content Governance
Role → capability              evidence → mastery             ownership → approval
→ learning → evidence          → adoption → insight           → lifecycle
        │                               │                              │
        └───────────────────────┬───────┴──────────────┬───────────────┘
                                │                      │
                                ▼                      ▼
                    03 Integration Layer      02 AI Performance Coach
                    HRIS/LMS/CRM/Data          governed enterprise RAG
                    contracts/retries/DLQ      citations/refusal/audit
```

### Operating principle

```text
Role
  ↓
Capability
  ↓
Learning
  ↓
Evidence
  ↓
Mastery
  ↓
Operational Adoption
  ↓
Business Insight
```

Supporting that chain are governed content, reliable integrations, enterprise AI, and product operations.

---

## 3. Portfolio Status — 6/6 Implemented

| # | Demo | Status | Primary Technical Story |
|---|---|---|---|
| 01 | Global Learning Capability Hub | **Implemented MVP** | Role → capability → learning → evidence → adoption |
| 02 | Enterprise AI Performance Coach / RAG | **Implemented MVP** | Authorized retrieval, grounding, refusal, citations, auditability |
| 03 | LMS ↔ CRM ↔ Enterprise Data Integration Lab | **Implemented MVP** | Contracts, system-of-record boundaries, idempotency, retries, DLQ, lineage |
| 04 | Enterprise Assessment Intelligence | **Implemented MVP** | Psychometrics → mastery → adoption → business insight |
| 05 | Enterprise Content Governance Agent | **Implemented MVP** | Ownership, source, accessibility, review, duplicates, lifecycle, human authority |
| 06 | Enterprise Learning Product Operations Control Plane | **Implemented MVP** | Roadmap, backlog, debt, dependencies, SLOs, incidents, risk, product health |

---

## 4. Demo 01 — Global Learning Capability Hub

A working FastAPI application demonstrating:

- role-based capability pathways
- onboarding progress
- capability mastery
- evidence counts
- adoption analytics
- manager readiness
- reusable learning assets
- content/version governance metadata
- API-backed UI
- synthetic enterprise integration events
- automated API tests

Core model:

```text
Role → Capability → Learning → Evidence → Adoption
```

Documentation:

- `01-global-learning-capability-hub/README.md`
- `01-global-learning-capability-hub/ARCHITECTURE.md`
- `01-global-learning-capability-hub/DEMO_WALKTHROUGH.md`

---

## 5. Demo 02 — Enterprise AI Performance Coach / RAG

A working enterprise performance-support reference implementation demonstrating:

- role-aware knowledge access
- authorization **before** retrieval
- approved-source grounding
- versioned citations
- evidence thresholds
- unsupported-answer refusal
- prompt-injection blocking
- sensitive-data request blocking
- `ANSWERED` / `REFUSED` / `BLOCKED` states
- deterministic interview behavior without external credentials
- audit logging
- evaluation strategy

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
      Grounded Response
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

## 6. Demo 03 — LMS ↔ CRM ↔ Enterprise Data Integration Lab

A working event-driven integration reference implementation demonstrating:

- explicit systems of record
- HRIS provisioning and role ownership
- LMS assignment/completion events
- capability-update events
- CRM adoption events
- enterprise-data refresh flow
- versioned event envelopes
- contract validation
- schema-version rejection
- idempotency keys and duplicate suppression
- correlation IDs
- bounded retries
- transient failure recovery
- permanent failure handling
- dead-letter queue
- delivery-attempt history
- data lineage
- failure-path regression tests

Reliability model:

```text
Producer
   ↓
Contract Validation
   ↓
Idempotency Check
   ↓
Routing
   ↓
Delivery
   ├── success → PROCESSED
   └── failure → bounded retry
                    ├── recovery → PROCESSED
                    └── exhausted → DEAD_LETTERED
```

System ownership:

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

## 7. Demo 04 — Enterprise Assessment Intelligence

A working assessment-to-capability analytics reference implementation demonstrating:

- deterministic synthetic employee data
- role cohorts
- capability-mapped items
- item difficulty
- upper/lower discrimination
- item-rest correlation
- KR-20 reliability
- transparent item-review rules
- capability mastery
- transfer-gap detection
- CRM/workflow adoption signals
- downstream business-outcome signals
- descriptive correlations
- system-of-record lineage
- automated psychometric regression tests

Evidence model:

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

A deliberately problematic synthetic assessment item is included so the analytics engine has meaningful evidence to diagnose rather than an unrealistically perfect dataset.

Documentation:

- `04-assessment-intelligence/README.md`
- `04-assessment-intelligence/ARCHITECTURE.md`
- `04-assessment-intelligence/METRICS.md`
- `04-assessment-intelligence/DEMO_WALKTHROUGH.md`

---

## 8. Demo 05 — Enterprise Content Governance Agent

A working content-governance reference implementation demonstrating:

- governed content inventory
- accountable ownership
- source-authority validation
- review-date controls
- accessibility readiness checks
- version snapshots
- duplicate/reuse similarity analysis
- governance score and risk classification
- review queue
- lifecycle recommendations
- human approval boundary
- publication gate
- audit history
- automated governance regression tests

Governance model:

```text
Create
  ↓
Automated Inspection
  ├── ownership
  ├── source authority
  ├── review date
  ├── accessibility
  ├── version
  └── duplicate / reuse
  ↓
Risk + Recommendation
  ↓
Human Governance
  ├── approve
  ├── request changes
  ├── reject
  ├── publish
  └── retire
  ↓
Monitor / Re-review
```

Core architectural boundary:

> **The agent may inspect, flag, score, and recommend. It cannot create organizational authority for itself.**

A production relationship to Demo 02 is explicit: governed/approved content determines which knowledge may become eligible for RAG retrieval.

Documentation:

- `05-content-governance-agent/README.md`
- `05-content-governance-agent/ARCHITECTURE.md`
- `05-content-governance-agent/GOVERNANCE_CONTROLS.md`
- `05-content-governance-agent/DEMO_WALKTHROUGH.md`

---

## 9. Demo 06 — Enterprise Learning Product Operations Control Plane

The final demo sits above the first five and shows how a Senior Manager / Tech Lead can operate the learning-technology capability as a product portfolio.

Implemented capabilities:

- executive outcome signals
- product health and ownership
- roadmap
- prioritized backlog
- backlog aging
- architecture decision records
- technical debt register
- vendor/internal dependencies
- service-level objectives
- error budgets
- latency
- incidents
- risk register
- AI quality signal
- governance readiness signal
- integration delivery health
- four operational scenario simulations
- deterministic executive insights
- automated regression tests

The interactive scenarios are:

1. **Release Risk** — critical identity dependency blocks release readiness.
2. **Integration Outage** — CRM delivery failure degrades the Integration Processor SLO and error budget.
3. **AI Quality Regression** — grounded-answer quality falls after a knowledge update.
4. **Governance Backlog** — content readiness falls and creates downstream RAG freshness risk.

Control-plane model:

```text
Outcomes + Reliability + Risk + Roadmap + Architecture
                         ↓
                Product Decisions
                         ↓
          Priorities + Ownership + Action
```

Documentation:

- `06-product-operations-dashboard/README.md`
- `06-product-operations-dashboard/ARCHITECTURE.md`
- `06-product-operations-dashboard/OPERATING_MODEL.md`
- `06-product-operations-dashboard/DEMO_WALKTHROUGH.md`

---

## 10. Cross-Demo Relationships

The portfolio is intentionally integrated rather than six unrelated proofs of concept.

### Governance → AI

```text
Content Repository
      ↓
05 Governance Agent
      ↓
Approved / current / authoritative?
      ├── NO → exclude
      └── YES
             ↓
       02 AI Coach RAG
```

### Learning → Assessment → Adoption

```text
01 Capability Hub
      ↓
04 Assessment Intelligence
      ↓
Capability Mastery
      ↓
03 Integration Layer
      ↓
CRM Adoption / Enterprise Data
```

### Operations across everything

```text
01 Capability
02 AI
03 Integration
04 Assessment
05 Governance
       ↓
06 Product Operations
       ↓
Roadmap / Reliability / Risk / Debt / Decisions
```

---

## 11. Key Engineering Principles

### Model the business problem before choosing the platform
Technology follows capability and workflow requirements rather than forcing every problem into one system.

### Completion is not the final outcome
Completion, mastery, adoption, and business outcomes are different evidence layers.

### Assessment is evidence, not truth
Psychometrics support decisions but do not replace validity evidence, SME review, or operational observation.

### Systems have explicit boundaries
HRIS, LMS, capability, CRM, content, analytics, governance, AI, and operations systems retain distinct responsibilities.

### Integration does not redefine ownership
The integration layer transports governed facts; it does not become the system of record.

### APIs and events are contracts
Enterprise integration requires schemas, compatibility, ownership, observability, retries, idempotency, and security.

### Failure must be visible
Retries, DLQs, incidents, error budgets, and correlation are architectural requirements.

### Authorization exists outside the model
Prompt instructions are not an access-control mechanism.

### Refusal is valid AI behavior
A system without approved evidence should abstain rather than hallucinate.

### AI recommendation is not organizational authority
Human approval and publication remain accountable business controls.

### Correlation is not causation
Cross-system analytics can reveal patterns without proving causal relationships.

### Technical debt is product work
Debt affects reliability, scalability, security, cost, and delivery velocity and should compete for roadmap capacity.

### Reliability changes priority
An exhausted error budget or critical dependency problem should affect feature sequencing.

---

## 12. Synthetic Data Policy

All demonstrations use synthetic information. The repository intentionally excludes real employee, patient, customer, clinical, proprietary, confidential, credential, production API-key, and private-endpoint data.

---

## 13. Security and Production Boundaries

These are reference implementations, not production pharmaceutical systems.

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
- privacy/retention controls
- immutable audit evidence
- environment separation
- managed databases
- backup/recovery
- formal data contracts
- schema compatibility controls
- security/privacy/legal/compliance review

Each demo README documents its specific hardening path.

---

## 14. Testing Standard

Every implemented module contains automated tests appropriate to its architecture, including combinations of:

- endpoint tests
- validation tests
- boundary tests
- data-flow tests
- failure-path tests
- idempotency tests
- integration-contract tests
- psychometric tests
- governance-control tests
- authorization-boundary tests
- AI refusal/safety behavior
- scenario regression tests

The goal is to demonstrate that testing and evaluation are part of engineering, not a demo afterthought.

---

## 15. Documentation Standard

Every demo follows the production-style documentation depth established for the NASDAQ Agent V2 project.

Individual README coverage includes architecture, repository structure, technology choices, data/contracts, setup, tests, security, observability, production hardening, known limitations, troubleshooting, interview walkthroughs, architecture-defense questions, roadmap, and disclaimers.

---

## 16. Repository Structure

```text
Jazz-Interview-Portfolio/
│
├── README.md
├── .gitignore
│
├── 01-global-learning-capability-hub/
├── 02-ai-performance-coach/
├── 03-lms-crm-data-integration/
├── 04-assessment-intelligence/
├── 05-content-governance-agent/
└── 06-product-operations-dashboard/
```

Each folder is runnable independently and includes its own technical documentation and tests.

---

## 17. Running a Demo

Typical pattern:

```bash
cd <demo-folder>
python -m venv .venv
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open:

```text
App:     http://127.0.0.1:8000
Swagger: http://127.0.0.1:8000/docs
```

Tests:

```bash
pytest -q
```

Use the README inside each demo for complete instructions.

---

## 18. Interview Positioning

The portfolio supports one central technical-lead message:

> **Modern enterprise L&D is not simply a collection of courses inside an LMS. It is a product ecosystem connecting role requirements, capability, learning, evidence, adoption, enterprise systems, data, governance, reliability, analytics, AI, and measurable business outcomes.**

The final control-plane demo adds the leadership layer:

> **A technical lead must also make roadmap, reliability, dependency, risk, architecture, and technical-debt decisions across that ecosystem.**

The code exists to make that thinking inspectable.

---

## 19. Portfolio Owner

**John Curry**

Personal technical portfolio / interview reference implementation.

---

## 20. Disclaimer

This repository is an independent portfolio project. It is not affiliated with, endorsed by, sponsored by, or an internal product of Jazz Pharmaceuticals or any other pharmaceutical company.

All names, roles, content, product metrics, capability scores, incidents, events, dependencies, roadmap items, assessments, and operating scenarios are synthetic.
