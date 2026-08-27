from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    r=client.get('/health'); assert r.status_code==200 and r.json()['status']=='ok'

def test_portfolio_contains_five_products():
    d=client.get('/api/portfolio').json(); assert len(d['products'])==5

def test_portfolio_health_score_baseline_positive():
    d=client.get('/api/portfolio').json(); assert 70 <= d['portfolio_metrics']['portfolio_health_score'] <= 100

def test_completion_adoption_gap_present():
    k=client.get('/api/portfolio').json()['cross_product_kpis']; assert k['learning_completion']-k['operational_adoption']>25

def test_roadmap_available():
    assert len(client.get('/api/roadmap').json()) >= 5

def test_p1_backlog_is_visible():
    rows=client.get('/api/backlog').json(); assert sum(1 for x in rows if x['priority']=='P1') >= 3

def test_technical_debt_contains_high_items():
    rows=client.get('/api/technical-debt').json(); assert any(x['severity']=='HIGH' for x in rows)

def test_architecture_decisions_present():
    rows=client.get('/api/architecture-decisions').json(); assert any(x['id']=='ADR-002' for x in rows)

def test_release_risk_scenario_marks_critical_dependency_red():
    d=client.post('/api/scenarios/release-risk').json(); dep=next(x for x in d['dependencies'] if x['name']=='Enterprise Identity'); assert dep['health']=='RED'; assert d['portfolio_metrics']['critical_dependency_issues']==1

def test_integration_outage_puts_slo_at_risk():
    d=client.post('/api/scenarios/integration-outage').json(); slo=next(x for x in d['slo_services'] if x['service']=='Integration Processor'); assert slo['status']=='AT_RISK'; assert d['portfolio_metrics']['at_risk_slos']==1

def test_ai_quality_regression_generates_insight():
    d=client.post('/api/scenarios/ai-quality').json(); assert d['cross_product_kpis']['ai_grounded_answer_rate']==71.0; assert any('AI grounded-answer quality degraded'==x['title'] for x in d['executive_insights'])

def test_governance_backlog_degrades_readiness():
    d=client.post('/api/scenarios/governance-backlog').json(); assert d['cross_product_kpis']['governed_content_ready']==42.0; assert any('Governance readiness is below threshold'==x['title'] for x in d['executive_insights'])

def test_unknown_scenario_returns_404():
    assert client.post('/api/scenarios/nope').status_code==404

def test_slo_targets_measured():
    rows=client.get('/api/slos').json(); assert all(x['actual']>0 and x['target']>0 for x in rows)

def test_dependency_ownership_explicit():
    rows=client.get('/api/dependencies').json(); assert all(x['owner'] for x in rows)
