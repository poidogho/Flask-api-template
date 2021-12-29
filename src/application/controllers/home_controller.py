from flask import Blueprint, request
from flask_restful import Resource, Api
from ..models import CreateHomeRequest
from ..handlers import HomeHandler

apiHomes = Blueprint('homes_api', __name__, url_prefix='/api/v1')
api = Api(apiHomes)


class HomeController(Resource):
    def __init__(self, homeHandler: HomeHandler) -> None:
        super().__init__()
        self.homeHandler = homeHandler

    def get(self, name):
        creatHomeReq = CreateHomeRequest()
        errors = creatHomeReq.validate(request.form)
        if errors:
            return {'errors': errors}, 400
        return {'home': name}


api.add_resource(HomeController, '/homes/<string:name>')
