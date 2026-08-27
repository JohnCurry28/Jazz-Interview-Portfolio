# Interview Demo Walkthrough — Product Operations Control Plane

## 5–7 minute walkthrough

### 1. Open with the product thesis

> "The first five demos show individual learning-technology capabilities. This final demo is how I would operate them as a portfolio. I want outcomes, reliability, roadmap, risk, technical debt, dependencies, and architecture decisions visible in one place."

### 2. Start on Executive

Point to completion, mastery, adoption, governed-content readiness, AI grounded-answer rate, integration success, and availability.

> "I intentionally keep these signals separate. Completion is not mastery, mastery is not adoption, and adoption is not automatically causation. The control plane gives leadership the chain without collapsing it into one vanity score."

### 3. Show Product Health

Explain that each product has an owner, health state, adoption signal, availability, risks, and incidents.

> "The purpose is accountability and decision support, not red-yellow-green theater. Every red or amber state needs a reason and an owner."

### 4. Show Roadmap & Backlog

> "A roadmap should describe intended outcomes, while the backlog exposes the executable work and constraints underneath it."

### 5. Show Reliability & SLOs

> "If a service burns through its error budget, that changes prioritization. Reliability is product work, not a separate infrastructure concern."

### 6. Run Integration Outage

Click **Integration Outage** and call out that product health, CRM dependency, Integration Processor SLO, error budget, incident, and portfolio health all change together.

> "This is where the control plane becomes operational. A dependency failure changes both reliability and roadmap decisions."

### 7. Run AI Quality Regression

> "For AI, quality is operational telemetry. If grounded-answer rate falls after a knowledge release, I would roll back, run the eval suite, review governance eligibility, and treat that regression as an incident—not wait for users to complain."

### 8. Run Governance Backlog

> "Content governance is upstream of RAG quality. A large review backlog is not only a content-operations problem; it can become an AI knowledge-freshness risk."

### 9. Show Architecture & Debt

> "I want architectural trade-offs and technical debt visible enough to compete for capacity. If they're invisible, they accumulate until they become incidents or delivery constraints."

### 10. Close

> "This is the operating model behind the portfolio: product outcomes, explicit ownership, reliable integrations, governed AI, measurable learning effectiveness, controlled content, and transparent technical trade-offs."
