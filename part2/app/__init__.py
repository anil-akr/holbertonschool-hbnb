from flask import Flask
from app.api.v1 import bp as api_v1_bp


def create_app():
    app = Flask(__name__)
    app.register_blueprint(api_v1_bp)
    return app