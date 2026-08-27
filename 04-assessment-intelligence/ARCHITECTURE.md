# Architecture — Enterprise Assessment Intelligence

## Product boundary

The service is an analytics layer, not a replacement system of record.

```text
LMS -------------------- completion + assessment evidence
  \
   \
    > Capability Analytics Service ---- derived mastery
   /
CRM -------------------- operational adoption
   \
    > Enterprise Data / BI ------------ downstream outcomes
```

## Logical layers

### Experience layer
Dashboard and API consumers.

### Psychometric layer
Difficulty, upper/lower discrimination, item-rest correlation, KR-20, and rule-based item review status.

### Capability layer
Item-to-capability mapping, capability mastery thresholds, and role/cohort rollups.

### Transfer layer
Comparison between demonstrated capability and observed operational adoption.

### Outcome layer
Aggregated downstream business signals and descriptive correlations.

### Integration layer
In production, Demo 03's event/API patterns would provide governed transport, lineage, idempotency, retry, schema versioning, and observability.

## System-of-record principle

Derived analytics do not overwrite source ownership:

- LMS owns completion/assessment state.
- CRM/workflow owns adoption.
- enterprise data owns downstream business metrics.
- capability analytics owns its derived models and evidence calculations.

## Production deployment sketch

```text
API Gateway / SSO
        │
        ▼
Assessment Intelligence API
        │
        ├── Psychometric Service
        ├── Capability Service
        ├── Cohort Service
        └── Insight Service
        │
        ▼
Managed Relational / Analytics Store
        │
        ├── LMS ingestion
        ├── CRM ingestion
        └── Enterprise Data ingestion
```

## Key architectural decisions

1. Keep psychometric logic deterministic and inspectable.
2. Keep completion, mastery, adoption, and business outcomes distinct.
3. Preserve source-system ownership.
4. Treat item flags as review evidence, not automatic decisions.
5. Treat correlations as descriptive, not causal.
6. Use synthetic data for portable interview demonstration.
