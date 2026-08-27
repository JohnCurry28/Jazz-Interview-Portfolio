# Jazz Interview Portfolio

A portfolio of working enterprise learning-technology reference implementations designed to demonstrate technical leadership across **learning architecture, AI/RAG, APIs, integrations, analytics, assessment intelligence, content governance, capability development, and product operations**.

> **Important:** This repository uses synthetic data and generic biopharma/commercial scenarios. It is an independent portfolio project and is **not affiliated with, sponsored by, endorsed by, or an internal system of Jazz Pharmaceuticals**. No proprietary, confidential, patient, employee, customer, partner, or regulated company data is included.

---

## 1. Portfolio Purpose

This repository demonstrates how a senior learning-technology / technical L&D leader can treat enterprise learning as a connected product ecosystem rather than a collection of isolated courses.

The portfolio makes the technical questions underneath modern enterprise L&D inspectable through working code:

- How should roles map to capabilities, learning, evidence, and adoption?
- How should an LMS interact with HRIS, CRM, enterprise data, content repositories, and AI services?
- How should systems of record be separated from integration mechanisms?
- How should APIs and events be governed as contracts?
- How should retries, duplicates, schema changes, failures, and dead letters be handled?
- How should enterprise AI be grounded, authorized, evaluated, and monitored?
- How should learning effectiveness be measured beyond completion?
- How should psychometric evidence connect to capability and operational adoption without overstating causality?
- How should content be owned, versioned, reviewed, made accessible, reused, approved, monitored, and retired?
- Where should automated intelligence stop and accountable human governance begin?
- How should the overall learning-technology capability be operated as a product?

The goal is not to reproduce any company's internal platform. The goal is to make architecture, engineering, product, data, analytics, AI, reliability, and governance thinking visible.

---

## 2. Enterprise Learning Capability OS

The six projects are designed to converge into one coherent reference architecture.

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
│   ├── Content Ownership
│   ├── Source Authority
│   ├── Versioning
│   ├── Review / Approval
│   ├── Accessibility
│   ├── Duplicate / Reuse Intelligence
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

## 3. Current Portfolio Status

| # | Demo | Status | Primary Technical Story |
|---|---|---|---|
| 01 | Global Learning Capability Hub | **Implemented MVP** | Role → capability → learning → evidence → adoption |
| 02 | Enterprise AI Performance Coach / RAG | **Implemented MVP** | Authorized retrieval, grounding, refusal, citations, auditability |
| 03 | LMS ↔ CRM ↔ Enterprise Data Integration Lab | **Implemented MVP** | Contracts, system-of-record boundaries, idempotency, retries, DLQ, lineage |
| 04 | Enterprise Assessment Intelligence | **Implemented MVP** | Psychometrics → mastery → adoption → business insight |
| 05 | Enterprise Content Governance Agent | **Implemented MVP** | Ownership, source, accessibility, review, duplicates, lifecycle, human authority |
| 06 | Product Operations Dashboard | **Planned** | Roadmap, backlog, technical debt, dependencies, SLOs, platform health |

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
- governance metadata
- API-backed UI
- integration-event monitoring
- automated API tests

Core model:

```text
Role → Capability → Learning → Evidence → Adoption
```

Documentation: `01-global-learning-capability-hub/README.md`

---

## 5. Demo 02 — Enterprise AI Performance Coach / RAG

A working enterprise performance-support reference implementation demonstrating:

- role-aware knowledge access
- authorization before retrieval
- approved-source grounding
- citations and relevance evidence
- unsupported-answer refusal
- prompt-injection blocking
- sensitive-data request blocking
- `ANSWERED` / `REFUSED` / `BLOCKED` states
- audit logging
- evaluation strategy
- deterministic interview behavior without external credentials

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

## 6. Demo 03 — LMS ↔ CRM ↔ Enterprise Data Integration Lab

A working FastAPI integration reference implementation demonstrating:

- explicit system-of-record boundaries
- HRIS provisioning
- LMS assignment/completion events
- capability updates
- CRM adoption events
- enterprise-data refresh
- versioned event envelopes
- contract validation
- schema-version rejection
- idempotency and duplicate suppression
- correlation IDs
- bounded retries
- transient failure recovery
- permanent failure handling
- dead-letter queue
- delivery-attempt history
- event lineage
- automated failure-path tests

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

