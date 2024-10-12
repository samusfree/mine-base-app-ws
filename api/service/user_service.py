from dependency_injector.wiring import inject

from api.repository.user_repository import UserRepository

from ..model.user import User


class UserService:
    """User service class"""

    @inject
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def get_all_users(self):
        """Get all users"""
        return self.user_repository.get_all()

    def get_user_by_id(self, user_id):
        """Get user by id"""
        return self.user_repository.get_by_id(user_id)

    def create_user(self, data):
        """Create user"""
        user = User(**data)
        self.user_repository.add(user)
        return user

    def update_user(self, user_id, data):
        """Update user"""
        user = self.get_user_by_id(user_id)
        for key, value in data.items():
            setattr(user, key, value)
        self.user_repository.update()
        return user

    def delete_user(self, user_id):
        """Delete user"""
        user = self.get_user_by_id(user_id)
        self.user_repository.delete(user)
