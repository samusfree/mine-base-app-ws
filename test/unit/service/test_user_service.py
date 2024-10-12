import pytest
from pytest_mock import MockerFixture

from api.model.user import User
from api.repository.user_repository import UserRepository
from api.service.user_service import UserService

pytestmark = pytest.mark.unit


@pytest.fixture
def mock_user_repository(mocker: MockerFixture):
    return mocker.Mock(spec=UserRepository)


@pytest.fixture
def user_service(mock_user_repository):
    return UserService(user_repository=mock_user_repository)


def test_get_all_users(user_service, mock_user_repository):
    mock_user_repository.get_all.return_value = [
        User(id=1, name="Test User"),
        User(id=2, name="Test User2"),
    ]

    users = user_service.get_all_users()

    assert len(users) == 2
    assert users[0].id == 1
    assert users[0].name == "Test User"
    assert users[1].id == 2
    assert users[1].name == "Test User2"
    mock_user_repository.get_all.assert_called_once()


def test_get_user_by_id(user_service, mock_user_repository):
    mock_user_repository.get_by_id.return_value = User(id=1, name="Test User")

    user = user_service.get_user_by_id(1)

    assert user.id == 1
    assert user.name == "Test User"
    mock_user_repository.get_by_id.assert_called_once_with(1)


def test_create_user(user_service, mock_user_repository):
    user_data = {"id": 1, "name": "Test User"}

    user = user_service.create_user(user_data)

    assert user.id == 1
    assert user.name == "Test User"
    mock_user_repository.add.assert_called_once()


def test_update_user(user_service, mock_user_repository):
    mock_user = User(id=1, name="Test User")
    updated_data = {"name": "Test User2"}
    mock_user_repository.get_by_id.return_value = mock_user

    updated_user = user_service.update_user(1, updated_data)

    assert updated_user.name == "Test User2"
    mock_user_repository.update.assert_called()


def test_delete_user(user_service, mock_user_repository):
    mock_user = User(id=1, name="Test User")
    mock_user_repository.get_by_id.return_value = mock_user

    user_service.delete_user(1)

    mock_user_repository.delete.assert_called_once_with(mock_user)