## 7. Demo 04 — Enterprise Assessment Intelligence

A working assessment-to-capability analytics reference implementation demonstrating:

- deterministic synthetic employee data
- role cohorts
- capability-mapped assessment items
- item difficulty
- upper/lower discrimination
- item-rest correlation
- KR-20 reliability
- transparent item-review rules
- capability mastery
- role cohort comparison
- transfer-gap detection
- CRM/workflow adoption signals
- downstream business-outcome signals
- descriptive correlations
- system-of-record lineage
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

The demo deliberately contains a statistically problematic synthetic item so the analytics engine has meaningful evidence to flag rather than presenting an unrealistically perfect assessment.

Documentation:

- `04-assessment-intelligence/README.md`
- `04-assessment-intelligence/ARCHITECTURE.md`
- `04-assessment-intelligence/METRICS.md`
- `04-assessment-intelligence/DEMO_WALKTHROUGH.md`

---

## 8. Demo 05 — Enterprise Content Governance Agent

A working content-governance reference implementation demonstrating:

- governed content inventory
- accountable ownership validation
- approved source-authority validation
- review-date controls
- accessibility readiness checks
- version metadata and version snapshots
- deterministic duplicate/reuse similarity
- governance score and risk classification
- review queue
- lifecycle recommendation
- human approval boundary
- publication gate
- audit trail
- interactive scenario dashboard
- automated regression tests

Core governance model:

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

The key architectural boundary is explicit:

> **The agent may inspect, flag, score, and recommend. It cannot create organizational authority for itself.**

This module also creates an important dependency for Demo 02: in a production ecosystem, only approved/governed content should become eligible for enterprise RAG retrieval.

Documentation:

- `05-content-governance-agent/README.md`
- `05-content-governance-agent/ARCHITECTURE.md`
- `05-content-governance-agent/GOVERNANCE_CONTROLS.md`
- `05-content-governance-agent/DEMO_WALKTHROUGH.md`

---

## 9. Demo 06 — Product Operations Dashboard

**Status:** Planned

Target capabilities:

- product roadmap
- prioritized backlog
- architecture decision records
- technical debt
- vendor dependencies
- release health
- incident/risk tracking
- integration health
- SLOs / service health
- adoption KPIs
- governance backlog
- platform-health indicators

This final module is intended to make the operating model visible: enterprise learning technology is managed as a product, not merely delivered as projects.

---

## 10. How the Demos Connect

The projects are intentionally not six unrelated proof-of-concepts.

```text
01 Capability Hub
      │
      ├───────────────┐
      ▼               ▼
02 AI Coach       04 Assessment Intelligence
      ▲               │
      │               ▼
05 Content        Capability / Transfer Signals
Governance            │
      │               │
      └───────┬───────┘
              ▼
03 Integration Layer
              │
              ▼
06 Product Operations
```

Examples of cross-demo relationships:

- Demo 05 determines which content is eligible for Demo 02 retrieval.
- Demo 03 transports governed completion, capability, adoption, and governance events.
- Demo 04 turns assessment evidence into capability and transfer signals.
- Demo 01 presents those signals through learner/manager capability experiences.
- Demo 06 will expose roadmap, operational health, governance backlog, dependencies, and technical debt across the ecosystem.

---

## 11. Technical Themes Demonstrated

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
- psychometric evidence
- capability mastery
- operational learning data
- CRM adoption signals
- business-outcome signals
- cross-system analytical boundaries

### AI / RAG

- retrieval grounding
- approved-source boundaries
- role-aware authorization
- refusal behavior
- citations
- prompt-injection testing
- provider abstraction
- auditability
- evaluation design

### Content governance

- ownership
- source authority
- review cadence
- accessibility readiness
- versioning
- duplicate/reuse detection
- lifecycle management
- human approval boundaries
- audit history

### Product operations

- roadmaps
- backlogs
- technical debt
- dependencies
- SLOs
- platform health
- measurable adoption

---

## 12. Engineering Principles

### Model the business problem before choosing the platform
Technology should follow capability and workflow requirements rather than forcing every problem into one system.

### Completion is not the final outcome
Learning completion is useful operational data, but capability, adoption, performance, and business outcomes require additional evidence.

### Assessment is evidence, not truth
Item statistics and scores support decisions but do not replace validity evidence, SME judgment, governance, or operational observation.

