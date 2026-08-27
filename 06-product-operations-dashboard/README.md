# Enterprise Learning Product Operations Control Plane

A working, synthetic executive/Tech Lead control plane for operating an enterprise learning-technology portfolio across **product outcomes, roadmap, backlog, architecture, technical debt, dependencies, reliability, SLOs, incidents, risks, AI quality, content governance, assessment signals, and adoption**.

> **Portfolio purpose:** Demonstrate how a Senior Manager / Learning & Development Technical Lead can operate learning technology as a product ecosystem rather than a collection of disconnected platforms and projects.

> **Data boundary:** All product names, health states, metrics, incidents, dependencies, roadmap items, risks, and operating signals are synthetic. This project is not affiliated with, sponsored by, endorsed by, or an internal system of Jazz Pharmaceuticals or any other employer.

---

## 1. Executive Summary

The first five portfolio demos answer domain questions:

1. How do roles connect to capability, learning, evidence, and adoption?
2. How can enterprise AI provide grounded, role-aware performance support?
3. How should LMS, CRM, HRIS, capability, and data systems integrate reliably?
4. How should assessment evidence connect to mastery, adoption, and business signals?
5. How should enterprise content be governed across ownership, source, review, accessibility, versioning, reuse, and approval?

Demo 06 answers the portfolio question:

> **How would a technical leader operate all of those capabilities as one product ecosystem?**

The control plane makes visible cross-product outcome signals, product health, service-level objectives, error budgets, latency, incidents, risks, vendor/internal dependencies, roadmap commitments, execution backlog, technical debt, architecture decisions, and synthetic executive recommendations.

The core operating model is:

```text
Outcomes + Reliability + Risk + Roadmap + Architecture
                         ↓
                Product Decisions
                         ↓
          Priorities + Ownership + Action
```

---

## 2. Project Thesis

Enterprise learning technology should be operated like a product portfolio, not as a queue of course requests or platform tickets.

A technical lead should be able to answer what outcomes are improving, which products are healthy, which SLOs are at risk, which incidents or dependencies threaten delivery, which P1 items are aging, which technical debt is becoming dangerous, which architecture decisions constrain future work, which roadmap commitments are at risk, whether weak business adoption is really a learning problem, whether AI quality is degrading, and whether content-governance debt is reducing knowledge trust.

---

## 3. Current Status

**Implemented MVP**

The repository contains a runnable FastAPI application, interactive control-plane dashboard, synthetic operating data, four scenario simulations, Swagger/OpenAPI documentation, regression tests, and production-style technical documentation.

---

## 4. Relationship to Demos 01–05

```text
01 Capability Hub
       │
02 AI Performance Coach
       │
03 Integration Layer
       │
04 Assessment Intelligence
       │
05 Content Governance
       │
       ▼
06 Product Operations Control Plane
```

Demo 06 does not replace the first five. It summarizes the product, operational, and architecture signals a leader would need to prioritize work across them.

---

## 5. Product Portfolio Modeled

| Product | Primary capability |
|---|---|
| Global Learning Capability Hub | Role, capability, learning, evidence, adoption |
| Enterprise AI Performance Coach | Governed RAG/performance support |
| LMS ↔ CRM ↔ Enterprise Data Integration | Event-driven system integration |
| Enterprise Assessment Intelligence | Psychometrics, mastery, transfer, adoption |
| Enterprise Content Governance Agent | Content lifecycle and human governance |
| Product Operations Control Plane | Portfolio operations and technical leadership |

---

## 6. Implemented Control-Plane Views

- Executive
- Product Health
- Roadmap & Backlog
- Reliability & SLOs
- Risk & Dependencies
- Architecture & Technical Debt

---

## 7. Executive Outcome Chain

The control plane intentionally displays different signals separately:

```text
Learning Completion
       ↓
Capability Mastery
       ↓
Operational Adoption
       ↓
Business / Product Insight
```

It also displays governed-content readiness, AI grounded-answer rate, integration delivery success, and portfolio availability.

---

## 8. Why Completion and Adoption Are Separate

High completion does not prove that users changed behavior or that a workflow supports the intended capability. The baseline synthetic data deliberately shows a material gap between completion and adoption so the product leader must ask whether the next intervention should be additional learning, manager reinforcement, workflow redesign, system usability improvement, role clarification, performance support, or incentive/process change.

