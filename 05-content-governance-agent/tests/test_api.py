from fastapi.testclient import TestClient

from app import db
from app.main import app

client = TestClient(app)


def setup_function():
    db.reset_db()


def test_health():
    r = client.get('/health')
    assert r.status_code == 200
    assert r.json()['status'] == 'ok'


def test_seed_inventory():
    r = client.get('/api/items')
    assert r.status_code == 200
    assert len(r.json()) == 6


def test_dashboard_summary():
    d = client.get('/api/dashboard').json()
    assert d['summary']['content_assets'] == 6
    assert d['summary']['review_queue'] >= 2
    assert d['summary']['duplicate_flags'] >= 1


def test_overdue_review_flagged():
    scan = client.post('/api/agent/scan', json={'item_id': 2, 'actor': 'test'}).json()
    check = next(c for c in scan['checks'] if c['check_name'] == 'Review Date')
    assert check['status'] == 'FAIL'


def test_accessibility_failure_detected():
    scan = client.post('/api/agent/scan', json={'item_id': 3}).json()
    check = next(c for c in scan['checks'] if c['check_name'] == 'Accessibility')
    assert check['status'] == 'FAIL'


def test_duplicate_candidate_detected():
    scan = client.post('/api/agent/scan', json={'item_id': 4}).json()
    assert scan['duplicate'] is not None
    assert scan['duplicate']['similarity'] >= 0.82


def test_high_risk_legacy_asset():
    scan = client.post('/api/agent/scan', json={'item_id': 6}).json()
    assert scan['recommendation']['risk_level'] == 'HIGH'
    assert scan['recommendation']['human_approval_required'] is False


def test_agent_cannot_publish():
    scan = client.post('/api/agent/scan', json={'item_id': 1}).json()
    assert 'Recommendation only' in scan['recommendation']['agent_boundary']


def test_human_publish_blocked_without_approved_state():
    r = client.post('/api/items/4/review', json={'reviewer': 'Governance Lead', 'action': 'PUBLISH', 'note': 'Attempt publish'}).json()
    assert r['allowed'] is False


def test_human_approval_blocked_for_high_risk_asset():
    r = client.post('/api/items/6/review', json={'reviewer': 'Governance Lead', 'action': 'APPROVE', 'note': 'Attempt approval'}).json()
    assert r['allowed'] is False


def test_human_approval_allowed_for_low_risk_draft():
    r = client.post('/api/items/5/review', json={'reviewer': 'Governance Lead', 'action': 'APPROVE', 'note': 'Governance review complete'}).json()
    assert r['allowed'] is True
    assert client.get('/api/items/5').json()['lifecycle_state'] == 'APPROVED'


def test_audit_log_records_agent_and_human_actions():
    client.post('/api/agent/scan', json={'item_id': 2, 'actor': 'test-agent'})
    client.post('/api/items/2/review', json={'reviewer': 'Reviewer', 'action': 'REQUEST_CHANGES', 'note': 'Update required'})
    events = client.get('/api/audit').json()
    types = {e['event_type'] for e in events}
    assert 'AGENT_SCAN' in types
    assert 'HUMAN_DECISION' in types


def test_versions_endpoint():
    versions = client.get('/api/items/1/versions').json()
    assert versions
    assert versions[0]['version'] == '2.3'
