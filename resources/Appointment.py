from flask import request, make_response, jsonify
from flask_restful import Resource
from Model import db, Appointment, AppointmentSchema
from classes.DatabaseFacade import DatabaseFacade

appointments_schema = AppointmentSchema(many=True)
appointment_schema = AppointmentSchema()

dbFacade = DatabaseFacade.getInstance(db)

# this file has to be correctly implemented
class AppointmentResource(Resource):

    def get(self):
        appointments = dbFacade.getAll("Appointment")
        resp = make_response(jsonify({'status': 'success', 'data': appointments}))
        resp.headers['Access-Control-Allow-Origin'] = '*'
        return resp

    ...

    def post(self):
        json_data = request.get_json(force=True)
        if not json_data:
            resp = make_response(jsonify({'message': 'No input data provided'}))
            resp.headers['Access-Control-Allow-Origin'] = '*'
            return resp
        result = dbFacade.register("Appointment", json_data)
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
        result = dbFacade.update("Appointment", json_data)
        resp = make_response(jsonify({"status": 'success', 'data': result}))
        resp.headers['Access-Control-Allow-Origin'] = '*'
        return resp

    ...

    def delete(self):
        json_data = request.get_json(force=True)
        if not json_data:
            resp = make_response(jsonify({'message': 'No input data provided'}))
            resp.headers['Access-Control-Allow-Origin'] = '*'
            return resp
        result = dbFacade.remove("Appointment", json_data)
        resp = make_response(jsonify({"status": 'success', 'data': result}))
        resp.headers['Access-Control-Allow-Origin'] = '*'
        return resp

