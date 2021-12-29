from flask import Flask

from .controllers import apiHomes


def register_blueprints(app, *args):
    for module in args:
        app.register_blueprint(module)


app = Flask(__name__)

register_blueprints(app, apiHomes)