---

## 9. Product Health Model

Each synthetic product includes product owner, health state (`GREEN`, `AMBER`, `RED`), adoption signal, SLO target, availability, open risks, open incidents, and current release. The health state is an operating signal, not a substitute for the underlying evidence.

---

## 10. Portfolio Health Score

The MVP computes a transparent composite score from red/amber product count, at-risk SLO count, unhealthy critical dependencies, high-severity risks, and P1 backlog concentration.

The score is **synthetic and demonstrative**, not a validated corporate KPI. Its purpose is to show how a control plane can synthesize underlying signals while still exposing the components that created the score.

---

## 11. Service-Level Objectives

The control plane models service name, target availability, actual availability, remaining error budget, latency, and operating status for the Capability API, AI Coach API, Integration Processor, Assessment API, and Governance API.

---

## 12. Error Budget Concept

An error budget converts an availability SLO into a product-management mechanism. When reliability consumes too much of the budget, discretionary feature delivery should be reconsidered until service health stabilizes. This allows reliability work to compete explicitly for capacity.

---

## 13. Incident Model

Synthetic incidents have incident ID, severity, affected product, state, summary, start timestamp, and MTTR field. The baseline has no active incident. Scenarios introduce specific failures.

---

## 14. Risk Model

Risks contain product, severity, risk statement, mitigation, and owner. Risks are visible separately from incidents because a known future exposure is not the same as an active service-impacting event.

---

## 15. Dependency Model

Dependencies include internal vs. vendor type, products affected, criticality, health, and owner. Examples include Enterprise Identity, LMS/LXP, CRM, Enterprise Data Platform, LLM Provider, and Content Repository.

---

## 16. Why Dependency Health Matters

A learning platform can be healthy while a critical dependency is not. A technical lead therefore needs to understand the end-to-end product, not only the component their team directly owns. The release-risk scenario demonstrates this explicitly.

---

## 17. Roadmap Model

Roadmap entries include quarter, initiative, affected product, status, intended outcome, and confidence. The roadmap is framed around **outcomes**, not only features.

---

## 18. Backlog Model

Backlog items include ID, title, product, priority, status, owner, and age in days. Aging P1 items are surfaced as an operating concern.

---

## 19. Roadmap vs. Backlog

The roadmap answers what outcome the product is trying to achieve and when. The backlog answers what executable work and constraints sit underneath that outcome. The two are related but should not be treated as the same artifact.

---

## 20. Technical Debt Model

Technical debt entries include ID, area, product, severity, debt statement, remediation, and status.

Current synthetic debt includes SQLite → managed PostgreSQL, synthetic identity → OIDC/RBAC/ABAC, in-process messaging → production event broker, lexical retrieval → vector/semantic retrieval and reranking, and accessibility readiness → deeper automated/manual conformance workflow.

---

## 21. Why Technical Debt Is Visible

Technical debt creates reliability risk, security risk, delivery friction, scalability limits, future migration cost, and reduced product velocity. Therefore it belongs in the product operating model.

---

## 22. Architecture Decision Records

The demo contains explicit ADR-style decisions to keep systems of record explicit, authorize before AI retrieval, separate AI recommendation from human approval, separate completion/mastery/adoption, and use deterministic services where interview portability matters.

---

## 23. Why ADRs Matter

Important architecture decisions have a longer life than individual tickets. Recording the decision and rationale prevents teams from repeatedly reopening the same trade-off without context and helps new engineers understand why the system looks the way it does.

---

## 24. Scenario Lab

The dashboard provides four interactive operating scenarios: Release Risk, Integration Outage, AI Quality Regression, and Governance Backlog. Each scenario mutates multiple related signals to demonstrate cross-product consequences.

---

## 25. Scenario — Release Risk

The Enterprise Identity dependency turns `RED`, the Capability Hub becomes `AMBER`, a SEV2 incident opens, and portfolio health falls.

Decision principle: a critical identity/security dependency can block release even if the application code itself is healthy.

---

## 26. Scenario — Integration Outage

The CRM dependency turns `RED`, the Integration Processor drops below its SLO threshold, latency rises, error budget falls, and an incident opens.

Decision principle: reliability degradation should change product priority, not simply create an operations ticket.

---

