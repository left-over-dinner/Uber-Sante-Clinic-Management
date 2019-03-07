from flask import request
from flask_restful import Resource
from Model import db, Appointment, AppointmentSchema
from Classes.DatabaseFacade import DatabaseFacade

appointments_schema = AppointmentSchema(many=True)
appointment_schema = AppointmentSchema()

dbFacade = DatabaseFacade.getInstance(db)

# this file has to be correctly implemented
class AppointmentResource(Resource):

    def get(self):
        appointments = dbFacade.getAppointments()
        return {'status': 'success', 'data': appointments}, 200

    ...

    def post(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        result = dbFacade.registerAppointment(json_data)
        return {"status": 'success', 'data': result}, 201
    ...

    def put(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400

        result = dbFacade.updateAappointment(json_data)

        return {"status": 'success', 'data': result}, 204

    ...

    def delete(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        result = dbFacade.removeAppointemt(json_data)

        return {"status": 'success', 'data': result}, 204

