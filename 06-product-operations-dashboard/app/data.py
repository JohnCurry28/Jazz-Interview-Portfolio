from __future__ import annotations

from copy import deepcopy

PORTFOLIO = {
    "as_of": "2026-08-26T21:35:00-04:00",
    "products": [
        {"id":"capability-hub","name":"Global Learning Capability Hub","owner":"Learning Platforms","health":"GREEN","adoption":78.0,"slo":99.95,"availability":99.98,"open_risks":1,"open_incidents":0,"release":"v0.1"},
        {"id":"ai-coach","name":"Enterprise AI Performance Coach","owner":"AI Enablement","health":"AMBER","adoption":64.0,"slo":99.90,"availability":99.93,"open_risks":2,"open_incidents":0,"release":"v0.2"},
        {"id":"integration-lab","name":"LMS ↔ CRM ↔ Enterprise Data Integration","owner":"Enterprise Integration","health":"GREEN","adoption":100.0,"slo":99.90,"availability":99.96,"open_risks":1,"open_incidents":0,"release":"v0.3"},
        {"id":"assessment-intelligence","name":"Enterprise Assessment Intelligence","owner":"Learning Intelligence","health":"GREEN","adoption":72.7,"slo":99.50,"availability":99.97,"open_risks":1,"open_incidents":0,"release":"v0.4"},
        {"id":"content-governance","name":"Enterprise Content Governance Agent","owner":"Content Operations","health":"AMBER","adoption":81.0,"slo":99.50,"availability":99.91,"open_risks":3,"open_incidents":0,"release":"v0.5"}
    ],
    "roadmap": [
        {"quarter":"Q3 2026","initiative":"Unify capability and adoption signals","product":"Capability Hub","status":"IN_PROGRESS","outcome":"Single role → capability → adoption view","confidence":"HIGH"},
        {"quarter":"Q3 2026","initiative":"RAG governance eligibility feed","product":"AI Coach + Governance","status":"IN_PROGRESS","outcome":"Only approved knowledge is retrievable","confidence":"HIGH"},
        {"quarter":"Q4 2026","initiative":"Enterprise event broker hardening","product":"Integration Layer","status":"PLANNED","outcome":"Durable retries, DLQ and schema registry","confidence":"MEDIUM"},
        {"quarter":"Q4 2026","initiative":"Manager intervention recommendations","product":"Assessment Intelligence","status":"PLANNED","outcome":"Learning vs workflow vs coaching diagnosis","confidence":"MEDIUM"},
        {"quarter":"Q1 2027","initiative":"Portfolio SLO and cost telemetry","product":"Product Operations","status":"PLANNED","outcome":"Operational health and unit economics","confidence":"MEDIUM"}
    ],
    "backlog": [
        {"id":"BL-101","title":"Add SSO/OIDC reference integration","product":"Platform","priority":"P1","status":"READY","owner":"Platform Engineering","age_days":12},
        {"id":"BL-102","title":"Add semantic retrieval provider adapter","product":"AI Coach","priority":"P1","status":"IN_PROGRESS","owner":"AI Enablement","age_days":8},
        {"id":"BL-103","title":"Externalize event schema registry","product":"Integration Layer","priority":"P1","status":"READY","owner":"Enterprise Integration","age_days":19},
        {"id":"BL-104","title":"Add accessibility deep-scan connector","product":"Content Governance","priority":"P2","status":"DISCOVERY","owner":"Content Operations","age_days":21},
        {"id":"BL-105","title":"Add manager reinforcement workflow","product":"Assessment Intelligence","priority":"P2","status":"DISCOVERY","owner":"Learning Intelligence","age_days":16},
        {"id":"BL-106","title":"Define cross-product analytics contracts","product":"Enterprise Data","priority":"P1","status":"IN_PROGRESS","owner":"Data Architecture","age_days":25}
    ],
    "technical_debt": [
        {"id":"TD-01","area":"Persistence","product":"Multiple","severity":"HIGH","item":"SQLite is appropriate for demos but not multi-user production workloads","remediation":"Managed PostgreSQL + migrations + backup/restore","status":"OPEN"},
        {"id":"TD-02","area":"Identity","product":"Multiple","severity":"HIGH","item":"Synthetic role context instead of enterprise identity","remediation":"OIDC SSO + RBAC/ABAC + service identity","status":"OPEN"},
        {"id":"TD-03","area":"Messaging","product":"Integration Layer","severity":"MEDIUM","item":"In-process delivery simulator","remediation":"Kafka / EventBridge / Service Bus + schema registry","status":"PLANNED"},
        {"id":"TD-04","area":"AI Retrieval","product":"AI Coach","severity":"MEDIUM","item":"Deterministic lexical retrieval for portable demo","remediation":"Embedding/vector retrieval + reranking + eval harness","status":"PLANNED"},
        {"id":"TD-05","area":"Accessibility","product":"Content Governance","severity":"MEDIUM","item":"Readiness signals are not full conformance testing","remediation":"Automated scanner + manual WCAG verification workflow","status":"OPEN"}
    ],
    "dependencies": [
        {"name":"Enterprise Identity","type":"INTERNAL","products":"All","criticality":"CRITICAL","health":"GREEN","owner":"Identity & Access"},
        {"name":"LMS / LXP","type":"VENDOR","products":"Capability Hub, Assessment","criticality":"CRITICAL","health":"GREEN","owner":"Learning Platforms"},
        {"name":"CRM","type":"VENDOR","products":"Integration, Assessment","criticality":"HIGH","health":"GREEN","owner":"Commercial Technology"},
        {"name":"Enterprise Data Platform","type":"INTERNAL","products":"Integration, Assessment, Ops","criticality":"CRITICAL","health":"GREEN","owner":"Data Platform"},
        {"name":"LLM Provider","type":"VENDOR","products":"AI Coach, Governance","criticality":"HIGH","health":"AMBER","owner":"AI Platform"},
        {"name":"Content Repository","type":"INTERNAL","products":"Governance, AI Coach","criticality":"HIGH","health":"GREEN","owner":"Content Operations"}
    ],
    "architecture_decisions": [
        {"id":"ADR-001","decision":"Keep systems of record explicit","status":"ACCEPTED","rationale":"Integration moves facts but does not redefine authoritative ownership."},
        {"id":"ADR-002","decision":"Authorize before AI retrieval","status":"ACCEPTED","rationale":"Prompt instructions are not an access-control boundary."},
        {"id":"ADR-003","decision":"Separate AI recommendation from human approval","status":"ACCEPTED","rationale":"Model confidence does not create organizational authority."},
        {"id":"ADR-004","decision":"Treat completion, mastery and adoption as separate signals","status":"ACCEPTED","rationale":"They answer different business questions and should not be collapsed."},
        {"id":"ADR-005","decision":"Use deterministic demo services where portability matters","status":"ACCEPTED","rationale":"Interview reliability is prioritized while production boundaries remain documented."}
    ],
    "incidents": [
        {"id":"INC-000","severity":"NONE","product":"Portfolio","status":"CLOSED","summary":"No active synthetic incidents","started_at":None,"mttr_minutes":0}
    ],
    "risks": [
        {"id":"R-01","product":"AI Coach","severity":"HIGH","risk":"Knowledge freshness can degrade answer quality","mitigation":"Governance eligibility + review dates + eval regression","owner":"AI Enablement"},
        {"id":"R-02","product":"Content Governance","severity":"HIGH","risk":"Review backlog can allow stale content to remain visible","mitigation":"SLA queue + owner escalation + publish guard","owner":"Content Operations"},
        {"id":"R-03","product":"Integration Layer","severity":"MEDIUM","risk":"Schema drift can break consumers","mitigation":"Schema registry + compatibility policy + contract tests","owner":"Enterprise Integration"},
        {"id":"R-04","product":"Assessment Intelligence","severity":"MEDIUM","risk":"Analytics may be overinterpreted as causal","mitigation":"Evidence labels + SME review + causal caution in UI/docs","owner":"Learning Intelligence"}
    ],
    "slo_services": [
        {"service":"Capability API","target":99.95,"actual":99.98,"error_budget_remaining":72,"latency_ms":118,"status":"MEETING"},
        {"service":"AI Coach API","target":99.90,"actual":99.93,"error_budget_remaining":39,"latency_ms":742,"status":"MEETING"},
        {"service":"Integration Processor","target":99.90,"actual":99.96,"error_budget_remaining":61,"latency_ms":186,"status":"MEETING"},
        {"service":"Assessment API","target":99.50,"actual":99.97,"error_budget_remaining":88,"latency_ms":154,"status":"MEETING"},
        {"service":"Governance API","target":99.50,"actual":99.91,"error_budget_remaining":52,"latency_ms":229,"status":"MEETING"}
    ],
    "cross_product_kpis": {
        "learning_completion": 96.2,
        "capability_mastery": 72.7,
        "operational_adoption": 51.9,
        "governed_content_ready": 66.7,
        "ai_grounded_answer_rate": 88.0,
        "integration_delivery_success": 99.4,
        "portfolio_availability": 99.95
    }
}

