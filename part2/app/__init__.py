from flask import Flask
from flask_restx import Api


def create_app():
    app = Flask(__name__)
    api = Api(app, version='1.0', title='HBnB API',
              description='HBnB Application API')
    return app

from app.api.v1 import api_v1
app.register_blueprint(api_v1, url_prefix="/api/v1")