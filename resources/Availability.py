from flask import request, make_response, jsonify
from flask_restful import Resource
from Model import db, Availability, AvailabilitySchema
from classes.DatabaseFacade import DatabaseFacade
from classes.jsonResponseBuilderPattern.Response import Response
from classes.jsonResponseBuilderPattern.dataTypes.SuccessStatus import Success, Failure
from classes.jsonResponseBuilderPattern.dataTypes.Messages import InvalidLoginMessage, RegistrationCompleteMessage, UpdateCompleteMessage, NoInputMessage, CustomMessage
from classes.jsonResponseBuilderPattern.dataTypes.Data import Data

availabilitys_schema = AvailabilitySchema(many=True)
availability_schema = AvailabilitySchema()

dbFacade = DatabaseFacade.getInstance(db)

# this file has to be correctly implemented
class AvailabilityResource(Resource):

    def get(self):
        jsonRespBuilder = Response()
        availabilities = dbFacade.getAll("Availability")
        jsonRespBuilder.add(Success())
        jsonRespBuilder.add(Data(availabilities))
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
        result = dbFacade.register("Availability", json_data)
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
            jsonRespBuilder.add(NoInputMessage())
            resp = make_response(jsonify(jsonRespBuilder.build()))
            resp.headers['Access-Control-Allow-Origin'] = '*'
            return resp
        # Validate and deserialize input
        result = dbFacade.update("Availability", json_data)
        jsonRespBuilder.add(Success())
        jsonRespBuilder.add(Data(result))
        resp = make_response(jsonify(jsonRespBuilder.build()))
        resp.headers['Access-Control-Allow-Origin'] = '*'
        return resp

    ...

    def delete(self):
        jsonRespBuilder = Response()
        json_data = request.get_json(force=True)
        print(json_data)
        if not json_data:
            jsonRespBuilder.add(Failure())
            jsonRespBuilder.add(NoInputMessage())
            resp = make_response(jsonify(jsonRespBuilder.build()))
            resp.headers['Access-Control-Allow-Origin'] = '*'
            return resp
        # Validate and deserialize input
        result = dbFacade.remove("Availability", json_data)
        jsonRespBuilder.add(Success())
        jsonRespBuilder.add(Data(result))
        resp = make_response(jsonify(jsonRespBuilder.build()))
        resp.headers['Access-Control-Allow-Origin'] = '*'
        return resp