SCENARIOS = {
    "release-risk": {
        "description":"A release is blocked by an unresolved high-severity identity dependency and aging P1 work.",
        "product_updates":{"capability-hub":{"health":"AMBER","open_risks":2}},
        "dependency_updates":{"Enterprise Identity":{"health":"RED"}},
        "incident":{"id":"INC-201","severity":"SEV2","product":"Capability Hub","status":"OPEN","summary":"SSO dependency unavailable in pre-production release validation","started_at":"2026-08-26T20:45:00-04:00","mttr_minutes":0},
        "risk":{"id":"R-201","product":"Capability Hub","severity":"HIGH","risk":"Release readiness blocked by identity dependency","mitigation":"Hold release; failover validation; identity owner escalation","owner":"Learning Platforms"}
    },
    "integration-outage": {
        "description":"CRM event delivery degrades and consumes the Integration Processor error budget.",
        "product_updates":{"integration-lab":{"health":"RED","open_incidents":1}},
        "dependency_updates":{"CRM":{"health":"RED"}},
        "slo_updates":{"Integration Processor":{"actual":99.61,"error_budget_remaining":8,"latency_ms":965,"status":"AT_RISK"}},
        "incident":{"id":"INC-301","severity":"SEV2","product":"Integration Layer","status":"OPEN","summary":"CRM destination failures are retrying and entering DLQ","started_at":"2026-08-26T21:00:00-04:00","mttr_minutes":0},
        "risk":{"id":"R-301","product":"Integration Layer","severity":"HIGH","risk":"Adoption signals may be delayed","mitigation":"Retry queue monitoring + DLQ replay + CRM owner escalation","owner":"Enterprise Integration"}
    },
    "ai-quality": {
        "description":"Grounded answer rate falls below the product threshold after a knowledge refresh.",
        "product_updates":{"ai-coach":{"health":"RED","open_risks":3}},
        "kpi_updates":{"ai_grounded_answer_rate":71.0},
        "incident":{"id":"INC-401","severity":"SEV3","product":"AI Coach","status":"OPEN","summary":"Grounded answer regression after knowledge update","started_at":"2026-08-26T21:10:00-04:00","mttr_minutes":0},
        "risk":{"id":"R-401","product":"AI Coach","severity":"HIGH","risk":"Unsupported or weakly grounded answers increase","mitigation":"Roll back knowledge release; run eval suite; review governance eligibility","owner":"AI Enablement"}
    },
    "governance-backlog": {
        "description":"Review queue expansion creates stale-content exposure risk.",
        "product_updates":{"content-governance":{"health":"RED","open_risks":5}},
        "kpi_updates":{"governed_content_ready":42.0},
        "incident":{"id":"INC-501","severity":"SEV3","product":"Content Governance","status":"OPEN","summary":"Governance review backlog exceeds operating threshold","started_at":"2026-08-26T19:30:00-04:00","mttr_minutes":0},
        "risk":{"id":"R-501","product":"Content Governance","severity":"HIGH","risk":"Stale content may remain eligible too long","mitigation":"Owner escalation + temporary RAG eligibility tightening + backlog burn-down","owner":"Content Operations"}
    }
}


def base_state() -> dict:
    return deepcopy(PORTFOLIO)


def apply_scenario(name: str) -> dict:
    state = base_state()
    scenario = SCENARIOS[name]
    for product in state["products"]:
        patch = scenario.get("product_updates", {}).get(product["id"])
        if patch:
            product.update(patch)
    for dep in state["dependencies"]:
        patch = scenario.get("dependency_updates", {}).get(dep["name"])
        if patch:
            dep.update(patch)
    for slo in state["slo_services"]:
        patch = scenario.get("slo_updates", {}).get(slo["service"])
        if patch:
            slo.update(patch)
    state["cross_product_kpis"].update(scenario.get("kpi_updates", {}))
    state["incidents"] = [scenario["incident"]]
    state["risks"] = [scenario["risk"], *state["risks"]]
    state["scenario"] = {"name": name, "description": scenario["description"]}
    return state
