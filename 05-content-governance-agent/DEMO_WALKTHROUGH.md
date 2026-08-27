# Interview Demo Walkthrough — Content Governance Agent

## Goal

Demonstrate that enterprise learning content should be governed as a lifecycle product, not treated as files uploaded once and forgotten.

## Suggested 6–8 minute walkthrough

### 1. Open with the principle

> "I designed this around a separation of responsibilities: automation can inspect and recommend, but people remain accountable for approval, publication, and retirement."

### 2. Show the dashboard

Point out the inventory, review queue, duplicate intelligence, lifecycle, and audit events.

Use the current synthetic metrics to explain that the portfolio includes deliberately imperfect assets so the governance system has meaningful decisions to make.

### 3. Healthy asset

Select **Commercial Data Literacy Reporting Guide**.

Explain:

- accountable owner exists
- source authority is approved
- review date is current
- accessibility signals pass
- version metadata is valid
- duplicate risk is low
- governance risk is LOW

This is the control case.

### 4. Overdue review

Select **Omnichannel Campaign Readiness Checklist**.

Say:

> "The content may still be useful, but the governance fact is that its review commitment has expired. The system should route that condition visibly instead of assuming yesterday's approval remains valid forever."

### 5. Accessibility failure

Select **Responsible AI Use for Commercial Teams**.

Show that content can be substantively strong while still not be publication-ready because accessibility metadata is incomplete.

### 6. Duplicate / reuse case

Select **CRM Workflow Quick Reference**.

It is intentionally very similar to the existing **Commercial CRM Workflow Guide**.

Say:

> "I don't want AI automatically deleting content because it looks similar. I want it to identify a reuse decision for the content owner: consolidate, differentiate, reuse, or document why both should exist."

### 7. High-risk legacy content

Select **Legacy Field Enablement FAQ**.

Show the combined risk:

- no owner
- unknown/unapproved source
- overdue review
- accessibility structure concerns

Say:

> "This is where governance becomes more important than content production. The correct output may be to retire or quarantine an asset rather than redesign it."

### 8. Human approval boundary

Use Swagger or the API to demonstrate that a high-risk item cannot be approved and a non-approved item cannot be published.

Key line:

> "The AI system does not own authority. Policy and human governance own authority."

### 9. Audit trail

Show the audit endpoint after agent scans and human decisions.

Explain that production audit events would include stronger identity, immutable storage, change references, approval evidence, and retention controls.

## Likely technical follow-ups

### Why not let the model approve low-risk content?
Because model confidence is not organizational authority. Approval is a business-control decision with accountability implications.

### Why use deterministic duplicate similarity?
For a portable MVP, it keeps the behavior inspectable. In production I would likely evaluate embeddings/semantic search while retaining thresholds and review behavior outside the model.

### How would you connect this to an LMS?
The governance service should sit upstream of publication. Approved content metadata and version IDs can be synchronized to LMS/LXP destinations through APIs/events, while source ownership stays in the governed repository.

### How would you handle global/local variants?
Add parent/variant relationships, market metadata, localization status, local owners, inheritance rules, and approval scopes. Duplicate detection should understand valid variants instead of treating them as accidental duplicates.

### Is the governance score a compliance score?
No. It is a prioritization/readiness signal for the demo. Production controls should map to explicit policies and evidence requirements rather than rely on one composite number.
