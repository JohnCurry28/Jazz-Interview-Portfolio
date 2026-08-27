# Enterprise Content Governance Agent

A working, synthetic enterprise content-governance reference implementation demonstrating how AI-assisted inspection can support metadata quality, accessibility readiness, ownership, source authority, review cadence, duplication analysis, lifecycle control, and auditability **without giving the agent authority to approve, publish, or retire content**.

> **Portfolio purpose:** Demonstrate how a technical L&D leader can design content governance as an enterprise product capability rather than as a manual spreadsheet or one-time publishing checklist.

> **Data boundary:** All content assets, owners, source authorities, dates, workflows, decisions, and audit events are synthetic. This project is not affiliated with, sponsored by, endorsed by, or an internal system of Jazz Pharmaceuticals or any other employer.

---

## 1. Executive Summary

Enterprise learning content often becomes difficult to govern because organizations focus on creation and publication but underinvest in what happens afterward:

- Who owns the asset?
- Which source is authoritative?
- When must it be reviewed again?
- Is the version current?
- Is the asset accessible?
- Does an equivalent asset already exist?
- Who approved it?
- Should it remain published?
- What changed and who made the decision?

This project models those questions through a controlled lifecycle:

```text
Create → Inspect → Review → Approve → Publish → Monitor → Re-review → Retire
```

The automated governance agent can inspect and recommend. Human reviewers remain authoritative for approval, publication, rejection, change requests, and retirement.

---

## 2. Business Problem

In a large learning ecosystem, content can be distributed across LMS courses, performance-support pages, repositories, job aids, videos, checklists, PDFs, microlearning, and regional variants.

Without explicit governance, common failure modes include:

- duplicate assets
- conflicting guidance
- outdated procedures
- orphaned content with no owner
- expired review dates
- inaccessible media
- inconsistent versions
- content published from unapproved sources
- no audit trail
- manual review queues that do not scale

The project demonstrates a technical pattern for making those risks visible and routable.

---

## 3. Project Thesis

> **AI should accelerate governance work, not replace organizational accountability.**

The system therefore separates:

```text
Automation / Recommendation
          from
Authority / Approval
```

This boundary is enforced in application logic and regression tests.

---

## 4. Current Status

**Status:** Implemented MVP

The current working demo includes:

- synthetic governed content inventory
- metadata checks
- owner validation
- source-authority validation
- review-date validation
- accessibility readiness checks
- semantic version validation
- duplicate/reuse similarity
- governance score
- risk classification
- lifecycle recommendation
- review queue
- human decision endpoint
- publication gate
- version snapshots
- audit log
- interactive dashboard
- Swagger/OpenAPI documentation
- automated regression tests

---

## 5. Supported Use

This repository is intended for:

- interview demonstrations
- architecture discussion
- technical learning
- enterprise L&D product design
- governance workflow prototyping
- API and lifecycle design discussion
- content-operations strategy

---

## 6. Prohibited / Out-of-Scope Use

The MVP should not be treated as:

- a validated regulated-content system
- a compliance certification tool
- a substitute for legal/regulatory review
- a WCAG conformance audit
- a records-management platform
- a production approval engine
- a repository for real sensitive content
- an autonomous publishing agent

---

## 7. Core Architecture

```text
Content Author / Source System
          │
          ▼
   Content Inventory
          │
          ▼
  Governance Agent
  ├── Metadata checks
  ├── Ownership checks
  ├── Source-authority checks
  ├── Review-date checks
  ├── Accessibility checks
  ├── Duplicate/reuse detection
  └── Risk / lifecycle recommendation
          │
          ▼
   Governance Record
          │
   ┌──────┴────────┐
   ▼               ▼
Human Review    Audit / Analytics
   │
   ├── APPROVE
   ├── REQUEST CHANGES
   ├── REJECT
   ├── PUBLISH
   └── RETIRE
          │
          ▼
 Content Lifecycle
```

See `ARCHITECTURE.md` for the architecture-specific reference.

---

## 8. Agent Authority Boundary

The agent is deliberately advisory.

### Agent may

- inspect metadata
- identify missing ownership
- check source status
- evaluate review dates
- evaluate accessibility metadata
- identify probable duplicates
- calculate a readiness/risk indicator
- recommend next actions
- recommend a lifecycle state
- write audit events

### Agent may not

- approve content
- publish content
- retire content
- override a reviewer
- bypass source authority
- erase audit history

The code returns this boundary explicitly in every agent recommendation.

---

## 9. Content Lifecycle

The modeled lifecycle is:

```text
DRAFT
  ↓
TECHNICAL_REVIEW
  ↓
CONTENT_OWNER_REVIEW
  ↓
APPROVED
  ↓
PUBLISHED
  ↓
MONITORED
  ↓
REVIEW_REQUIRED
  ↓
RETIRED
```

