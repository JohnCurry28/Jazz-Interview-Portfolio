# Architecture — Enterprise AI Performance Coach

## Design goal

Provide role-aware, grounded performance support while keeping authorization, retrieval policy, refusal logic, and auditability outside the generative model.

## Logical architecture

```text
Client / UI
   │
   ▼
FastAPI
   │
   ├── request validation
   ├── user + role context
   ▼
Guardrail layer
   │
   ├── injection detection
   ├── sensitive-data boundary
   └── future policy checks
   ▼
Knowledge authorization
   │
   └── remove non-entitled content before retrieval
   ▼
Retriever
   │
   ├── lexical weighting (MVP)
   ├── phrase boost
   └── top-k evidence
   ▼
Grounding decision
   │
   ├── below threshold → refuse
   └── sufficient → synthesize
   ▼
Provider boundary
   │
   └── deterministic grounded synthesizer (MVP)
   ▼
Response contract
   │
   ├── answer
   ├── citations
   ├── confidence heuristic
   ├── next actions
   └── guardrail telemetry
   ▼
Audit persistence
```

## Key architecture decisions

### Authorization before retrieval
Unauthorized knowledge is filtered before it can be scored or inserted into model context.

### Provider is replaceable
The MVP does not make the LLM provider the center of the architecture. Retrieval, policy, citations, refusal logic, and audit contracts survive a provider change.

### Explicit abstention state
`refused` is distinct from `blocked`. A knowledge gap is operationally different from a security/safety violation.

### Source version in response
Traceability requires knowing which version of approved knowledge supported the response.

### Audit every decision
Answered, refused, and blocked requests all become measurable product signals.

## Production target architecture

```text
Enterprise SSO / IdP
        │
        ▼
API Gateway / WAF
        │
        ▼
Coach Orchestrator
        │
 ┌──────┼───────────────┐
 │      │               │
 ▼      ▼               ▼
Policy  Query          Safety
Engine  Rewriter       Classifier
 │      │               │
 └──────┼───────────────┘
        ▼
Authorized Hybrid Retrieval
        │
 ┌──────┼──────────────┐
 ▼      ▼              ▼
Vector  Keyword       Structured tools
DB      Search        (CRM/LMS/etc.)
        │
        ▼
Reranker / Evidence Pack
        │
        ▼
Approved Model Gateway
        │
        ▼
Structured Output Validator
        │
        ▼
Claim / Citation Verification
        │
        ▼
Response + Human Escalation
        │
        ├── Audit / SIEM
        ├── RAG telemetry
        └── Product analytics
```

## Failure modes to design for

- retrieval misses the correct source
- stale content remains indexed
- user role is incorrect or overprivileged
- prompt injection in user input
- prompt injection inside retrieved documents
- fabricated claim despite correct retrieval
- incorrect citation association
- low-confidence question answered instead of refused
- excessive refusal for valid questions
- model/provider outage
- audit pipeline failure
- sensitive information entered into prompt

## Scaling considerations

For larger environments:

- asynchronous content ingestion
- document chunking service
- metadata-aware vector index
- distributed cache
- model gateway with provider failover
- policy decision point / policy enforcement point separation
- centralized observability
- regional deployment where required
- queue-based audit/analytics events

## Tradeoffs

### Simple lexical retrieval vs vector retrieval
The MVP favors transparency and zero infrastructure. Production may favor hybrid retrieval for semantic recall.

### Local SQLite vs centralized event platform
SQLite is ideal for a portable demo. Production needs durable centralized storage, access control, retention, and monitoring.

### Rule-based guardrails vs classifiers
Rules are inspectable but narrow. Production should layer classifiers and policy checks rather than replacing deterministic controls entirely.
