# Architecture — Enterprise Content Governance Agent

## Purpose

This reference implementation models a governed enterprise content lifecycle in which automated intelligence can inspect and recommend, but authoritative approval and publication remain human-controlled.

## High-level architecture

```text
Content Author / Source System
          │
          ▼
   Content Inventory
          │
          ▼
  Governance Agent
  ├── Metadata checks
  ├── Ownership checks
  ├── Source-authority checks
  ├── Review-date checks
  ├── Accessibility checks
  ├── Duplicate/reuse detection
  └── Risk / lifecycle recommendation
          │
          ▼
   Governance Record
          │
   ┌──────┴────────┐
   ▼               ▼
Human Review    Audit / Analytics
   │
   ├── APPROVE
   ├── REQUEST CHANGES
   ├── REJECT
   ├── PUBLISH
   └── RETIRE
          │
          ▼
 Content Lifecycle
```

## Core boundary

The agent is advisory. It cannot execute authoritative governance decisions.

```text
AGENT MAY                    AGENT MAY NOT
─────────                    ─────────────
Inspect metadata             Approve content
Flag risk                    Publish content
Detect duplicates            Retire content
Check dates                  Override a reviewer
Check accessibility          Bypass source authority
Recommend a state            Rewrite audit history
```

## Lifecycle

```text
DRAFT
  ↓
TECHNICAL_REVIEW
  ↓
CONTENT_OWNER_REVIEW
  ↓
APPROVED
  ↓
PUBLISHED
  ↓
MONITORED
  ↓
REVIEW_REQUIRED
  ↓
RETIRED
```

The lifecycle is not required to be perfectly linear in production. Content may move backward for changes, re-review, or remediation.

## Governance domains

### Ownership
A governed asset should have a named accountable owner. The agent treats missing ownership as a blocking failure.

### Source authority
The content must be attributable to an approved source authority. An unapproved source is a blocking condition.

### Review cadence
Review dates are treated as operational controls. An overdue review generates a failure; an upcoming review generates a warning.

### Accessibility
The MVP checks metadata signals for alt text, captions/transcripts, heading order, and descriptive links. These are not substitutes for a full WCAG accessibility audit.

### Versioning
Every seeded content asset has a semantic `major.minor` version and an immutable snapshot in the `versions` table.

### Duplicate / reuse intelligence
A deterministic cosine-similarity function compares title + body text. High similarity is a prompt for reuse/consolidation review, not automatic deletion.

### Human review
The review endpoint enforces human decision semantics. Publication requires both an `APPROVED` state and `LOW` governance risk.

## Data model

```text
content_items
  ├── identity / type
  ├── owner
  ├── source authority
  ├── version
  ├── review due date
  ├── accessibility metadata
  ├── approved-source flag
  └── lifecycle state

      │
      ├── governance_checks
      ├── duplicate_candidates
      ├── versions
      └── audit_log
```

## AI/provider boundary

The MVP uses deterministic rules to keep interview behavior portable and inspectable. A production implementation could add an LLM/provider behind an abstraction for tasks such as:

- metadata extraction
- plain-language review summaries
- duplicate explanation
- proposed taxonomy tags
- accessibility remediation suggestions
- change-impact summaries

The provider must not own authorization, lifecycle state, approval, or audit history.

## Production evolution

A production architecture would likely add:

- SSO/OIDC and identity claims
- RBAC/ABAC
- workflow engine
- enterprise content repository integration
- managed database
- object storage/versioning
- event bus
- source registry
- policy engine
- accessibility scanning services
- semantic/vector duplicate detection
- notification service
- SLA/SLO monitoring
- immutable audit storage
- legal/compliance/privacy review