### Systems should have explicit boundaries
HRIS, LMS, capability, CRM, content, analytics, governance, and AI services should not be treated as one undifferentiated platform.

### Integration does not redefine ownership
The integration layer transports governed facts. It does not become the authoritative source for identity, learning, mastery, adoption, content, or business outcomes.

### APIs and events are contracts
Enterprise integration requires ownership, schemas, compatibility, observability, retries, idempotency, and security—not only connectivity.

### Failure must be visible
Retries, dead letters, correlation, and operator workflows are architectural requirements, not afterthoughts.

### Authorization exists outside the model
AI instructions are not an access-control mechanism. Restricted content is filtered before retrieval and model context construction.

### Refusal is valid product behavior
If approved evidence is insufficient, the AI system should abstain rather than generate a plausible unsupported answer.

### AI recommendation is not organizational authority
Governed approval, publication, and retirement remain accountable business decisions.

### Correlation is not causation
Cross-system analytics can reveal useful patterns without justifying causal claims the evidence does not support.

### Reference architecture is not production architecture
Each project documents what is simplified in the MVP and what would need to change for secure, scalable enterprise deployment.

---

## 13. Synthetic Data Policy

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

Generic role names, content, metrics, dates, and commercial-learning scenarios are used only to make the architecture understandable.

---

## 14. Security and Production Boundaries

The demos are not presented as production-ready pharmaceutical systems.

Production deployments may require:

- SSO/OIDC
- OAuth 2.x
- RBAC/ABAC
- API gateway
- service identity
- encryption in transit and at rest
- secrets management
- centralized observability
- threat modeling
- CI/CD quality gates
- privacy and retention controls
- validated content-governance workflows
- immutable approval/audit evidence
- incident response
- environment separation
- managed databases
- backup/recovery
- formal data contracts
- schema compatibility controls
- legal/compliance/privacy/security review

Each demo README documents its specific production-hardening path.

---

## 15. Testing and Evaluation Standard

Every implemented module includes tests appropriate to its architecture.

For deterministic applications this includes:

- endpoint tests
- validation tests
- boundary tests
- data-flow tests
- failure-path tests
- integration-contract tests
- duplicate/idempotency tests
- psychometric calculations
- governance-control tests
- authorization/authority boundary tests

For AI/RAG applications this additionally includes:

- retrieval relevance
- authorization boundaries
- groundedness
- citation accuracy
- unsupported-answer refusal
- prompt-injection resistance
- sensitive-data handling
- conflict handling
- knowledge freshness
- continuous regression evaluation

The goal is to demonstrate that testing and evaluation are part of engineering, not a demo afterthought.

---

## 16. README Documentation Standard

Each implemented demo follows the same detailed, production-style documentation standard used for the NASDAQ Agent V2 project.

README coverage includes:

1. executive summary
2. business/capability problem
3. project thesis
4. current status
5. supported/prohibited use
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
25. interview walkthrough
26. architecture-defense questions
27. roadmap
28. ownership/review
29. disclaimer

The intention is for a hiring manager or technical reviewer to understand the architecture without requiring a live explanation from the author.

---

## 17. Running the Implemented Demos

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
05-content-governance-agent
```

For each demo:

- App: `http://127.0.0.1:8000`
- Swagger: `http://127.0.0.1:8000/docs`
- Tests: `pytest -q`

Use each demo's README for full setup, architecture, testing, troubleshooting, evaluation, and interview guidance.

---

## 18. Portfolio Development Path

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

The codebase is intentionally evolving toward an integrated architecture rather than a collection of disconnected demos.

---

## 19. Interview Positioning

The portfolio supports one central technical-lead message:

> **Modern enterprise L&D is not simply a collection of courses inside an LMS. It is a governed product ecosystem connecting role requirements, capability, learning, evidence, content, adoption, enterprise systems, data, reliability, analytics, governance, and increasingly AI.**

The code exists to make that thinking inspectable.

---

## 20. Project Owner

**John Curry**

Personal technical portfolio / interview reference implementation.

---

## 21. Disclaimer

This repository is an independent portfolio project.

It is not affiliated with, endorsed by, sponsored by, or an internal product of Jazz Pharmaceuticals or any other pharmaceutical company.

All names, roles, metrics, content, capability scores, events, assessments, governance decisions, and system interactions used in the demos are synthetic.
