# Interview Demo Walkthrough

## 90-second version

1. Start on the dashboard and explain that this is a synthetic cross-system integration lab, not a mocked screenshot.
2. Point to the system-of-record matrix: HRIS owns identity/role, LMS owns learning, Capability owns mastery, CRM owns adoption, Data Platform owns cross-system analytics.
3. Run **Happy Path** and open the lineage view.
4. Explain correlation IDs and governed event contracts.
5. Run **Show Idempotency** and explain why the duplicate produces no second downstream delivery.
6. Run **Show Retry Recovery** and show two failed attempts followed by success.
7. Run **Show Dead Letter** and show exhausted delivery attempts moving into the operator-visible DLQ.
8. Open Swagger to prove the UI is backed by real APIs.

## Five-minute technical version

### 1. Start with boundaries

> “I designed the demo around system ownership before integrations. HRIS remains authoritative for identity and role, the LMS remains authoritative for assignments and completion, capability is its own derived domain, CRM owns operational adoption, and the data platform combines those signals for analytics.”

### 2. Show the happy path

Run `happy-path`.

Explain:

```text
HRIS provisioning
→ LMS assignment
→ LMS completion
→ capability update
→ CRM adoption
→ analytical refresh
```

Clarify that the correlation ID represents one business journey across multiple independently owned events.

### 3. Show contract governance

Open `/api/contracts` in Swagger.

Discuss:

- schema version
- required fields
- source/destination expectations
- rejection before downstream processing

### 4. Show idempotency

Run `duplicate`.

> “Retries and duplicate network deliveries are normal in distributed systems. I don't want a completion or capability update to be applied twice simply because a producer retried. The business-stable idempotency key is checked before downstream delivery.”

### 5. Show retry semantics

Run `retry-success`.

Point out that each destination fails twice and succeeds on the third attempt.

> “A retry policy should be bounded and observable. The system preserves each attempt rather than hiding retries.”

### 6. Show the DLQ

Run `dead-letter`.

> “Permanent failure should become an operational workflow, not silent data loss. After the retry budget is exhausted, the message lands in the dead-letter queue with correlation and payload context for triage or controlled replay.”

### 7. Discuss production architecture

Explain that a production system would replace synchronous simulated delivery with a managed broker, durable consumers, schema registry, service identities, centralized observability, contract compatibility testing, and formal replay controls.

## Strong closing statement

> “When I say I understand enterprise integrations, I don't only mean that I can call a REST endpoint. I think about ownership, contracts, event semantics, idempotency, failure recovery, version compatibility, observability, and how the data eventually supports business decisions.”
