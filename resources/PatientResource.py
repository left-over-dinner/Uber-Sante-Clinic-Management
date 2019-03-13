from flask import request, make_response, jsonify
from flask_restful import Resource
from Model import db, Patient, PatientSchema
from Classes.DatabaseFacade import DatabaseFacade

patients_schema = PatientSchema(many=True)
patient_schema = PatientSchema()

dbFacade = DatabaseFacade.getInstance(db)

# this file has to be correctly implemented
class PatientResource(Resource):

    def get(self):
        patients = dbFacade.getPatients()
        return {'status': 'success', 'data': patients}, 200

    ...

    def post(self):
        json_data = request.get_json(force=True)
        if not json_data:
            resp = make_response(jsonify({'status': 'failure', 'message': 'No input data provided'}))
            resp.headers['Access-Control-Allow-Origin'] = '*'
            return resp
        result = dbFacade.registerPatient(json_data)
        if 'error' in result:
            resp = make_response(jsonify({'status': 'failure', 'message': result}))
        else:
            resp = make_response(jsonify({'status': 'success', 'message': 'Registration Complete'}))
        resp.headers['Access-Control-Allow-Origin'] = '*'
        return resp

    ...

    def put(self):
        json_data = request.get_json(force=True)
        if not json_data:
            resp = make_response(jsonify({'status': 'failure', 'message': 'No input data provided'}))
            resp.headers['Access-Control-Allow-Origin'] = '*'
            return resp
        result = dbFacade.updatePatient(json_data)
        if 'error' in result:
            resp = make_response(jsonify({'status': 'failure', 'message': result}))
        else:
            resp = make_response(jsonify({'status': 'success', 'message': 'Registration Complete'}))
        resp.headers['Access-Control-Allow-Origin'] = '*'
        return resp

    ...

    def delete(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        result = dbFacade.removePatient(json_data)
        if 'error' in result:
            return {"status": 'failure', 'message': result['error']}, 400
        return {"status": 'success', 'data': result}, 200

