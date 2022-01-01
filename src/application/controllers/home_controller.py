from flask import Blueprint, request
from flask_restful import Resource, Api
from ..middleware.auth_middleware import authMiddleware

apiHomes = Blueprint('homes_api', __name__, url_prefix='/api/v1')
api = Api(apiHomes)


class HomeController(Resource):
    def __init__(self) -> None:
        from ...infrastructure import HomeRepository
        super().__init__()
        self.homeRepository = HomeRepository()

    def get(self):
        homes = self.homeRepository.getHomes()
        return {'home': homes}

    @authMiddleware()
    def post(self):
        return 'testing'


api.add_resource(HomeController, '/homes')