A production workflow could permit additional transitions such as local approval, translation review, legal review, emergency withdrawal, remediation, or archival states.

---

## 10. Governed Content Model

Each content item includes:

- title
- content type
- owner
- source authority
- version
- review due date
- content body
- accessibility metadata
- approved-source indicator
- lifecycle state
- timestamps

---

## 11. Ownership Control

A governed asset requires an accountable owner.

MVP behavior:

```text
owner present → PASS
owner missing → FAIL
```

Missing ownership is treated as a high-risk condition because there is no accountable party for maintenance or approval.

---

## 12. Source Authority Control

Content must be traceable to an approved source authority.

Examples in the synthetic dataset include:

- CRM Product Owner
- Campaign Governance Council
- Enterprise AI Governance
- Enterprise Data Product Owner

Unapproved or unknown sources are treated as blocking failures.

---

## 13. Review-Date Control

The MVP calculates the number of days between today and the content review due date.

```text
overdue       → FAIL
0–30 days     → WARN
>30 days      → PASS
```

The intent is to make stale-content risk operationally visible.

---

## 14. Accessibility Readiness

The MVP checks four synthetic accessibility metadata signals:

- alt text complete
- captions/transcript complete
- heading order valid
- descriptive links present

These checks are **not** a WCAG conformance audit. They represent content-readiness signals that would feed a broader accessibility QA process.

---

## 15. Version Governance

Every seeded content asset uses a semantic content version:

```text
major.minor
```

Example:

```text
2.3
```

The database also stores a version snapshot in the `versions` table for traceability.

A production repository would likely use immutable repository IDs, release versions, change summaries, approver references, and source checksums.

---

## 16. Duplicate / Reuse Intelligence

The MVP compares:

```text
title + body
```

using deterministic cosine similarity over token counts.

This is intentionally explainable and portable.

Threshold behavior:

```text
>= 0.82 → strong duplicate/reuse signal
>= 0.68 → moderate duplicate/reuse signal
< 0.68  → no material duplicate flag
```

A duplicate flag is **not** an instruction to delete content.

The human decision may be to:

- reuse an existing asset
- consolidate assets
- create a justified role/local variant
- retain both
- retire obsolete content

---

## 17. Governance Score

The demo computes a synthetic readiness score from the automated checks.

```text
base_score = mean(check scores)
```

A duplicate penalty is then applied:

```text
similarity >= .82 → -0.15
similarity >= .68 → -0.07
```

Final:

```text
score = max(0, base_score - duplicate_penalty) × 100
```

The governance score is a prioritization/readiness indicator for the demo, **not a compliance score**.

---

## 18. Risk Classification

The MVP classifies assets as LOW, MEDIUM, or HIGH risk.

### HIGH

- missing ownership
- unapproved source
- governance score below 60

### MEDIUM

- score below 82
- duplicate similarity at or above .68
- any remaining failed automated check

### LOW

- no HIGH or MEDIUM condition

---

## 19. Agent Recommendation

The agent returns:

- governance score
- risk level
- proposed lifecycle state
- reasons
- recommended actions
- human-approval indicator
- agent-boundary statement

Example conceptual response:

```json
{
  "governance_score": 83.3,
  "risk_level": "MEDIUM",
  "proposed_state": "MONITORED",
  "reasons": ["The review date is overdue."],
  "recommended_actions": ["Route to content owner review before continued use."],
  "human_approval_required": false
}
```

---

## 20. Human Governance API

Human decisions use a separate endpoint and data contract.

Supported decisions:

- `APPROVE`
- `REJECT`
- `REQUEST_CHANGES`
- `PUBLISH`
- `RETIRE`

This separation is intentional: the same service that recommends does not silently transform recommendation into organizational authority.

---

## 21. Publication Gate

For the MVP, publication is permitted only when:

```text
current lifecycle state == APPROVED
AND
risk level == LOW
```

A direct attempt to publish a draft, medium-risk, or high-risk asset is rejected.

---

## 22. Auditability

The `audit_log` records:

- actor
- item ID
- event type
- detail
- timestamp

Current event examples:

- `SEED`
- `AGENT_SCAN`
- `HUMAN_DECISION`

A production audit model would require stronger user identity, immutable evidence, change references, retention controls, and centralized logging.

---

## 23. Version History

The `versions` table stores:

- item ID
- version
- JSON snapshot
- timestamp

This allows the architecture to distinguish:

```text
current operational content record
          from
historical version evidence
```

---

## 24. Synthetic Demo Inventory

The seed data intentionally contains different governance conditions.

