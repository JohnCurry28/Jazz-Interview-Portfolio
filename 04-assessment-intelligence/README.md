# Enterprise Assessment Intelligence

A working, synthetic assessment-to-capability analytics reference implementation that connects **learning completion, psychometric evidence, capability mastery, operational adoption, and downstream business signals** without treating any one metric as sufficient proof of performance.

> **Portfolio purpose:** Demonstrate how a technical L&D leader can evolve assessment analytics from a faculty-facing item-analysis tool into an enterprise capability intelligence product.

> **Data boundary:** All learners, items, roles, scores, adoption signals, business outcomes, and system interactions are synthetic. This project is not affiliated with, sponsored by, endorsed by, or an internal system of Jazz Pharmaceuticals or any other employer.

---

## 1. Executive Summary

Traditional learning reporting often stops at completion, participation, or mean assessment score. Those metrics are useful, but they do not answer the harder enterprise questions:

- Did the assessment provide trustworthy evidence?
- Which items functioned well or poorly?
- Which capabilities appear strong or weak?
- Did demonstrated mastery transfer into the workflow?
- Did operational adoption correlate with downstream business outcomes?
- When performance is weak, is the likely problem learning, workflow design, manager reinforcement, incentives, tooling, or something else?

This demo models those questions through the chain:

```text
Completion → Assessment Evidence → Capability Mastery → Operational Adoption → Business Insight
```

The application deliberately keeps those layers distinct rather than collapsing them into one “learning score.”

---

## 2. Relationship to the Original Assessment Intelligence Suite

This demo evolves the existing Assessment Intelligence work rather than replacing it.

The earlier suite already supported:

- Canvas Student Analysis data
- Quiz and Item Analysis data
- item difficulty
- upper/lower discrimination
- item-rest correlation
- reliability
- distractor analysis
- competency/outcome mapping
- review recommendations
- local privacy-aware analysis

The enterprise version preserves that psychometric logic while adding:

- role cohorts
- capability rollups
- transfer-gap detection
- CRM/workflow adoption signals
- downstream business-outcome signals
- system-of-record boundaries
- cross-layer correlations
- manager/product insights
- API-backed delivery

---

## 3. Project Thesis

> **Completion is an output. Assessment is evidence. Capability is an inferred state. Adoption is observed behavior. Business impact is a downstream outcome.**

No single layer should be used as a substitute for the others.

---

## 4. Current Status

**Status: Implemented MVP**

The current build includes:

- deterministic synthetic data generation
- 96 synthetic employees
- four role cohorts
- four enterprise capabilities
- 12 dichotomously scored assessment items
- psychometric item analysis
- KR-20 reliability
- capability rollups
- transfer-gap analysis
- operational adoption signals
- business-outcome signals
- correlation analysis
- role-cohort comparisons
- system-of-record lineage
- decision insights
- FastAPI endpoints
- interactive dashboard
- Swagger/OpenAPI documentation
- automated regression tests

---

## 5. Supported Use

This reference implementation is appropriate for:

- interview demonstrations
- architecture discussions
- psychometric-design discussions
- capability analytics demonstrations
- API/data-model discussions
- learning-effectiveness discussions
- product-thinking demonstrations
- synthetic experimentation

It is **not** a validated production assessment, clinical decision system, employee-performance system, or pharmaceutical compliance platform.

---

## 6. Core Architecture

```text
LMS Completion
      │
      ▼
Assessment Responses ───────► Psychometric Engine
      │                           │
      │                           ├── Difficulty
      │                           ├── Upper/Lower 27%
      │                           ├── Discrimination
      │                           ├── Item-Rest Correlation
      │                           └── KR-20
      │
      ▼
Capability Mapping
      │
      ▼
Capability Mastery
      │
      ├───────────────┐
      ▼               ▼
CRM / Workflow     Manager / Product
Adoption Signal       Insight
      │
      ▼
Enterprise Data / BI
      │
      ▼
Business Outcome Signal
```

---

## 7. Outcome Chain

The dashboard exposes five distinct evidence layers:

1. **Completion** — Was required learning completed?
2. **Assessment** — What evidence did the assessment produce?
3. **Capability Mastery** — Which capability standards appear demonstrated?
4. **Operational Adoption** — Is the expected behavior occurring in the workflow?
5. **Business Insight** — What downstream operational pattern appears alongside adoption?

