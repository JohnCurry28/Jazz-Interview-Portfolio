# Interview Demo Walkthrough

## 30-second setup

> I built this as a small reference implementation of how I think about enterprise L&D as a product rather than a course repository. The central model is Role → Capability → Learning → Evidence → Adoption. The data is fully synthetic; what I want to demonstrate is the architecture and product thinking.

## 1. Overview — 45 seconds

Show the product KPIs and capability flow.

Key point:

> Course completion is useful operational data, but it is not the outcome. I want to know whether the person developed the required capability and whether that capability is showing up in adoption or performance signals.

## 2. Learner Experience — 60 seconds

Change between personas.

Explain:

- role determines required capabilities
- capabilities have target levels
- mastery is supported by evidence
- learning interventions are mapped to capabilities
- the path changes by role and current state

Key point:

> I would not want every learner pushed through the same catalog. The architecture should know why the learner is receiving an intervention.

## 3. Manager Readiness — 45 seconds

Show the team view sorted by adoption risk.

Key point:

> This is where completion and adoption can diverge. If onboarding is high but CRM adoption is low, the correct intervention may be coaching, workflow redesign, or system support—not automatically another course.

## 4. Governance — 45 seconds

Show versions, owners, review dates, reusable status, in-review items, and retirement candidates.

Key point:

> At enterprise scale, content needs a lifecycle. I want assets to be reusable, versioned, owned, reviewable, and tied to a capability rather than copied into dozens of disconnected courses.

## 5. Integration Health — 60 seconds

Show the event log and system strip.

Key point:

> The LMS should not be an island. Identity can originate in HRIS, learning activity can originate in an LMS, adoption signals can come from CRM, and analytics can live in the enterprise data platform. The integration layer gives us traceability across that ecosystem.

Point out correlation IDs and the warning event.

> I included a warning deliberately because enterprise integration isn't just about the happy path. You need observability, retry logic, idempotency, and clear ownership when data does not move as expected.

## 6. API Explorer — 60 seconds

Open `/docs`.

Demonstrate:

- `GET /api/users/{id}/capabilities`
- `GET /api/dashboard/manager`
- `POST /api/learning/completions`

Key point:

> The UI is backed by actual endpoints. In production I would put these behind enterprise identity, an API gateway, formal data contracts, security controls, and observability.

## Strong closing statement

> I don't see this exact application as a prescription for another company's stack. I built it to demonstrate how I approach the problem: define the capability model, separate the architectural layers, integrate systems through governed interfaces, measure outcomes beyond completion, and make the platform observable and evolvable.

## If asked “Why did you build it?”

> The role description made it clear that the technical lead needs to translate capability goals into architecture and executable technical work. I wanted to demonstrate how I think rather than only describe it.
