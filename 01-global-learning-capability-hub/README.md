# Global Learning Capability Hub

A synthetic, interview-ready reference implementation for an enterprise learning capability product.

> **Purpose:** Demonstrate how a technical L&D leader can connect role-based learning, capability mastery, adoption, platform governance, APIs, and enterprise data in one coherent product architecture.

This project is intentionally **not branded for any employer** and contains only synthetic users, synthetic learning content, and synthetic operational data.

## Why this exists

Traditional learning demos often stop at course completion. This demo intentionally goes further:

**Role → Capability → Learning → Evidence → Adoption → Business Insight**

It is designed to support a technical-lead conversation about:

- enterprise LMS/LXP architecture
- scalable onboarding and role-based curricula
- capability and competency data models
- learning analytics and adoption measures
- reusable/versioned learning assets
- governance and content lifecycle
- API-based integration patterns
- product-oriented L&D operating models
- separation of experience, capability, integration, data, and governance concerns
- future AI/RAG/coaching extensions

## Current MVP capabilities

### Executive / product overview
Shows high-level product signals including onboarding, mastery, adoption, reusable assets, and integration health.

### Learner experience
A user selects a synthetic persona and sees:

- role and manager context
- onboarding progress
- role-required capabilities
- target proficiency levels
- current mastery
- evidence counts
- recommended/assigned/completed learning
- assessment scores and due dates

### Manager readiness view
Compares employees using:

- onboarding progress
- evidence-based mastery
- adoption
- an intervention-risk signal

This intentionally illustrates the difference between **training completion** and **behavior/adoption**.

### Governance view
Treats learning content as governed product assets with:

- version
- lifecycle status
- owner
- last review date
- reusability
- capability mapping

### Integration operations
Shows a synthetic event trail across enterprise systems such as:

- HRIS / Identity
- Learning Hub
- LMS / content systems
- CRM
- enterprise data platform
- analytics

Correlation IDs illustrate how events could be traced across systems.

### API explorer
FastAPI automatically exposes Swagger documentation at:

`/docs`

This allows the demo to move from polished UI into a live technical discussion of endpoints and payloads.

## Architecture

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

## Data model

Core entities:

- `roles`
- `users`
- `capabilities`
- `role_capabilities`
- `user_capabilities`
- `learning_assets`
- `learning_assignments`
- `integration_events`

The critical modeling decision is that **learning assets are not the center of the model**. Roles and capabilities are. Learning assets are one intervention used to build capability.

## API endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/health` | Application health check |
| GET | `/api/roles` | Role catalog |
| GET | `/api/users` | Synthetic users and headline metrics |
| GET | `/api/users/{id}` | Persona context |
| GET | `/api/users/{id}/capabilities` | Role-required capability mastery |
| GET | `/api/users/{id}/learning-path` | Personalized learning path |
| GET | `/api/dashboard/overview` | Product KPI summary |
| GET | `/api/dashboard/manager` | Team readiness/adoption view |
| GET | `/api/governance/assets` | Governed learning assets |
| GET | `/api/integrations/events` | Integration event log |
| POST | `/api/learning/completions` | Record a completion and create evidence/event data |

## Run locally

### 1. Create a virtual environment

```bash
python -m venv .venv
```

### 2. Activate it

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

macOS/Linux:

```bash
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the app

```bash
uvicorn app.main:app --reload
```

Open:

- App: `http://127.0.0.1:8000`
- Swagger/API explorer: `http://127.0.0.1:8000/docs`

## Run tests

```bash
pytest -q
```

## Interview walkthrough

A strong 4–6 minute demo sequence is:

1. **Start at Overview.** Explain that the product is organized around capability and adoption, not course inventory.
2. **Open Learner Experience.** Change personas and show that roles drive capability requirements and learning paths.
3. **Open Manager Readiness.** Point out a learner with reasonable onboarding completion but weak adoption. Explain why completion alone is an insufficient KPI.
4. **Open Governance.** Show versioning, ownership, reusable assets, review lifecycle, and retirement candidates.
5. **Open Integration Health.** Explain how learning, CRM, HRIS, and enterprise data can communicate through APIs/events rather than point-to-point manual processes.
6. **Open `/docs`.** Demonstrate that the interface is backed by actual APIs and discuss how you would secure and scale them in production.

## What to say about production hardening

This is a reference implementation, not a production pharmaceutical platform. In an enterprise deployment I would add:

- SSO / OIDC and enterprise identity
- role-based authorization
- managed relational database
- API gateway
- secrets management
- encryption in transit and at rest
- audit logging and centralized observability
- structured event bus / message queue
- retries, dead-letter handling, idempotency, and schema versioning
- security review and threat modeling
- privacy / retention controls
- regulated-content workflows defined with legal/compliance stakeholders
- automated testing and CI/CD
- infrastructure as code
- monitoring / SLOs / incident response
- formal data contracts with CRM, LMS, HRIS, analytics, and content systems

## Planned evolution

This repository is intentionally structured so later interview demos can become product modules rather than unrelated projects:

1. **AI Performance Coach** — grounded RAG, citations, role-aware retrieval, unsupported-answer refusal, evaluation.
2. **LMS ↔ CRM ↔ Enterprise Data Integration Lab** — richer event schemas, webhooks, retries, mapping, lineage.
3. **Assessment Intelligence** — difficulty, discrimination, reliability, item-rest correlation, capability mapping.
4. **Content Governance Agent** — lifecycle checks, metadata, accessibility, version, source/approval validation.
5. **Tech Lead Product Dashboard** — roadmap, backlog, technical debt, dependencies, product health, adoption KPIs.

## Design principle

> Completion is an output. Capability and adoption are outcomes.

That principle is the conceptual center of the demo.
