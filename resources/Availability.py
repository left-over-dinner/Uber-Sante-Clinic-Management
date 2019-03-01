from flask import request
from flask_restful import Resource
from Model import db, Availability, AvailabilitySchema
from Classes.DatabaseFacade import DatabaseFacade

availabilitys_schema = AvailabilitySchema(many=True)
availability_schema = AvailabilitySchema()

dbFacade = DatabaseFacade.getInstance(db)

# this file has to be correctly implemented
class AvailabilityResource(Resource):

    def get(self):
        availabilities = dbFacade.getAvailibilities()
        return {'status': 'success', 'data': availabilities}, 200

    ...

    def post(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        result = dbFacade.registerAvailability(json_data)
        return {"status": 'success', 'data': result}, 201
    ...

    def put(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        # Validate and deserialize input
        result = dbFacade.updateAvailability(json_data)

        return {"status": 'success', 'data': result}, 204

    ...

    def delete(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        # Validate and deserialize input

        result = dbFacade.registerAvailability(json_data)

        return {"status": 'success', 'data': result}, 204


