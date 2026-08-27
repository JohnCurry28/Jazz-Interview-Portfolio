from fastapi.testclient import TestClient
from app.main import app
from app.db import init_db

init_db()
client = TestClient(app)


def test_health():
    r = client.get('/health')
    assert r.status_code == 200
    assert r.json()['status'] == 'ok'


def test_overview():
    r = client.get('/api/dashboard/overview')
    assert r.status_code == 200
    data = r.json()
    assert data['active_users'] >= 4
    assert 'adoption_pct' in data


def test_learner_capabilities():
    r = client.get('/api/users/1/capabilities')
    assert r.status_code == 200
    assert len(r.json()) >= 5


def test_governance_assets():
    r = client.get('/api/governance/assets')
    assert r.status_code == 200
    assert any(x['status'] == 'In Review' for x in r.json())
