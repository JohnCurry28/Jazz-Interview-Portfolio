# Governance Controls Reference

## Automated checks

| Control | Purpose | MVP behavior | Production evolution |
|---|---|---|---|
| Ownership | Ensure accountability | Missing owner = FAIL | Directory / ownership registry validation |
| Source authority | Ensure trustworthy source | Unapproved source = FAIL | Managed source registry / policy engine |
| Review date | Prevent stale content | Overdue = FAIL; <=30 days = WARN | Scheduled review workflows / notifications |
| Accessibility | Identify obvious readiness gaps | Metadata checks for alt text, captions, headings, links | Automated scanners + human accessibility QA |
| Version metadata | Support lifecycle traceability | `major.minor` version required | Repository-native version IDs + release metadata |
| Content substance | Prevent empty placeholder assets | Short content = WARN | Content-type-specific validation |
| Duplicate similarity | Promote reuse/consolidation | Cosine similarity over title + body | Embeddings, semantic clustering, repository search |

## Governance score

The MVP governance score is an interview-friendly readiness indicator, not a validated compliance score.

```text
base_score = mean(check scores)

duplicate penalty:
  similarity >= .82  → -0.15
  similarity >= .68  → -0.07

score = max(0, base_score - duplicate_penalty) × 100
```

## Risk classification

```text
HIGH
- missing ownership or unapproved source
- OR governance score < 60

MEDIUM
- governance score < 82
- OR duplicate similarity >= .68
- OR any remaining FAIL

LOW
- no above condition
```

## Human authority

The following decisions are modeled as human-governance actions:

- APPROVE
- PUBLISH
- RETIRE
- REJECT
- REQUEST_CHANGES

The agent may recommend a proposed state but does not execute authoritative transitions.

## Publication rule

For the MVP:

```text
PUBLISH is allowed only when:
  current_state == APPROVED
  AND risk_level == LOW
```

This makes the approval boundary inspectable in code and testable through the API.

## Accessibility boundary

The accessibility checks are intentionally described as readiness checks, not certification. A full accessibility program would require automated and manual review against applicable WCAG criteria, testing with assistive technology, and governance for remediation exceptions.

## Duplicate boundary

Similarity is not a deletion rule. A high duplicate score should trigger a human decision among:

- reuse existing asset
- consolidate content
- create a role/local variant
- retain both with documented rationale
- retire obsolete content
