# Evaluation Strategy — Enterprise AI Performance Coach

A production RAG assistant should not be evaluated only by user satisfaction or fluency. This demo uses deterministic automated tests and defines a broader evaluation strategy for future model-backed versions.

## Evaluation dimensions

| Dimension | Question |
|---|---|
| Retrieval relevance | Did retrieval return the correct approved evidence? |
| Authorization | Was restricted evidence excluded for the caller? |
| Groundedness | Are answer claims supported by retrieved evidence? |
| Citation correctness | Does each citation actually support the associated claim? |
| Refusal precision | Does the system avoid refusing questions it can answer? |
| Refusal recall | Does it refuse unsupported questions consistently? |
| Injection resistance | Do adversarial instructions fail to override policy? |
| Sensitive-data handling | Are disallowed requests blocked or redirected? |
| Usefulness | Does the response help the employee complete the task? |
| Escalation quality | Does the system recommend the right next step when it cannot answer? |
| Latency | Is the answer fast enough for in-workflow support? |
| Knowledge freshness | Are only current approved versions used? |

## MVP automated regression cases

Current Pytest coverage includes:

- application health
- grounded answer with citations
- role-based content filtering
- unsupported-answer refusal
- prompt-injection blocking
- sensitive-data blocking
- audit-event persistence

## Proposed gold-set schema

```json
{
  "case_id": "EVAL-001",
  "role": "sales_rep",
  "question": "What do I need to verify before launching an omnichannel campaign?",
  "expected_status": "answered",
  "expected_documents": ["KB-CAMPAIGN-001"],
  "forbidden_documents": ["KB-MGR-003"],
  "required_concepts": ["approval", "content version"],
  "must_cite": true
}
```

## Safety/adversarial set

Include cases for:

- direct prompt injection
- indirect injection embedded in retrieved content
- role escalation attempts
- requests to reveal hidden instructions
- attempts to retrieve unauthorized manager content
- sensitive-data requests
- encoded/obfuscated injection instructions
- conflicting sources
- stale versus current source versions

## Release gate examples

A production release could require thresholds such as:

- 0 unauthorized-document retrievals in the authorization suite
- 100% block rate on high-severity known injection cases
- minimum groundedness score on gold-set answers
- citation precision above agreed threshold
- refusal behavior within defined precision/recall bounds
- no critical safety regressions from prior release

Exact thresholds should be calibrated to the use case and risk level rather than copied generically.

## Continuous evaluation

Production monitoring should sample real interactions into a privacy-safe evaluation workflow, with human review for:

- low-confidence answers
- disputed citations
- repeated refusals
- escalations
- user negative feedback
- policy violations

The evaluation set should grow as new failure modes are discovered.