## 27. Scenario — AI Quality Regression

The grounded-answer rate drops from the baseline to 71% after a synthetic knowledge release. Recommended actions include pausing knowledge expansion, rolling back suspect content, executing regression evaluation, inspecting governance eligibility, and restoring quality before reopening.

---

## 28. Scenario — Governance Backlog

Governed-content readiness falls to 42%, the Content Governance product turns `RED`, and stale-content exposure risk increases.

```text
Governance backlog
      ↓
Content freshness risk
      ↓
RAG eligibility risk
      ↓
AI answer-quality risk
```

---

## 29. Executive Insight Engine

The MVP uses deterministic threshold rules rather than an LLM to generate operating recommendations.

Examples include a large completion/adoption gap → investigate transfer barriers; governed-content readiness below threshold → tighten eligibility and burn down review queue; grounded-answer rate below threshold → rollback/evaluate; SLO at risk → protect error budget; critical dependency unhealthy → escalate and reconsider release.

This keeps the control logic inspectable.

---

## 30. Architecture

```text
Authoritative Domain Systems
        │
        ├── LMS/LXP
        ├── CRM
        ├── Content Governance
        ├── AI Eval / RAG
        ├── Integration Platform
        ├── Assessment Analytics
        ├── Observability
        └── Work Management
                 ↓
          Aggregation Layer
                 ↓
        Product Operations API
                 ↓
          Control-Plane UI
                 ↓
      Executive / Tech Lead Decisions
```

The MVP uses synthetic adapters represented as deterministic Python data structures.

---

## 31. System-of-Record Principle

The control plane aggregates information but does not become authoritative for identity, learning completion, capability mastery, CRM adoption, business outcomes, content approval, AI evaluation evidence, incident truth, or roadmap/work-item truth. Production integrations should retain those ownership boundaries.

---

## 32. Repository Structure

```text
06-product-operations-dashboard/
├── app/
│   ├── __init__.py
│   ├── analytics.py
│   ├── data.py
│   ├── main.py
│   └── static/
│       └── index.html
├── tests/
│   └── test_api.py
├── ARCHITECTURE.md
├── OPERATING_MODEL.md
├── DEMO_WALKTHROUGH.md
├── README.md
├── pyproject.toml
└── requirements.txt
```

---

## 33. Technology Stack

- Python
- FastAPI
- Uvicorn
- Vanilla HTML/CSS/JavaScript
- Pytest
- HTTPX/TestClient

---

## 34. API Surface

| Endpoint | Purpose |
|---|---|
| `GET /health` | Service health |
| `GET /api/portfolio` | Full control-plane baseline |
| `GET /api/products` | Product health |
| `GET /api/roadmap` | Roadmap |
| `GET /api/backlog` | Execution backlog |
| `GET /api/technical-debt` | Technical debt register |
| `GET /api/dependencies` | Dependency register |
| `GET /api/architecture-decisions` | ADR register |
| `GET /api/slos` | Service SLOs |
| `GET /api/risks` | Risk register |
| `GET /api/scenarios` | Available scenarios |
| `POST /api/scenarios/{name}` | Run scenario |

---

## 35. Local Setup

```bash
python -m venv .venv
```

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install:

```bash
pip install -r requirements.txt
```

---

## 36. Run the Application

```bash
uvicorn app.main:app --reload
```

App: `http://127.0.0.1:8000`

Swagger: `http://127.0.0.1:8000/docs`

---

## 37. Run Tests

```bash
pytest -q
```

Current regression suite: **15 tests**.

---

## 38. What the Tests Cover

- health endpoint
- five-product portfolio inventory
- portfolio health score
- completion/adoption gap
- roadmap visibility
- P1 backlog visibility
- high-severity technical debt
- architecture decision presence
- release-risk dependency failure
- integration outage SLO degradation
- AI-quality regression insight
- governance-backlog insight
- invalid scenario handling
- SLO metric completeness
- dependency ownership

---

## 39. Observability Strategy

The MVP exposes synthetic operational metrics in the control plane. Production would integrate metrics, logs, distributed traces, event delivery health, SLO/error budget calculations, incident management, alerting, model-evaluation telemetry, and governance queue telemetry.

---

## 40. Security and Access Control

