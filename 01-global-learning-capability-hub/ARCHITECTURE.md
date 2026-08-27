# Architecture Notes

## Product thesis

The hub is deliberately modeled around **capability** rather than a course catalog.

```text
Role
  ↓
Capability requirement
  ↓
Learning intervention
  ↓
Evidence of proficiency
  ↓
Observed adoption / behavior
  ↓
Manager + product insight
```

This supports a technical discussion about why enterprise L&D systems should connect learning data to operational systems rather than treating course completion as the final outcome.

## Logical layers

### 1. Experience layer
Learner, manager, product owner, and platform-administration experiences.

### 2. Capability layer
Roles, required capabilities, target levels, user mastery, and evidence.

### 3. Learning layer
Courses, simulations, workshops, microlearning, job aids, assignments, and scores.

### 4. Governance layer
Version, owner, review date, lifecycle state, and asset reuse.

### 5. Integration layer
API and event boundaries between HRIS/identity, LMS, CRM, content systems, enterprise data, and analytics.

### 6. Analytics layer
Onboarding, mastery, adoption, risk, product health, and later assessment intelligence.

### 7. AI layer (planned)
Role-aware RAG, coaching, source grounding, evaluation, refusal behavior, and auditability.

## Why SQLite in the demo

SQLite keeps the reference implementation portable and makes the data model inspectable during an interview. It is **not** the proposed production database.

For production, move to a managed relational platform such as PostgreSQL and introduce migrations, backup/restore, high availability, formal data retention, and environment separation.

## Integration approach

The MVP exposes synchronous REST APIs and records synthetic integration events. A production design would normally combine:

- REST/GraphQL APIs for request/response workflows
- event-driven integration for learning completion, capability change, CRM adoption, and content lifecycle events
- idempotency keys
- correlation IDs
- retry policies
- dead-letter handling
- schema contracts/versioning
- observability and alerting

## Identity and authorization

The demo has no authentication because all data is synthetic. Production should use enterprise SSO/OIDC plus RBAC/ABAC so learner, manager, L&D admin, vendor, and technical operations permissions are explicitly separated.

## Security and compliance conversation

Do not claim this demo implements pharmaceutical compliance. Instead explain that the reference architecture deliberately creates governance and audit boundaries that would be configured with the organization's security, privacy, regulatory, legal, quality, and business owners.
