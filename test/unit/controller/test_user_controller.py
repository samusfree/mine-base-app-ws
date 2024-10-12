from datetime import date

import pytest

from api.controller.user_controller import UserController
from api.exception.not_found_error import NotFoundError
from api.model.user import User
from api.service.user_service import UserService

pytestmark = pytest.mark.unit


@pytest.fixture
def user_service_mock(mocker):
    return mocker.Mock(spec=UserService)


@pytest.fixture
def user_controller(user_service_mock) -> UserController:
    return UserController(user_service=user_service_mock)


def test_get_users(app, user_controller: UserController, user_service_mock):
    with app.app_context():
        user_service_mock.get_all_users.return_value = [
            {"id": 1, "name": "Test", "lastname": "User"}
        ]

        response = user_controller.get_users()

        assert response.status_code == 200
        assert response.json == [
            {"id": 1, "name": "Test", "lastname": "User"}
        ]


def test_get_user(app, user_controller, user_service_mock):
    with app.app_context():
        user_service_mock.get_user_by_id.return_value = {
            "id": 1,
            "name": "Test",
            "lastname": "User",
        }

        response = user_controller.get_user(1)

        assert response.status_code == 200
        assert response.json == {"id": 1, "name": "Test", "lastname": "User"}


def test_get_user_no_exists(app, user_controller, user_service_mock):
    with app.app_context():
        user_service_mock.get_user_by_id.return_value = None

        with pytest.raises(NotFoundError):
            user_controller.get_user(1)


def test_create_user(
    app, user_controller: UserController, user_service_mock, mocker
):
    with app.app_context():
        mocker.patch(
            "flask.request.get_json",
            return_value={
                "name": "Test",
                "lastname": "User",
                "born": "2024-10-07",
            },
        )
        user_service_mock.create_user.return_value = User(
            id=1,
            name="Test",
            lastname="User",
            born=date.fromisoformat("2024-10-07"),
        )

        response = user_controller.create_user()

        assert response.status_code == 200
        assert response.json == {
            "id": 1,
            "name": "Test",
            "lastname": "User",
            "born": "2024-10-07",
        }


def test_update_user(
    app,
    user_controller: UserController,
    user_service_mock: UserService,
    mocker,
):
    with app.app_context():
        mocker.patch(
            "flask.request.get_json",
            return_value={
                "name": "Test",
                "lastname": "User",
                "born": "2024-10-02",
            },
        )
        user_service_mock.update_user.return_value = User(
            id=1,
            name="Test",
            lastname="User",
            born=date.fromisoformat("2024-10-02"),
        )

        response = user_controller.update_user(1)

        assert response.status_code == 200
        assert response.json == {
            "id": 1,
            "name": "Test",
            "lastname": "User",
            "born": "2024-10-02",
        }


def test_update_user_no_exists(app, user_controller, user_service_mock):
    with app.app_context():
        user_service_mock.get_user_by_id.return_value = None

        with pytest.raises(NotFoundError):
            user_controller.update_user(1)


def test_delete_user(app, user_controller, user_service_mock):
    with app.app_context():
        response = user_controller.delete_user(1)
        user_service_mock.delete_user.assert_called_once_with(1)
        assert response == ("", 204)


def test_delete_user_no_exists(app, user_controller, user_service_mock):
    with app.app_context():
        user_service_mock.get_user_by_id.return_value = None

        with pytest.raises(NotFoundError):
            user_controller.delete_user(1)
