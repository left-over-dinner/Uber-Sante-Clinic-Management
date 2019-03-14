from flask import request, make_response, jsonify
from flask_restful import Resource
from Model import db, Availability, AvailabilitySchema
from classes.DatabaseFacade import DatabaseFacade

availabilitys_schema = AvailabilitySchema(many=True)
availability_schema = AvailabilitySchema()

dbFacade = DatabaseFacade.getInstance(db)

# this file has to be correctly implemented
class AvailabilityResource(Resource):

    def get(self):
        availabilities = dbFacade.getAvailibilities()
        resp = make_response(jsonify({'status': 'success', 'data': availabilities}))
        resp.headers['Access-Control-Allow-Origin'] = '*'
        return resp

    ...

    def post(self):
        json_data = request.get_json(force=True)
        if not json_data:
            resp = make_response(jsonify({'message': 'No input data provided'}))
            resp.headers['Access-Control-Allow-Origin'] = '*'
            return resp
        result = dbFacade.registerAvailability(json_data)
        resp = make_response(jsonify({"status": 'success', 'data': result}))
        resp.headers['Access-Control-Allow-Origin'] = '*'
        return resp

    ...

    def put(self):
        json_data = request.get_json(force=True)
        if not json_data:
            resp = make_response(jsonify({'message': 'No input data provided'}))
            resp.headers['Access-Control-Allow-Origin'] = '*'
            return resp
        # Validate and deserialize input
        result = dbFacade.updateAvailibility(json_data)
        resp = make_response(jsonify({"status": 'success', 'data': result}))
        resp.headers['Access-Control-Allow-Origin'] = '*'
        return resp

    ...

    def delete(self):
        json_data = request.get_json(force=True)
        print(json_data)
        if not json_data:
<<<<<<< HEAD
            resp = make_response(jsonify({'message': 'No input data provided'}))
            resp.headers['Access-Control-Allow-Origin'] = '*'
            return resp
        # Validate and deserialize input

        result = dbFacade.removeAvailability(json_data)
        resp = make_response(jsonify({"status": 'success', 'data': result}))
        resp.headers['Access-Control-Allow-Origin'] = '*'
        return resp
=======
            return {'message': 'No input data provided'}
        # Validate and deserialize input

        result = dbFacade.removeAvailability(json_data)

        return {"status": 'success', 'data': result}
>>>>>>> master


