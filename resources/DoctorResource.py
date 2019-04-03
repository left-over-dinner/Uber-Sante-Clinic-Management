from flask import request, make_response, jsonify
from flask_restful import Resource
from Model import db, Doctor, DoctorSchema
from classes.DatabaseFacade import DatabaseFacade
from classes.jsonResponseBuilderPattern.Response import Response
from classes.jsonResponseBuilderPattern.dataTypes.SuccessStatus import Success, Failure
from classes.jsonResponseBuilderPattern.dataTypes.Messages import InvalidLoginMessage, RegistrationCompleteMessage, UpdateCompleteMessage, NoInputMessage, CustomMessage
from classes.jsonResponseBuilderPattern.dataTypes.Data import Data

doctors_schema = DoctorSchema(many=True)
doctor_schema = DoctorSchema()

dbFacade = DatabaseFacade.getInstance(db)

# this file has to be correctly implemented
class DoctorResource(Resource):

    def get(self):
        jsonRespBuilder = Response()
        doctors = dbFacade.getAll("Doctor")
        jsonRespBuilder.add(Success)
        jsonRespBuilder.add(Data(doctors))
        resp = make_response(jsonify(jsonRespBuilder.build()))
        resp.headers['Access-Control-Allow-Origin'] = '*'
        return resp
    ...

    def post(self):
        jsonRespBuilder = Response()
        json_data = request.get_json(force=True)
        if not json_data:
            jsonRespBuilder.add(Failure())
            jsonRespBuilder.add(NoInputMessage())
            resp = make_response(jsonify(jsonRespBuilder.build()))
            resp.headers['Access-Control-Allow-Origin'] = '*'
            return resp
        result = dbFacade.register("Doctor", json_data)
        if 'error' in result:
            jsonRespBuilder.add(Failure())
            jsonRespBuilder.add(CustomMessage(result))
            resp = make_response(jsonify(jsonRespBuilder.build()))
        else:
            jsonRespBuilder.add(Success())
            jsonRespBuilder.add(RegistrationCompleteMessage)
            resp = make_response(jsonify(jsonRespBuilder.build()))
        resp.headers['Access-Control-Allow-Origin'] = '*'
        return resp

    ...

    def put(self):
        jsonRespBuilder = Response()
        json_data = request.get_json(force=True)
        print(json_data)
        if not json_data:
            jsonRespBuilder.add(Failure())
            jsonRespBuilder.add(NoInputMessage())
            resp = make_response(jsonify(jsonRespBuilder.build()))
            resp.headers['Access-Control-Allow-Origin'] = '*'
            return resp
        result = dbFacade.update("Doctor", json_data)
        if 'error' in result:
            jsonRespBuilder.add(Failure())
            jsonRespBuilder.add(CustomMessage(result))
            resp = make_response(jsonify(jsonRespBuilder.build()))
        else:
            jsonRespBuilder.add(Success())
            jsonRespBuilder.add(Data(result))
            resp = make_response(jsonify(jsonRespBuilder.build()))
        resp.headers['Access-Control-Allow-Origin'] = '*'
        return resp

    ...
    #API CALL NOT IN USED FOR THE MOMENT
    #IGNORE
    def delete(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        result = dbFacade.remove("Doctor", json_data)
        if 'error' in result:
            return {"status": 'failure', 'message': result['error']}, 400
        return {"status": 'success', 'data': result}, 200

