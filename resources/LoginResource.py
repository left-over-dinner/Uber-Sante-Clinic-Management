from flask import request, make_response, jsonify
from flask_restful import Resource
from Model import db
from classes.DatabaseFacade import DatabaseFacade
from classes.jsonResponseBuilderPattern.Response import Response
from classes.jsonResponseBuilderPattern.dataTypes.SuccessStatus import Success, Failure
from classes.jsonResponseBuilderPattern.dataTypes.Messages import InvalidLoginMessage, RegistrationCompleteMessage, UpdateCompleteMessage, NoInputMessage, CustomMessage
from classes.jsonResponseBuilderPattern.dataTypes.Data import Data

dbFacade = DatabaseFacade.getInstance(db)

class LoginResource(Resource):

    def post(self):
        #received data from cleint
        json_data = request.get_json()
        print(json_data)
        #Responsoe Builder
        jsonRespBuiler = Response()
        if not json_data:
            # No data received from client
            jsonRespBuiler.add(Failure())
            jsonRespBuiler.add(NoInputMessage)
            resp = make_response(jsonify(jsonRespBuiler.build()))
            resp.headers['Access-Control-Allow-Origin'] = '*'
            return resp
        #perform login using database
        account = dbFacade.login(json_data['type'], json_data['email'],json_data['password'])
        if 'email' not in account:
            #invalid login
            jsonRespBuiler.add(Failure())
            jsonRespBuiler.add(InvalidLoginMessage)
            resp = make_response(jsonify(jsonRespBuiler.build()))
        else:
            #Login successfull
            jsonRespBuiler.add(Success())
            jsonRespBuiler.add(Data(account))
            resp = make_response(jsonify(jsonRespBuiler.build()))
        resp.headers['Access-Control-Allow-Origin'] = '*'
        return resp
