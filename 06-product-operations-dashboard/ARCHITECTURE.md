# Architecture — Enterprise Learning Product Operations Control Plane

## Architectural intent

Demo 06 is the portfolio-level control plane. The first five demos show domain capabilities; this project shows how a Senior Manager / Tech Lead would operate them as a product ecosystem.

```text
01 Capability Hub ───────────────┐
02 AI Performance Coach ────────┤
03 Integration Layer ───────────┤
04 Assessment Intelligence ─────┤──> Product Operations Control Plane
05 Content Governance ──────────┘        │
                                          ├── outcomes
                                          ├── health/SLOs
                                          ├── incidents
                                          ├── risks
                                          ├── roadmap/backlog
                                          ├── technical debt
                                          ├── dependencies
                                          └── architecture decisions
```

## Layers

1. **Product telemetry layer** — product health, availability, adoption, open risks/incidents.
2. **Outcome layer** — completion, mastery, adoption, governance readiness, AI grounding, integration delivery success.
3. **Reliability layer** — SLOs, error budgets, latency, incidents.
4. **Planning layer** — roadmap, backlog, release confidence.
5. **Risk layer** — cross-product risks and critical dependencies.
6. **Architecture layer** — ADRs and technical debt.
7. **Executive synthesis layer** — deterministic operating insights from explicit thresholds.

## System-of-record model

The control plane does not become the operational system of record for the underlying domains. In production it would aggregate governed telemetry from the systems that already own it.

| Domain | Authoritative owner |
|---|---|
| Identity / role | HRIS / IAM |
| Learning assignment/completion | LMS/LXP |
| Capability mastery | Capability/analytics service |
| Operational adoption | CRM/workflow systems |
| Business outcome | Enterprise Data / BI |
| Content governance state | Content governance service/repository |
| AI quality/evaluation | AI platform/evaluation service |
| Integration delivery | Integration platform |
| Roadmap/backlog | Product work-management platform |
| Incidents/SLOs | Observability/incident platforms |

## Production evolution

The MVP aggregates deterministic in-memory/synthetic state for interview portability. Production would replace this with adapters to platforms such as Jira/Azure DevOps, ServiceNow/PagerDuty, Datadog/Splunk/Grafana, cloud event platforms, LMS/LXP APIs, CRM, data warehouse/BI, model evaluation stores, and content-governance systems.

The key design principle remains: **aggregate authoritative facts; do not silently redefine ownership.**
