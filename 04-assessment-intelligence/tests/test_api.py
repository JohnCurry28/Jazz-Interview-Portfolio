from fastapi.testclient import TestClient

from app.main import app


def test_health():
    with TestClient(app) as client:
        r = client.get('/health')
        assert r.status_code == 200
        assert r.json()['status'] == 'ok'


def test_overview_has_outcome_chain_metrics():
    with TestClient(app) as client:
        data = client.get('/api/overview').json()
        for key in ['completion_rate','assessment_mean','capability_mastery','adoption_rate','business_outcome_index','kr20_reliability']:
            assert key in data
        assert data['completion_rate'] > data['adoption_rate']


def test_item_metrics_are_bounded():
    with TestClient(app) as client:
        rows = client.get('/api/items').json()
        assert len(rows) == 12
        for row in rows:
            assert 0 <= row['difficulty'] <= 1
            assert -1 <= row['discrimination'] <= 1
            if row['item_rest_correlation'] is not None:
                assert -1 <= row['item_rest_correlation'] <= 1


def test_flawed_item_is_flagged_for_review():
    with TestClient(app) as client:
        rows = client.get('/api/items?status=REVIEW').json()
        assert rows
        assert any(x['item_id'] == 'Q09' for x in rows)


def test_capabilities_roll_up_assessment_and_adoption():
    with TestClient(app) as client:
        rows = client.get('/api/capabilities').json()
        assert len(rows) == 4
        assert all('mastery_rate' in x and 'adoption_score' in x for x in rows)


def test_cohorts_are_role_based():
    with TestClient(app) as client:
        rows = client.get('/api/cohorts').json()
        assert len(rows) == 4
        assert all(x['learners'] > 0 for x in rows)


def test_transfer_gap_view_returns_high_completion_risk_cases():
    with TestClient(app) as client:
        rows = client.get('/api/learners?risk_only=true').json()
        assert rows
        assert all(x['completion_score'] >= 0.90 for x in rows)
        assert all(x['capability_mastery'] < 0.70 or x['adoption_score'] < 0.60 for x in rows)


def test_insights_include_outcome_and_business_link():
    with TestClient(app) as client:
        rows = client.get('/api/insights').json()
        kinds = {x['type'] for x in rows}
        assert {'OUTCOME_CHAIN','CAPABILITY_GAP','ITEM_QUALITY','BUSINESS_LINK'} <= kinds


def test_metric_definitions_document_psychometrics():
    with TestClient(app) as client:
        data = client.get('/api/metric-definitions').json()
        assert 'discrimination' in data
        assert 'item_rest_correlation' in data
        assert 'kr20_reliability' in data


def test_lineage_keeps_system_of_record_boundaries_explicit():
    with TestClient(app) as client:
        rows = client.get('/api/data-lineage').json()
        systems = {x['system_of_record'] for x in rows}
        assert 'LMS' in systems
        assert 'CRM / workflow platform' in systems
        assert 'Enterprise data / BI' in systems
