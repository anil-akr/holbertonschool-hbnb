from flask import Blueprint, request
from flask_jwt_extended import create_access_token
from app.models.user import User

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/login", methods=["POST"])
def login():

    data = request.get_json()

    user = User.query.filter_by(email=data["email"]).first()

    if not user:
        return {"error": "Invalid credentials"}, 401

    token = create_access_token(identity=user.id)

    return {"access_token": token}