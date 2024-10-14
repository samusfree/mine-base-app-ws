import pytest

pytestmark = pytest.mark.unit


def test_health_check(app, client):
    with app.app_context():
        response = client.get("/api/v1/health-check")

        assert response.status_code == 200
        assert response.json == {"status": "UP"}


def test_not_found(app, client):
    with app.app_context():
        response = client.get("/api/v1/not-found")

        assert response.status_code == 404
        assert response.json == {"error": "Page not found"}
