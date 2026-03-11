from flask import Flask
from app.api.v1 import bp as api_v1_bp
from config import config


def create_app(config_name="default"):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    app.register_blueprint(api_v1_bp)
    return app