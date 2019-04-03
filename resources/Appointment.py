from flask import request, make_response, jsonify
from flask_restful import Resource
from Model import db, Appointment, AppointmentSchema
from classes.DatabaseFacade import DatabaseFacade
from classes.jsonResponseBuilderPattern.Response import Response
from classes.jsonResponseBuilderPattern.dataTypes.SuccessStatus import Success, Failure
from classes.jsonResponseBuilderPattern.dataTypes.Messages import InvalidLoginMessage, RegistrationCompleteMessage, UpdateCompleteMessage, NoInputMessage, CustomMessage
from classes.jsonResponseBuilderPattern.dataTypes.Data import Data

appointments_schema = AppointmentSchema(many=True)
appointment_schema = AppointmentSchema()

dbFacade = DatabaseFacade.getInstance(db)

# this file has to be correctly implemented
class AppointmentResource(Resource):

    def get(self):
        jsonRespBuilder = Response()
        appointments = dbFacade.getAll("Appointment")
        jsonRespBuilder.add(Success())
        jsonRespBuilder.add(Data(appointments))
        resp = make_response(jsonify(jsonRespBuilder.build()))
        resp.headers['Access-Control-Allow-Origin'] = '*'
        return resp

    ...

    def post(self):
        jsonRespBuilder = Response()
        json_data = request.get_json(force=True)
        if not json_data:
            jsonRespBuilder.add(Failure())
            jsonRespBuilder.add(NoInputMessage)
            resp = make_response(jsonify(jsonRespBuilder.build()))
            resp.headers['Access-Control-Allow-Origin'] = '*'
            return resp
        result = dbFacade.register("Appointment", json_data)
        jsonRespBuilder.add(Success())
        jsonRespBuilder.add(Data(result))
        resp = make_response(jsonify(jsonRespBuilder.build()))
        resp.headers['Access-Control-Allow-Origin'] = '*'
        return resp
    ...

    def put(self):
        jsonRespBuilder = Response()
        json_data = request.get_json(force=True)
        if not json_data:
            jsonRespBuilder.add(Failure())
            jsonRespBuilder.add(NoInputMessage)
            resp = make_response(jsonify(jsonRespBuilder.build()))
            resp.headers['Access-Control-Allow-Origin'] = '*'
            return resp
        result = dbFacade.update("Appointment", json_data)
        jsonRespBuilder.add(Success())
        jsonRespBuilder.add(Data(result))
        resp = make_response(jsonify(jsonRespBuilder.build()))
        resp.headers['Access-Control-Allow-Origin'] = '*'
        return resp

    ...

    def delete(self):
        jsonRespBuilder = Response()
        json_data = request.get_json(force=True)
        if not json_data:
            jsonRespBuilder.add(Failure())
            jsonRespBuilder.add(NoInputMessage)
            resp = make_response(jsonify(jsonRespBuilder.build()))
            resp.headers['Access-Control-Allow-Origin'] = '*'
            return resp
        result = dbFacade.remove("Appointment", json_data)
        jsonRespBuilder.add(Success())
        jsonRespBuilder.add(Data(result))
        resp = make_response(jsonify(jsonRespBuilder.build()))
        resp.headers['Access-Control-Allow-Origin'] = '*'
        return resp