These are intentionally not interchangeable.

---

## 8. Why Completion Is Insufficient

A learner may complete every required course but still:

- misunderstand the workflow
- fail to retain critical knowledge
- perform poorly on the assessment
- know what to do but not do it
- encounter a badly designed system
- lack manager reinforcement
- face competing incentives
- lack access to required tools

The demo therefore includes a **Transfer Gaps** view showing high-completion employees whose mastery or adoption remains weak.

---

## 9. Psychometric Metrics

The engine calculates four core item-quality signals.

### 9.1 Item Difficulty

For dichotomous items:

```text
p = number correct / number responding
```

A higher value means the item is easier.

### 9.2 Upper/Lower 27% Discrimination

Learners are ranked by total score. The top 27% and bottom 27% are compared:

```text
D = P(upper correct) - P(lower correct)
```

Positive values indicate stronger learners are more likely to answer correctly.

### 9.3 Item-Rest Correlation

The item score is correlated with the learner's score on the **remainder** of the assessment.

This avoids mechanically correlating an item with a total score that already contains the item itself.

### 9.4 KR-20 Reliability

For dichotomously scored items:

```text
KR20 = k/(k-1) * (1 - Σ(pq) / variance(total score))
```

Reliability is evidence about internal consistency in the observed sample. It is not proof of validity.

---

## 10. Item Status Logic

The MVP uses transparent rule-based flags.

### REVIEW

Triggered when discrimination or item-rest evidence becomes negative.

Possible causes include incorrect keying, ambiguous wording, misalignment, scoring problems, multidimensional constructs, or sampling noise.

### DIFFICULT

Used when success is below 45%. This does **not** automatically mean the item should be made easier.

### GOOD

Used when difficulty is within a practical range and both discrimination and item-rest evidence are sufficiently positive.

### MONITOR

Used for mixed or inconclusive evidence.

---

## 11. Deliberately Flawed Demo Item

`Q09` is intentionally generated so stronger learners are less likely to answer correctly.

That produces a negative item-rest signal and allows the demo to show an authentic review workflow.

The point is not to create a perfect synthetic assessment. The point is to demonstrate how the system detects questionable evidence.

---

## 12. Capability Model

The synthetic capability framework includes:

- CRM Workflow
- Omnichannel Execution
- Data Literacy
- Responsible AI Use

Each capability is supported by three mapped assessment items.

A learner is considered to demonstrate a capability in the MVP when at least two of the three mapped items are correct.

This threshold is illustrative, not a proposed enterprise standard.

---

## 13. Learner Mastery Model

For each learner:

```text
Capability score = correct items in capability / mapped items
```

A capability is counted as mastered when:

```text
Capability score >= 2/3
```

Overall capability mastery is the proportion of the four capabilities meeting that threshold.

Production standards should be defined through job analysis, SME validation, assessment design, evidence requirements, and governance.

---

## 14. Operational Adoption

The MVP includes a synthetic adoption score representing behavior observed in a CRM or workflow platform after enablement.

Examples of real-world adoption signals could include:

- required workflow completion
- data-quality compliance
- use of approved digital features
- correct process sequencing
- manager-observed behavior
- use of performance-support tools

The actual signal should be defined with business, data, privacy, compliance, and platform owners.

---

## 15. Business Outcome Signal

The demo includes a synthetic downstream operational-quality index.

It exists to show **architecture and analytics linkage**, not to claim causality.

A real implementation might connect capability/adoption to carefully governed measures such as process quality, cycle time, error reduction, readiness, customer-experience signals, productivity, or appropriate commercial KPIs.

Any causal claim would require stronger research design than simple correlation.

---

## 16. Correlation Is Not Causation

The dashboard displays:

- mastery ↔ adoption correlation
- adoption ↔ business-outcome correlation

These correlations are descriptive.

They do **not** prove that training caused adoption or that adoption caused the business outcome.

Production analysis may require pre/post designs, matched comparison groups, quasi-experimental designs, longitudinal analysis, multivariate modeling, or controlled experiments where feasible.

---

## 17. System-of-Record Boundaries

| Signal | Logical system of record | Role |
|---|---|---|
| Completion | LMS | assignment/completion state |
| Assessment response | Assessment/LMS | raw response evidence |
| Capability mastery | Capability analytics service | derived capability evidence |
| Adoption | CRM/workflow platform | observed operational behavior |
| Business outcome | Enterprise data/BI | downstream business signal |

