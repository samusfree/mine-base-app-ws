from dependency_injector.wiring import Provide
from flask import Blueprint

from api.config.containers import APPContainer
from api.controller.user_controller import UserController

user_blueprint_v1 = Blueprint("user_bp", __name__)

user_controller: UserController = Provide[
    APPContainer.controllers.user_controller
]


@user_blueprint_v1.route("/users", methods=["GET"])
def get_users_v1():
    """
    List all users (v1)
    ---
    get:
        description: List all users
        responses:
            200:
                description: A list of users
                content:
                    application/json:
                        schema:
                            type: array
                            items: UserSchema
            500:
                description: Internal server error
        tags:
            - users
    """
    return user_controller.get_users()


@user_blueprint_v1.route("/users", methods=["POST"])
def create_user_v1():
    """
    Create a new user (v1)
    ---
    post:
        description: Create a new user
        requestBody:
            required: true
            content:
                application/json:
                    schema: UserSchema
        responses:
            201:
                description: User created
                content:
                    application/json:
                        schema: UserSchema
            400:
                description: Invalid input
            500:
                description: Internal server error
        tags:
            - users
    """
    return user_controller.create_user()


@user_blueprint_v1.route("/users/<int:user_id>", methods=["GET"])
def get_user_v1(user_id: int):
    """
    Get a user by ID (v1)
    ---
    get:
        description: Get a user by ID
        parameters:
            - in: path
              name: user_id
              required: true
              description: ID of the user
              schema:
                type: integer
        responses:
            200:
                description: A user
                content:
                    application/json:
                        schema: UserSchema
            404:
                description: User not found
            500:
                description: Internal server error
        tags:
            - users
    """
    return user_controller.get_user(user_id)


@user_blueprint_v1.route("/users/<int:user_id>", methods=["PUT"])
def update_user_v1(user_id: int):
    """
    Update a user by ID (v1)
    ---
    put:
        description: Update a user by ID
        parameters:
            - in: path
              name: user_id
              required: true
              description: ID of the user
              schema:
                type: integer
        requestBody:
            required: true
            content:
                application/json:
                    schema: UserSchema
        responses:
            200:
                description: User updated
                content:
                    application/json:
                        schema: UserSchema
            404:
                description: User not found
            500:
                description: Internal server error
        tags:
            - users
    """
    return user_controller.update_user(user_id)


@user_blueprint_v1.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user_v1(user_id: int):
    """
    Delete a user by ID (v1)
    ---
    delete:
        description: Delete a user by ID
        parameters:
            - in: path
              name: user_id
              required: true
              description: ID of the user
              schema:
                type: integer
        responses:
            204:
                description: User deleted
            404:
                description: User not found
            500:
                description: Internal server error
        tags:
            - users
    """
    return user_controller.delete_user(user_id)
