from flask import request, make_response, jsonify
from flask_restful import Resource
from Model import db, Patient, PatientSchema
from classes.DatabaseFacade import DatabaseFacade
from classes.jsonResponseBuilderPattern.Response import Response
from classes.jsonResponseBuilderPattern.dataTypes.SuccessStatus import Success, Failure
from classes.jsonResponseBuilderPattern.dataTypes.Messages import InvalidLoginMessage, RegistrationCompleteMessage, UpdateCompleteMessage, NoInputMessage, CustomMessage
from classes.jsonResponseBuilderPattern.dataTypes.Data import Data

patients_schema = PatientSchema(many=True)
patient_schema = PatientSchema()

dbFacade = DatabaseFacade.getInstance(db)

# this file has to be correctly implemented
class PatientResource(Resource):

    def get(self):
        #Response Buidler
        jsonRespBuilder = Response()
        patients = dbFacade.getAll("Patient")
        jsonRespBuilder.add(Success())
        jsonRespBuilder.add(Data(patients))
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
        result = dbFacade.register("Patient", json_data)
        if 'error' in result:
            jsonRespBuilder.add(Failure())
            jsonRespBuilder.add(CustomMessage(result))
            resp = make_response(jsonify(jsonRespBuilder.build()))
        else:
            jsonRespBuilder.add(Success)
            jsonRespBuilder.add(RegistrationCompleteMessage)
            resp = make_response(jsonify(jsonRespBuilder.build()))
        resp.headers['Access-Control-Allow-Origin'] = '*'
        return resp

    ...

    def put(self):
        jsonRespBuilder = Response()
        json_data = request.get_json(force=True)
        if not json_data:
            jsonRespBuilder.add(Failure())
            jsonRespBuilder.add(NoInputMessage())
            resp = make_response(jsonify(jsonRespBuilder.build()))
            resp.headers['Access-Control-Allow-Origin'] = '*'
            return resp
        result = dbFacade.update("Patient", json_data)
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
        jsonRespBuilder = Response()
        json_data = request.get_json(force=True)
        if not json_data:
            jsonRespBuilder.add(Failure())
            jsonRespBuilder.add(NoInputMessage())
            return {'message': 'No input data provided'}, 400
        result = dbFacade.remove("Patient", json_data)
        if 'error' in result:
            return {"status": 'failure', 'message': result['error']}, 400
        return {"status": 'success', 'data': result}, 200