The analytics layer links these signals but does not pretend to own the operational source data.

---

## 18. Relationship to Demo 03

Demo 03 demonstrates the integration infrastructure needed to transport these signals through event contracts, correlation IDs, idempotency, retries, dead-letter handling, schema versioning, and lineage.

Demo 04 demonstrates **what analytical value can be created once those governed signals are available**.

---

## 19. Synthetic Data Generation

The sample dataset is generated deterministically using a fixed random seed.

This provides reproducible results, no real employee data, predictable interview behavior, and stable regression tests.

The synthetic model includes variation in latent learner ability, role specialization, item difficulty, training completion, adoption, and downstream outcome.

---

## 20. Repository Structure

```text
04-assessment-intelligence/
│
├── app/
│   ├── __init__.py
│   ├── analytics.py
│   ├── data.py
│   ├── main.py
│   └── static/
│       └── index.html
│
├── tests/
│   └── test_api.py
│
├── .gitignore
├── ARCHITECTURE.md
├── DEMO_WALKTHROUGH.md
├── METRICS.md
├── README.md
├── pyproject.toml
└── requirements.txt
```

---

## 21. Technology Stack

- Python 3.10+
- FastAPI
- Uvicorn
- standard-library statistics/math
- vanilla HTML/CSS/JavaScript
- Pytest
- HTTPX / FastAPI TestClient

No external AI model or paid API is required.

---

## 22. Why No Heavy Analytics Library

The MVP implements the core formulas directly so the logic is inspectable during an interview.

Production analytics could use validated statistical libraries and a governed analytics platform, but hiding every calculation behind a package would make the educational value of the demo weaker.

---

## 23. API Surface

### `GET /health`
Service health.

### `GET /api/overview`
Top-level outcome-chain metrics and correlations.

### `GET /api/items`
Psychometric item results. Optional filter: `/api/items?status=REVIEW`.

### `GET /api/capabilities`
Capability-level assessment, mastery, adoption, and outcome rollups.

### `GET /api/cohorts`
Role-level cohort metrics.

### `GET /api/learners`
Synthetic learner-level signals. Transfer-gap filter: `/api/learners?risk_only=true`.

### `GET /api/insights`
Rule-based decision insights.

### `GET /api/metric-definitions`
Plain-language metric definitions.

### `GET /api/data-lineage`
System-of-record map.

---

## 24. Run Locally

```bash
python -m venv .venv
```

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

---

## 25. Environment Variables

No environment variables are required for the MVP.

A production implementation would likely require configuration for database connection, identity provider, API gateway, data platform, LMS integration, CRM integration, secrets manager, and telemetry.

---

## 26. Testing

Run:

```bash
pytest -q
```

The current automated suite validates health, outcome-chain metrics, item metric bounds, detection of the deliberately flawed item, capability rollups, cohort aggregation, transfer-gap logic, insight categories, metric definitions, and system-of-record lineage.

---

## 27. Current Regression Result

```text
10 passed
```

---

## 28. Privacy Model

The demo contains no real employee data.

A production implementation should minimize learner-level exposure and prefer aggregated analytics where possible.

Potential controls include pseudonymous identifiers, role-based access, minimum cohort sizes, data retention rules, privacy review, export restrictions, and audit logging.

---

## 29. Security Boundary

The MVP intentionally excludes authentication because all data is synthetic.

Production would require SSO/OIDC, RBAC/ABAC, API gateway, encryption in transit and at rest, service authentication, secrets management, audit logging, environment separation, and vulnerability management.

---

## 30. Fairness and Employee-Analytics Caution

Assessment and adoption data can affect employees if misused.

The architecture should therefore avoid turning a learning analytics dashboard into an opaque employee-ranking system.

Production governance should address intended use, prohibited use, transparency, access controls, human review, bias/fairness evaluation, contestability where decisions affect people, and minimum evidence requirements.

---

## 31. Validity Boundary

Psychometric quality is broader than reliability or item statistics.

A production assessment strategy should consider evidence for content validity, response processes, internal structure, relationships to other variables, and consequences of use.

This MVP does not claim to establish those forms of validity.

---

## 32. Observability

