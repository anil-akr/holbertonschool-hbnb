from flask import request
from flask_restx import Namespace, Resource, fields
from app.services.facade import HBnBFacade

api = Namespace('amenities', description='Amenity operations')
facade = HBnBFacade()

amenity_input_model = api.model('AmenityInput', {
    'name': fields.String(required=True)
})

amenity_output_model = api.model('AmenityOutput', {
    'id': fields.String,
    'name': fields.String,
    'created_at': fields.String,
    'updated_at': fields.String
})


@api.route('/')
class AmenityList(Resource):

    @api.expect(amenity_input_model)
    @api.marshal_with(amenity_output_model, code=201)
    def post(self):
        data = request.json
        try:
            amenity = facade.create_amenity(data)
            return amenity.to_dict(), 201
        except ValueError as e:
            api.abort(400, str(e))

    @api.marshal_list_with(amenity_output_model)
    def get(self):
        amenities = facade.get_all_amenities()
        return [a.to_dict() for a in amenities], 200


@api.route('/<string:amenity_id>')
class AmenityResource(Resource):

    @api.marshal_with(amenity_output_model)
    def get(self, amenity_id):
        amenity = facade.get_amenity(amenity_id)
        if not amenity:
            api.abort(404, "Amenity not found")
        return amenity.to_dict(), 200

    @api.expect(amenity_input_model)
    @api.marshal_with(amenity_output_model)
    def put(self, amenity_id):
        data = request.json
        try:
            amenity = facade.update_amenity(amenity_id, data)
            if not amenity:
                api.abort(404, "Amenity not found")
            return amenity.to_dict(), 200
        except ValueError as e:
            api.abort(400, str(e))