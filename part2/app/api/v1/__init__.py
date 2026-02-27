from flask import Blueprint
from flask_restx import Api

# Création du Blueprint
api_v1 = Blueprint("api_v1", __name__)

# Initialisation de l'API RESTx
api = Api(
    api_v1,
    title="HBnB API",
    version="1.0",
    description="HBnB Application API - Part 2"
)

# Import des fichiers endpoints
from app.api.v1 import users
# Plus tard tu ajouteras :
# from app.api.v1 import places
# from app.api.v1 import reviews
# from app.api.v1 import amenities