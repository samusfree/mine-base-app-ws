from dependency_injector.wiring import inject
from flask import request

from api.exception.not_found_error import NotFoundError
from ..schema.user_schema import UserSchema
from ..service.user_service import UserService


class UserController:

    @inject
    def __init__(self, user_service: UserService):
        self.user_service = user_service
        self.user_schema = UserSchema()
        self.users_schema = UserSchema(many=True)

    def get_users(self):
        users = self.user_service.get_all_users()
        return self.users_schema.jsonify(users)

    def get_user(self, user_id):
        user = self.user_service.get_user_by_id(user_id)
        if not user:
            raise NotFoundError("User not found")
        return self.user_schema.jsonify(user)

    def create_user(self):
        data = request.get_json()
        validated_data = self.user_schema.load(data)
        user = self.user_service.create_user(validated_data)
        return self.user_schema.jsonify(user), 201

    def update_user(self, user_id):
        user = self.user_service.get_user_by_id(user_id)
        if not user:
            raise NotFoundError("User not found")

        data = request.get_json()
        validated_data = self.user_schema.load(data)
        user = self.user_service.update_user(user_id, validated_data)
        return self.user_schema.jsonify(user)

    def delete_user(self, user_id):
        user = self.user_service.get_user_by_id(user_id)
        if not user:
            raise NotFoundError("User not found")

        self.user_service.delete_user(user_id)
        return "", 204
