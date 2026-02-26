from flask import request
from flask_restx import Namespace, Resource, fields
from app.services.facade import HBnBFacade

api = Namespace('places', description='Place operations')
facade = HBnBFacade()


# ----------- MODELS (Swagger) -----------

place_input_model = api.model('PlaceInput', {
    'title': fields.String(required=True),
    'price': fields.Float(required=True),
    'owner_id': fields.String(required=True),
    'amenity_ids': fields.List(fields.String)
})

place_output_model = api.model('PlaceOutput', {
    'id': fields.String,
    'title': fields.String,
    'price': fields.Float,
    'owner_id': fields.String,
    'amenity_ids': fields.List(fields.String),
    'created_at': fields.String,
    'updated_at': fields.String
})


# ----------- ROUTES -----------

@api.route('/')
class PlaceList(Resource):

    @api.expect(place_input_model)
    @api.marshal_with(place_output_model, code=201)
    def post(self):
        """Create a new place"""
        data = request.json
        try:
            place = facade.create_place(data)
            return place.to_dict(), 201
        except ValueError as e:
            api.abort(400, str(e))

    @api.marshal_list_with(place_output_model)
    def get(self):
        """Get all places"""
        places = facade.get_all_places()
        return [p.to_dict() for p in places], 200


@api.route('/<string:place_id>')
class PlaceResource(Resource):

    @api.marshal_with(place_output_model)
    def get(self, place_id):
        """Get one place"""
        place = facade.get_place(place_id)
        if not place:
            api.abort(404, "Place not found")
        return place.to_dict(), 200

    @api.expect(place_input_model)
    @api.marshal_with(place_output_model)
    def put(self, place_id):
        """Update a place"""
        data = request.json
        try:
            place = facade.update_place(place_id, data)
            if not place:
                api.abort(404, "Place not found")
            return place.to_dict(), 200
        except ValueError as e:
            api.abort(400, str(e))