from datetime import date

import pytest

from api.controller.user_controller import UserController
from api.model.user import User
from api.service.user_service import UserService

pytestmark = pytest.mark.unit


@pytest.fixture
def mock_user_service(mocker) -> UserService:
    return mocker.patch("api.controller.user_controller.UserService")


@pytest.fixture
def user_controller(mock_user_service) -> UserController:
    return UserController(user_service=mock_user_service)


def test_get_users(app, mock_user_service, user_controller, mocker, client):
    with app.app_context():
        mocker.patch(
            "api.route.v1.users.user_routes.user_controller",
            user_controller,
        )
        mock_user_service.get_all_users.return_value = [
            User(id=1, name="User", lastname="Test")
        ]

        response = client.get("/api/v1/users")

        assert response.status_code == 200
        assert response.content_type == "application/json"
        assert len(response.json) == 1
        assert response.json[0]["id"] == 1
        assert response.json[0]["name"] == "User"
        assert response.json[0]["lastname"] == "Test"
        mock_user_service.get_all_users.assert_called_once()


def test_get_user(app, mock_user_service, user_controller, mocker, client):
    with app.app_context():
        mocker.patch(
            "api.route.v1.users.user_routes.user_controller",
            user_controller,
        )
        mock_user_service.get_user_by_id.return_value = User(
            id=1, name="User", lastname="Test"
        )

        response = client.get("/api/v1/users/1")

        assert response.status_code == 200
        assert response.content_type == "application/json"
        assert response.json["id"] == 1
        assert response.json["name"] == "User"
        assert response.json["lastname"] == "Test"
        mock_user_service.get_user_by_id.assert_called_once_with(1)


def test_get_user_no_exists(
    app, mock_user_service, user_controller, mocker, client
):
    with app.app_context():
        mocker.patch(
            "api.route.v1.users.user_routes.user_controller",
            user_controller,
        )
        mock_user_service.get_user_by_id.return_value = None

        response = client.get("/api/v1/users/1")

        assert response.status_code == 404
        assert response.content_type == "application/json"
        assert response.json == {"error": "User not found"}
        mock_user_service.get_user_by_id.assert_called_once_with(1)


def test_create_user(app, mock_user_service, user_controller, mocker, client):
    with app.app_context():
        mocker.patch(
            "api.route.v1.users.user_routes.user_controller",
            user_controller,
        )
        mock_user_service.create_user.return_value = User(
            id=1,
            name="User",
            lastname="Test",
            born=date.fromisoformat("2024-10-04"),
        )

        response = client.post(
            "/api/v1/users",
            json={"name": "Test", "lastname": "User", "born": "2024-10-04"},
        )

        assert response.status_code == 200
        assert response.content_type == "application/json"
        assert response.json["id"] == 1
        assert response.json["name"] == "User"
        assert response.json["lastname"] == "Test"
        assert response.json["born"] == "2024-10-04"
        mock_user_service.create_user.assert_called_once()


def test_create_user_without_name(
    app, mock_user_service, user_controller, mocker, client
):
    with app.app_context():
        mocker.patch(
            "api.route.v1.users.user_routes.user_controller",
            user_controller,
        )

        response = client.post(
            "/api/v1/users",
            json={"lastname": "User", "born": "2024-10-04"},
        )

        assert response.status_code == 400
        assert response.content_type == "application/json"
        assert response.json == {"name": ["Missing data for required field."]}
        mock_user_service.create_user.assert_not_called()


def test_create_user_with_error(
    app, mock_user_service, user_controller, mocker, client
):
    with app.app_context():
        mocker.patch(
            "api.route.v1.users.user_routes.user_controller",
            user_controller,
        )
        mocker.patch(
            "api.controller.user_controller.UserService.create_user",
            side_effect=Exception,
        )

        response = client.post(
            "/api/v1/users",
            json={"name": "Test", "lastname": "User", "born": "2024-10-04"},
        )

        assert response.status_code == 500
        assert response.content_type == "application/json"
        assert response.json == {"error": "An unexpected error occurred"}
        mock_user_service.create_user.assert_called_once()


def test_update_user(app, mock_user_service, user_controller, mocker, client):
    with app.app_context():
        mocker.patch(
            "api.route.v1.users.user_routes.user_controller",
            user_controller,
        )
        mock_user_service.get_user_by_id.return_value = User(
            id=1,
            name="User",
            lastname="Test",
            born=date.fromisoformat("2024-10-02"),
        )
        mock_user_service.update_user.return_value = User(
            id=1,
            name="Test",
            lastname="User",
            born=date.fromisoformat("2024-10-04"),
        )

        response = client.put(
            "/api/v1/users/1",
            json={"name": "Test", "lastname": "User", "born": "2024-10-04"},
        )

        assert response.status_code == 200
        assert response.content_type == "application/json"
        assert response.json["id"] == 1
        assert response.json["name"] == "Test"
        assert response.json["lastname"] == "User"
        assert response.json["born"] == "2024-10-04"
        mock_user_service.update_user.assert_called_once_with(
            1, {"name": "Test", "lastname": "User", "born": date(2024, 10, 4)}
        )


def test_delete_user(app, mock_user_service, user_controller, mocker, client):
    with app.app_context():
        mocker.patch(
            "api.route.v1.users.user_routes.user_controller",
            user_controller,
        )
        mock_user_service.delete_user.return_value = None

        response = client.delete("/api/v1/users/1")

        assert response.status_code == 204
        assert response.json is None
        mock_user_service.delete_user.assert_called_once_with(1)