### Commercial CRM Workflow Guide

- current source
- published
- accessible
- strong content quality
- near-duplicate relationship with a second CRM asset

### Omnichannel Campaign Readiness Checklist

- good source/ownership
- overdue review date

### Responsible AI Use for Commercial Teams

- strong source
- incomplete accessibility readiness

### CRM Workflow Quick Reference

- valid draft
- near duplicate of an existing governed asset

### Commercial Data Literacy Reporting Guide

- fully current synthetic LOW-risk control case

### Legacy Field Enablement FAQ

- missing owner
- unapproved source
- overdue review
- structural accessibility concerns
- HIGH risk

---

## 25. Dashboard

The web UI exposes:

- portfolio-style governance summary
- content inventory
- governance score
- lifecycle state
- risk level
- review queue
- duplicate/reuse intelligence
- detailed check results
- recommended actions
- lifecycle visualization
- recent audit events

---

## 26. Interview Scenarios

The dashboard provides direct scenario buttons for:

- Overdue Review
- Accessibility Failure
- Duplicate Candidate
- High-Risk Legacy Asset

The healthy Data Literacy asset is available as the control case.

---

## 27. Technology Stack

### Backend

- Python
- FastAPI
- Pydantic
- SQLite

### Frontend

- HTML
- CSS
- vanilla JavaScript

### Testing

- pytest
- FastAPI TestClient
- httpx

No external model API or credential is required for the MVP.

---

## 28. Why No External LLM Is Required

The demo deliberately keeps core governance controls deterministic so that:

- interview behavior is reproducible
- policy logic is inspectable
- no external credential is needed
- authority is visibly outside the model
- test results are stable

A production AI provider can be introduced behind a provider boundary for non-authoritative assistance.

---

## 29. Where AI Could Be Added in Production

Potential AI-assisted features include:

- metadata extraction
- content summaries
- change summaries
- suggested taxonomy tags
- semantic duplicate explanation
- accessibility remediation suggestions
- source comparison
- stale-content risk summaries
- localization-impact analysis
- content owner review briefs

AI would remain advisory for governed decisions.

---

## 30. Repository Structure

```text
05-content-governance-agent/
│
├── app/
│   ├── __init__.py
│   ├── agent.py
│   ├── db.py
│   ├── governance.py
│   ├── main.py
│   ├── models.py
│   ├── service.py
│   └── static/
│       └── index.html
│
├── tests/
│   └── test_api.py
│
├── .gitignore
├── ARCHITECTURE.md
├── DEMO_WALKTHROUGH.md
├── GOVERNANCE_CONTROLS.md
├── README.md
├── pyproject.toml
└── requirements.txt
```

---

## 31. API Surface

### Health

```http
GET /health
```

### Dashboard

```http
GET /api/dashboard
```

### Content inventory

```http
GET /api/items
GET /api/items/{item_id}
```

### Agent scan

```http
POST /api/agent/scan
POST /api/agent/scan-all
```

Example:

```json
{
  "item_id": 3,
  "actor": "governance-agent"
}
```

### Human review

```http
POST /api/items/{item_id}/review
```

Example:

```json
{
  "reviewer": "Governance Lead",
  "action": "REQUEST_CHANGES",
  "note": "Resolve accessibility findings before approval."
}
```

### Versions

```http
GET /api/items/{item_id}/versions
```

### Audit

```http
GET /api/audit
```

### Reset

```http
POST /api/reset
```

---

## 32. Local Setup

From the demo folder:

```bash
python -m venv .venv
```

Activate the environment.

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install:

```bash
pip install -r requirements.txt
```

---

## 33. Run the Application

```bash
uvicorn app.main:app --reload
```

Open:

```text
http://127.0.0.1:8000
```

Swagger/OpenAPI:

```text
http://127.0.0.1:8000/docs
```

---

## 34. Run Tests

```bash
pytest -q
```

Current regression suite validates:

- health endpoint
- seeded inventory
- dashboard summary
- overdue-review detection
- accessibility-failure detection
- duplicate detection
- high-risk legacy content
- agent authority boundary
- blocked publication
- blocked high-risk approval
- valid human state transition
- audit event persistence
- version history

---

## 35. Current Test Result

At the time this README was prepared:

```text
13 passed
```

---

## 36. Security and Privacy

The demo contains no real employee, patient, customer, learner, or proprietary company data.

A production system would require:

- SSO/OIDC
- RBAC/ABAC
- service identity
- secrets management
- encryption
- secure API gateway
- audit protection
- privacy review
- least-privilege repository permissions
- retention policy
- incident response

---

## 37. Accessibility Boundary

This project treats accessibility as a governance dimension, but it does not claim that a boolean metadata check proves accessibility compliance.

