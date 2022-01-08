# from ..handlers.user_handler import UserHandler
from flask import Blueprint, request
from marshmallow.fields import Str
from werkzeug.exceptions import BadRequest
from flask_restful import Resource, Api
from ..models.user.create_user_request import CreateUserRequest
import uuid

apiUsers = Blueprint('users_api', __name__, url_prefix='/api/v1')
api = Api(apiUsers)


class UserController(Resource):
    def __init__(self) -> None:
        from ...infrastructure import UserRepository
        super().__init__()
        self.userRepository = UserRepository()

    def get(self):
        users = self.userRepository.getUsers()
        return {'users': users}

    def post(self):
        createUserRequest = CreateUserRequest()
        errors = createUserRequest.validate(request.get_json())
        if errors:
            raise BadRequest()
        reqBody = request.get_json()
        # print(firstname)
        newUser = self.userRepository.createUser(reqBody)
        return {'user': 'new user'}


api.add_resource(UserController, '/users')
