from flask import Blueprint
from dependency_injector.wiring import Provide
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
                items:
                  type: object
                  properties:
                    id:
                      type: integer
                    name:
                      type: string
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
            schema:
              type: object
              properties:
                name:
                  type: string
      responses:
        200:
          description: User created
        400:
            Invalid data
        404:
            user not found
        500:
            Internal server error
    """
    return user_controller.create_user()


@user_blueprint_v1.route("/users/<int:user_id>", methods=["GET"])
def get_user_v1(user_id: int):
    """
    Fetch a user given its identifier (v1)
    ---
    get:
      description: Fetch a user by ID
      parameters:
        - in: path
          name: user_id
          schema:
            type: integer
          required: true
          description: The user ID
      responses:
        200:
          description: A user object
          content:
            application/json:
              schema:
                type: object
                properties:
                    id:
                        type: integer
                    name:
                        type: string
                    lastname:
                        type: string
                    born:
                        type: date
        404:
            user not found
        500:
            Internal server error
    """
    return user_controller.get_user(user_id)


@user_blueprint_v1.route("/users/<int:user_id>", methods=["PUT"])
def update_user_v1(user_id: int):
    """
    Update a user given its identifier (v1)
    ---
    put:
      description: Update a user by ID
      parameters:
        - in: path
          name: user_id
          schema:
            type: integer
          required: true
          description: The user ID
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                name:
                  type: string
      responses:
        200:
            description: User updated
        400:
            Invalid data
        404:
            user not found
        500:
            Internal server error
    """
    return user_controller.update_user(user_id)


@user_blueprint_v1.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user_v1(user_id: int):
    """
    Delete a user given its identifier (v1)
    ---
    delete:
      description: Delete a user by ID
      parameters:
        - in: path
          name: user_id
          schema:
            type: integer
          required: true
          description: The user ID
      responses:
        204:
            description: User deleted
        404:
            user not found
        500:
            Internal server error
    """
    return user_controller.delete_user(user_id)
