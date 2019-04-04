from flask import request, make_response, jsonify
from flask_restful import Resource
from Model import db, Doctor, ClinicsSchema
from classes.DatabaseFacade import DatabaseFacade
from classes.jsonResponseBuilderPattern.Response import Response
from classes.jsonResponseBuilderPattern.dataTypes.SuccessStatus import Success, Failure
from classes.jsonResponseBuilderPattern.dataTypes.Messages import InvalidLoginMessage, RegistrationCompleteMessage, UpdateCompleteMessage, NoInputMessage, CustomMessage
from classes.jsonResponseBuilderPattern.dataTypes.Data import Data

clinics_schema = ClinicsSchema(many=True)
clinic_schema = ClinicsSchema()

dbFacade = DatabaseFacade.getInstance(db)

# this file has to be correctly implemented
class ClinicsResource(Resource):

    def get(self):
        jsonRespBuilder = Response()
        doctors = dbFacade.getAll("Clinics")
        jsonRespBuilder.add(Success)
        jsonRespBuilder.add(Data(doctors))
        resp = make_response(jsonify(jsonRespBuilder.build()))
        resp.headers['Access-Control-Allow-Origin'] = '*'
        return resp
    ...