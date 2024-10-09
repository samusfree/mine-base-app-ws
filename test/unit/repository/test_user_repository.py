import pytest
from api.model.user import User
from api.repository.user_repository import UserRepository

pytestmark = pytest.mark.unit


@pytest.fixture
def user_repository():
    return UserRepository()


def test_get_all_users(app, user_repository, mocker):
    with app.app_context():
        scalars_mock = mocker.Mock()
        scalars_mock.all = mocker.Mock(
            return_value=[
                User(name="Test", lastname="User", born="1990-01-01")
            ]
        )
        session_mock = mocker.Mock()
        session_mock.scalars = mocker.Mock(return_value=scalars_mock)
        mocker.patch(
            "api.repository.user_repository.db.session",
            session_mock,
        )

        users = user_repository.get_all()

        assert len(users) == 1
        assert users[0].name == "Test"
        assert users[0].lastname == "User"
        assert users[0].born == "1990-01-01"


def test_get_user_by_id(app, user_repository, mocker):
    with app.app_context():
        mocker.patch(
            "api.repository.user_repository.db.session.get",
            return_value=User(
                name="Test", lastname="User", born="1990-01-01"
            ),
        )

        user = user_repository.get_by_id(1)

        assert user.name == "Test"
        assert user.lastname == "User"
        assert user.born == "1990-01-01"


def test_create_user(app, user_repository, mocker):
    with app.app_context():
        mock_add = mocker.patch(
            "api.repository.user_repository.db.session.add"
        )
        mock_commit = mocker.patch(
            "api.repository.user_repository.db.session.commit"
        )
        data = {"name": "Test", "lastname": "User", "born": "1990-01-01"}

        user_repository.add(data)

        mock_add.assert_called_once()
        mock_commit.assert_called_once()


def test_update_user(app, user_repository, mocker):
    with app.app_context():
        mock_commit = mocker.patch(
            "api.repository.user_repository.db.session.commit"
        )

        user_repository.update()

        mock_commit.assert_called_once()


def test_delete_user(app, user_repository, mocker):
    with app.app_context():
        mock_delete = mocker.patch(
            "api.repository.user_repository.db.session.delete"
        )
        mock_commit = mocker.patch(
            "api.repository.user_repository.db.session.commit"
        )

        user_repository.delete(
            User(name="Test", lastname="User", born="1990-01-01")
        )

        mock_delete.assert_called_once()
        mock_commit.assert_called_once()