The MVP has no real user authentication because it contains only synthetic data. Production should include SSO/OIDC, RBAC/ABAC, least-privilege dashboards, restricted incident/security views, audit logging, secrets management, service identity, and environment separation.

Executives, product owners, engineers, vendors, and compliance/security partners should not necessarily receive identical views.

---

## 41. Privacy and Data Minimization

A production control plane should prefer aggregated operational signals over unnecessary person-level learning or employee data. Where drill-down is needed, access should be purpose-limited and governed.

---

## 42. AI Governance Boundary

The control plane does not allow a model to independently redefine AI quality or approve content. AI quality should be supported by explicit evaluation evidence such as groundedness, citation accuracy, authorization-boundary performance, refusal accuracy, retrieval relevance, knowledge freshness, and safety regression results.

---

## 43. Accessibility

The UI uses semantic HTML tables, textual labels, explicit health terms, and does not rely on color alone to convey product status. A production implementation would require formal accessibility testing across keyboard interaction, focus behavior, contrast, screen-reader announcements, responsive behavior, and data visualization alternatives.

---

## 44. Production Hardening

Production evolution would include enterprise identity and RBAC, managed persistence, adapters to Jira/Azure DevOps, incident platform integration, observability platform integration, SLO calculation service, data warehouse/BI feeds, product telemetry contracts, API gateway, secrets management, caching, background refresh jobs, alert thresholds, immutable audit logs, release/environment separation, and CI/CD quality gates.

---

## 45. Build vs. Buy

The dashboard itself could be implemented through existing enterprise platforms rather than custom software. A technical lead should decide which capabilities belong in work-management platforms, observability platforms, incident platforms, BI dashboards, architecture repositories, or custom product APIs.

The demo therefore represents a **reference operating model**, not a recommendation to rebuild Jira, ServiceNow, Datadog, or Power BI.

---

## 46. Known Limitations

- synthetic data only
- no real connectors
- no authentication
- no persistent state
- simplified health-score weighting
- simplified SLO calculations
- no real cost telemetry
- no historical trend storage
- no release pipeline integration
- no vendor contract/SLA data
- no automated prioritization optimizer

These limitations are deliberate and documented.

---

## 47. Interview Talking Points

> "I treat learning technology as a product capability, so I want outcomes, reliability, roadmap, dependencies, and technical debt visible together."

> "An error budget is a product-prioritization mechanism, not only an infrastructure metric."

> "A critical dependency can block a release even if our own code is green."

> "AI groundedness and content-governance readiness are operating metrics because degradation can directly affect employee trust and performance support."

> "Technical debt should be explicit enough to compete for roadmap capacity."

---

## 48. Architecture-Defense Questions

### Why build a custom dashboard instead of Power BI?
The demo is a reference implementation showing the operating model and data contracts. In production, BI or existing product-ops platforms may be the correct rendering layer.

### Why use a composite health score?
To demonstrate synthesis. The underlying component signals remain visible, and the README explicitly states that the score is synthetic rather than a validated KPI.

### Why are incidents and risks separate?
An incident is an active event; a risk is a future exposure. Their ownership and response differ.

### Why expose technical debt to executives?
Because debt affects reliability, speed, scalability, security, and future investment decisions.

### Why is AI quality in the same control plane as LMS/integration health?
Because AI performance support is an enterprise product capability. If users rely on it, quality degradation is operational degradation.

### Why does governance readiness affect AI?
Because RAG quality depends on authoritative, current, approved knowledge. Content governance is upstream of retrieval trust.

---

## 49. Portfolio Completion

With this module, the six-demo portfolio is complete:

```text
01 Global Learning Capability Hub
02 Enterprise AI Performance Coach
03 LMS ↔ CRM ↔ Enterprise Data Integration
04 Enterprise Assessment Intelligence
05 Enterprise Content Governance Agent
06 Enterprise Learning Product Operations Control Plane
```

Together they form one coherent reference architecture for a modern enterprise learning capability.

---

## 50. Project Owner

**John Curry**

Personal technical portfolio / interview reference implementation.

---

## 51. Disclaimer

This repository is an independent portfolio project. It is not affiliated with, endorsed by, sponsored by, or an internal product of Jazz Pharmaceuticals or any other pharmaceutical company. All product names, incidents, dependencies, metrics, roadmap items, risk statements, and operational conditions used in the demo are synthetic.
