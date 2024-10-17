import pytest

pytestmark = pytest.mark.unit


def test_health_check(mocker, client):
    """Test the health check endpoint."""
    mocker.patch(
        "api.route.v1.health.health_routes.db.session.execute"
    ).return_value = True

    response = client.get("/api/v1/health-check")

    assert response.status_code == 200
    assert response.json == {"status": "UP", "db_status": True}


def test_health_check_db_failure(mocker, client):
    """Test the health check endpoint when the database is down."""
    mocker.patch(
        "api.route.v1.health.health_routes.db.session.execute"
    ).side_effect = Exception

    response = client.get("/api/v1/health-check")

    assert response.status_code == 200
    assert response.json == {"status": "UP", "db_status": False}


def test_not_found(app, client):
    with app.app_context():
        response = client.get("/api/v1/not-found")
        assert response.status_code == 404
        assert response.json == {"error": "Page not found"}