Production accessibility governance should include:

- automated scanning
- manual QA
- keyboard testing
- screen-reader testing where appropriate
- color/contrast review
- caption/transcript validation
- document accessibility validation
- documented exceptions/remediation

---

## 38. Observability

Current observability is represented by:

- governance check persistence
- audit events
- review queue
- risk levels
- duplicate candidates

Production observability should include:

- structured logs
- metrics
- traces
- workflow latency
- review SLA aging
- error rates
- source-sync failures
- publication failures
- duplicate trends
- stale-content trends

---

## 39. Production Hardening

A production implementation would likely add:

- managed relational database
- enterprise content-repository integration
- workflow engine
- event bus
- source registry
- policy engine
- identity and authorization
- immutable audit records
- semantic/vector duplicate detection
- accessibility scanning services
- notification service
- localization governance
- environment separation
- backups and disaster recovery
- CI/CD security scanning
- approval evidence retention

---

## 40. Build vs. Buy Considerations

Many organizations already own platforms that provide portions of this workflow.

A technical lead should evaluate:

### Buy / configure when

- repository workflow is already mature
- governance rules are mostly standard
- integrations are supported
- audit capabilities are sufficient
- ownership/versioning already exist

### Build / extend when

- governance must span multiple repositories
- learning-specific metadata is unique
- duplicate/reuse intelligence is cross-platform
- custom lifecycle orchestration is required
- enterprise analytics need unified governance events

The likely production answer is often a hybrid architecture rather than replacing every existing platform.

---

## 41. Known Limitations

The MVP intentionally simplifies several areas:

- no external identity provider
- no true workflow engine
- SQLite instead of managed storage
- deterministic duplicate similarity
- no file ingestion
- no document parsing
- no LLM provider
- no semantic embeddings
- no full accessibility audit
- no localization model
- no legal/regulatory approval stages
- no notification service
- no immutable audit store

These limitations are documented rather than hidden.

---

## 42. Interview Talking Points

Strong lines for the demo include:

> **"The agent can inspect and recommend, but it cannot create organizational authority for itself."**

> **"I treat a review date as an operational control, not decorative metadata."**

> **"Duplicate detection should create a reuse decision, not an automatic deletion decision."**

> **"Accessibility is part of release readiness and governance, not a cleanup step after publication."**

> **"Content governance is a lifecycle problem: ownership, source, version, approval, monitoring, re-review, and retirement all matter."**

---

## 43. Architecture-Defense Questions

### Why separate human review from the agent?

Because organizational approval is a control and accountability function. Model confidence is not authority.

### Why use rules instead of an LLM for the MVP?

Because the important architecture decision is where authority and policy live. Deterministic rules make that boundary inspectable and testable without credentials.

### How would this integrate with an LMS/LXP?

The governance layer should sit upstream of publication. Approved content/version metadata can synchronize to delivery systems through APIs/events while authoritative source ownership remains in the governed repository.

### How would you handle regulated or market-specific content?

Add approval scopes, market metadata, source requirements, required reviewer roles, effective dates, localization status, and policy-driven lifecycle transitions.

### How would you scale duplicate detection?

Use embeddings/vector search, semantic clustering, repository metadata, and variant relationships while keeping the final reuse/consolidation decision human-controlled.

---

## 44. Relationship to the Other Portfolio Demos

### Demo 01 — Capability Hub

Governed content becomes reusable learning/performance-support assets in capability pathways.

### Demo 02 — AI Performance Coach

Only approved, governed content should be eligible for enterprise RAG retrieval.

### Demo 03 — Integration Lab

Content governance events can flow to LMS/LXP, analytics, or product-operations systems through governed contracts.

### Demo 04 — Assessment Intelligence

Content and assessment quality findings can create review work in the governance lifecycle.

### Demo 06 — Product Operations

Governance backlog, review SLA, risk, technical debt, and platform health can become product-operating metrics.

---

## 45. Roadmap

Potential next increments:

- file upload and parsing
- semantic duplicate detection
- content lineage graph
- role/market variants
- review SLA aging
- notification workflows
- automated change summaries
- WCAG scanning integration
- repository adapters
- LMS publishing adapter
- RAG eligibility flag
- policy-as-code engine
- multi-stage approval scopes
- signed approval evidence

---

## 46. Project Owner

**John Curry**

Personal technical portfolio / interview reference implementation.

---

## 47. Disclaimer

This repository is an independent portfolio project.

It is not affiliated with, endorsed by, sponsored by, or an internal product of Jazz Pharmaceuticals or any other pharmaceutical company.

All content assets, roles, owners, metrics, dates, governance decisions, and system interactions are synthetic.
