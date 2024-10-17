import pytest
from flask.testing import FlaskClient

pytestmark = pytest.mark.integration


def test_health(test_client: FlaskClient):
    response = test_client.get("/api/v1/health-check")

    assert response.status_code == 200
    assert response.json == {"status": "UP", "db_status": True}


def test_page_not_found(test_client: FlaskClient):
    response = test_client.get("/api/v1/health/1")

    assert response.status_code == 404
    assert response.json == {"error": "Page not found"}
