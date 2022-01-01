# from ..handlers.user_handler import UserHandler
from flask import Blueprint, request
from flask_restful import Resource, Api

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
        return {'user': 'new user'}


api.add_resource(UserController, '/users')
