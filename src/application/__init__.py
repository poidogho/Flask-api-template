from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from ..config import Config
from .controllers import apiHomes
from .controllers.user_controller import apiUsers


def register_blueprints(app, *args):
    for module in args:
        app.register_blueprint(module)


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = Config.POSTGRES_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
JWTManager(app)
db.init_app(app)

register_blueprints(app, apiHomes, apiUsers)
