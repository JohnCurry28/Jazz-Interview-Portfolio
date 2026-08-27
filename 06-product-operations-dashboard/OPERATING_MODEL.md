# Operating Model

## Product operating cadence

### Daily / continuous
- critical dependency health
- active incidents
- SLO/error budget consumption
- integration delivery failures
- AI evaluation regressions
- governance eligibility or stale-content risk

### Weekly
- portfolio health review
- P1 backlog aging
- technical debt movement
- roadmap confidence
- product adoption and transfer gaps
- vendor/dependency risk

### Monthly / quarterly
- capability outcomes
- product roadmap prioritization
- build-vs-buy decisions
- architecture decision review
- investment vs. technical debt balance
- SLO target review
- product value and adoption review

## Decision principles

1. **Outcomes before outputs** — shipping features is not itself the goal.
2. **Reliability consumes capacity** — an exhausted error budget should change roadmap priority.
3. **Dependencies are product risks** — a platform cannot treat an unhealthy critical dependency as somebody else's problem.
4. **Technical debt is visible work** — debt competes for capacity and should have severity, owner, and remediation.
5. **Architecture decisions are durable records** — significant trade-offs should be explicit and revisitable.
6. **Completion is not adoption** — learning metrics should not mask operational transfer problems.
7. **AI quality is an operational metric** — groundedness, refusal, authorization, and freshness need ongoing evaluation.
8. **Governance backlog is product health** — stale/unreviewed content can degrade both learner experience and AI retrieval quality.

## Scenario response model

### Release Risk
Pause release if a critical dependency is red. Escalate ownership, validate failover/rollback, and avoid shipping around unresolved identity/security boundaries.

### Integration Outage
Protect the error budget, observe retry/DLQ behavior, restore delivery, then replay safely using idempotency controls.

### AI Quality Regression
Stop knowledge expansion, rollback suspect content, execute the eval suite, inspect retrieval/citations, and re-open only after quality thresholds recover.

### Governance Backlog
Tighten eligibility, prioritize high-risk/overdue assets, escalate owners, and prevent stale content from becoming trusted AI knowledge.
