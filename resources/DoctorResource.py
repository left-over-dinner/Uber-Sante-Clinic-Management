from flask import request, make_response, jsonify
from flask_restful import Resource
from Model import db, Doctor, DoctorSchema
from Classes.DatabaseFacade import DatabaseFacade

doctors_schema = DoctorSchema(many=True)
doctor_schema = DoctorSchema()

dbFacade = DatabaseFacade.getInstance(db)

# this file has to be correctly implemented
class DoctorResource(Resource):

    def get(self):
        doctors = dbFacade.getDoctors()
        return {'status': 'success', 'data': doctors}, 200
    ...

    def post(self):
        json_data = request.get_json(force=True)
        if not json_data:
            resp = make_response(jsonify({'status': 'failure', 'message': 'No input data provided'}))
            resp.headers['Access-Control-Allow-Origin'] = '*'
            return resp
        result = dbFacade.registerDoctor(json_data)
        if 'error' in result:
            resp = make_response(jsonify({'status': 'failure', 'message': result}))
        else:
            resp = make_response(jsonify({'status': 'success', 'message': 'Registration Complete'}))
        resp.headers['Access-Control-Allow-Origin'] = '*'
        return resp

    ...

    def put(self):
        json_data = request.get_json(force=True)
        print(json_data)
        if not json_data:
            resp = make_response(jsonify({'status': 'failure', 'message': 'No input data provided'}))
            resp.headers['Access-Control-Allow-Origin'] = '*'
            return resp
        result = dbFacade.updateDoctor(json_data)
        if 'error' in result:
            resp = make_response(jsonify({'status': 'failure', 'message': result}))
        else:
            resp = make_response(jsonify({'status': 'success', 'message': 'Update Complete'}))
        resp.headers['Access-Control-Allow-Origin'] = '*'
        return resp

    ...

    def delete(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        result = dbFacade.removeDoctor(json_data)
        if 'error' in result:
            return {"status": 'failure', 'message': result['error']}, 400
        return {"status": 'success', 'data': result}, 200

