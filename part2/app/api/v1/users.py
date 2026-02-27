from flask import request
from flask_restx import Namespace, Resource, fields
from app.services.facade import HBnBFacade

api = Namespace('users', description='User operations')
facade = HBnBFacade()

user_input_model = api.model('UserInput', {
    'email': fields.String(required=True),
    'first_name': fields.String(required=True),
    'last_name': fields.String(required=True)
})

user_output_model = api.model('UserOutput', {
    'id': fields.String,
    'email': fields.String,
    'first_name': fields.String,
    'last_name': fields.String,
    'created_at': fields.String,
    'updated_at': fields.String
})


@api.route('/')
class UserList(Resource):

    @api.expect(user_input_model)
    @api.marshal_with(user_output_model, code=201)
    def post(self):
        data = request.json
        try:
            user = facade.create_user(data)
            return user.to_dict(), 201
        except ValueError as e:
            api.abort(400, str(e))

    @api.marshal_list_with(user_output_model)
    def get(self):
        users = facade.get_all_users()
        return [u.to_dict() for u in users], 200


@api.route('/<string:user_id>')
class UserResource(Resource):

    @api.marshal_with(user_output_model)
    def get(self, user_id):
        user = facade.get_user(user_id)
        if not user:
            api.abort(404, "User not found")
        return user.to_dict(), 200

    @api.expect(user_input_model)
    @api.marshal_with(user_output_model)
    def put(self, user_id):
        data = request.json
        try:
            user = facade.update_user(user_id, data)
            if not user:
                api.abort(404, "User not found")
            return user.to_dict(), 200
        except ValueError as e:
            api.abort(400, str(e))