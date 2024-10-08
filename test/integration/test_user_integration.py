import pytest

pytestmark = pytest.mark.integration


def test_create_user(test_client):
    response = test_client.post(
        "/api/v1/users",
        json={"name": "Test", "lastname": "User", "born": "1990-01-01"},
    )

    assert response.status_code == 200
    data = response.get_json()
    assert data["name"] == "Test"
    assert data["lastname"] == "User"
    assert data["born"] == "1990-01-01"


def test_create_user_without_name(test_client):
    response = test_client.post(
        "/api/v1/users",
        json={"lastname": "User", "born": "1990-01-01"},
    )

    assert response.status_code == 400
    assert response.get_json() == {"name": ["Missing data for required field."]}


def test_get_all_users_with_generic_exception(test_client, mocker):
    mocker.patch(
        "api.controller.user_controller.UserService.get_all_users",
        side_effect=Exception,
    )

    response = test_client.get("/api/v1/users")

    assert response.status_code == 500
    assert response.get_json() == {"error": "An unexpected error occurred"}


def test_get_all(test_client):
    response = test_client.get("/api/v1/users")

    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)
    assert len(data) > 0
    assert data[0]["name"] == "Test"
    assert data[0]["lastname"] == "User"
    assert data[0]["born"] == "1990-01-01"
    assert data[0]["id"] == 1


def test_get_user_by_id(test_client):
    response = test_client.get("/api/v1/users/1")

    assert response.status_code == 200
    data = response.get_json()
    assert data["name"] == "Test"
    assert data["lastname"] == "User"
    assert data["born"] == "1990-01-01"


def test_update_user(test_client):
    current_user = test_client.get("/api/v1/users/1").get_json()

    response = test_client.put(
        "/api/v1/users/1",
        json={"name": "User", "lastname": "Test", "born": "2024-10-04"},
    )

    assert response.status_code == 200
    data = response.get_json()
    assert current_user["name"] != data["name"]
    assert current_user["lastname"] != data["lastname"]
    assert current_user["born"] != data["born"]
    assert data["name"] == "User"
    assert data["lastname"] == "Test"
    assert data["born"] == "2024-10-04"


def test_update_user_not_exists(test_client):
    response = test_client.put(
        "/api/v1/users/10",
        json={"name": "User", "lastname": "Test", "born": "2024-10-04"},
    )

    assert response.status_code == 404
    assert response.get_json() == {"error": "User not found"}


def test_delete_user(test_client):
    response = test_client.delete("/api/v1/users/1")
    assert response.status_code == 204

    # Verify the user is deleted
    response = test_client.get("/api/v1/users/1")
    assert response.status_code == 404
    assert response.get_json() == {"error": "User not found"}


def test_delete_user_not_exists(test_client):
    response = test_client.delete("/api/v1/users/10")
    assert response.status_code == 404
    assert response.get_json() == {"error": "User not found"}