For production, monitor ingestion success, missing/late data, item-analysis job failures, schema drift, cohort size, metric freshness, API latency/error rate, downstream dashboard freshness, and access/audit events.

---

## 33. Data Quality Controls

Potential production checks include duplicate response detection, missing item IDs, impossible scores, mismatched assessment versions, stale capability mappings, missing role metadata, invalid adoption windows, and business-metric timestamp alignment.

---

## 34. Accessibility

The dashboard uses semantic headings, real tables, readable contrast, text labels in addition to visual emphasis, and responsive layout.

A production release would undergo formal WCAG testing, keyboard testing, screen-reader testing, and zoom/reflow validation.

---

## 35. Production Hardening

A production implementation should add:

- managed database / warehouse
- formal data contracts
- scheduled or event-driven pipelines
- immutable raw-event retention where appropriate
- transformation/version controls
- data catalog
- CI/CD
- migrations
- SSO
- authorization
- centralized logging
- metrics/tracing
- privacy controls
- validated statistical libraries
- assessment-version governance
- content-owner workflow
- model documentation
- incident response

---

## 36. Build vs. Buy

A technical lead should not assume custom software is automatically the right answer.

Potential enterprise options include native LMS analytics, assessment vendor analytics, LRS/xAPI platforms, enterprise BI, a data warehouse/lakehouse, commercial talent/capability platforms, or custom analytics services.

Custom development is justified when the required cross-system capability model, governance, or insight cannot be achieved cleanly through existing platforms.

---

## 37. Known Limitations

The MVP intentionally simplifies:

- all items are dichotomous
- no distractor UI is included in this enterprise version
- no live Canvas import is included
- capability thresholds are illustrative
- adoption signals are synthetic
- business outcomes are synthetic
- no causal inference is performed
- no authentication
- no persistent database
- no longitudinal model
- no item-response-theory model
- no differential-item-functioning analysis

---

## 38. Future Enhancements

Possible next iterations:

- Canvas dual-report import adapter
- CSV upload
- assessment-version comparison
- longitudinal cohorts
- pre/post analysis
- confidence intervals
- distractor analysis
- item exposure history
- item bank governance
- capability heatmaps
- manager drill-down
- intervention recommendation workflow
- integration with Demo 03 event stream
- AI-assisted item review with approved-data boundaries

---

## 39. Interview Demo Walkthrough

Recommended 5–7 minute sequence:

1. Open **Outcome Chain**.
2. Point out high completion but materially lower adoption.
3. Explain why that prevents “more training” from becoming the automatic answer.
4. Open **Item Intelligence**.
5. Find `Q09` and explain negative item-rest evidence.
6. Open **Capabilities** and compare mastery with adoption.
7. Open **Transfer Gaps** and show completed learners with weak downstream evidence.
8. Open **Data Lineage** and explain system-of-record ownership.
9. Open `/docs` and show the API layer.

---

## 40. Architecture Defense Questions

### Why not just use completion?
Because completion only proves a required learning event reached an operational state. It does not establish mastery or adoption.

### Why not use assessment score as the KPI?
Assessment provides evidence under test conditions. Adoption requires observation in the flow of work.

### Why calculate item-rest rather than simple item-total correlation?
Removing the item from the total reduces part-whole inflation.

### Why use KR-20?
The current sample items are dichotomously scored. For broader item types, a different reliability model may be appropriate.

### Why not claim the business metric proves training impact?
Because correlation across observational signals is not causal evidence.

### Why keep system-of-record boundaries visible?
Because analytics should integrate authoritative signals without creating ambiguous ownership.

---

## 41. Strong Interview Talking Point

> “I started with item-level psychometrics, but enterprise learning effectiveness cannot stop there. I want to know whether the assessment generated trustworthy evidence, whether that evidence maps to role capabilities, whether capability transfers into operational adoption, and whether those signals relate to business outcomes. If completion is high but adoption is low, I would investigate the workflow before prescribing another course.”

---

## 42. Ownership

**John Curry**  
Personal technical portfolio / interview reference implementation.

---

## 43. Disclaimer

This repository is an independent portfolio project.

It is not affiliated with, endorsed by, sponsored by, or an internal product of Jazz Pharmaceuticals or any other pharmaceutical company.

All employee, role, assessment, adoption, and outcome data is synthetic.
