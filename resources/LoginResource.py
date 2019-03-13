from flask import request, make_response, jsonify
from flask_restful import Resource
from Model import db
from Classes.DatabaseFacade import DatabaseFacade

dbFacade = DatabaseFacade.getInstance(db)




class LoginResource(Resource):

    def post(self):
        json_data = request.get_json()
        print(json_data)
        if not json_data:
            resp = make_response(jsonify({'status':'failure','message': 'No input data provided'}))
            resp.headers['Access-Control-Allow-Origin'] = '*'
            return resp

        account = dbFacade.login(json_data['type'], json_data['email'],json_data['password'])
        if 'email' not in account:
            resp = make_response(jsonify({'status': 'failure','message':'Invalid login'}))
        else:
            resp = make_response(jsonify({'status': 'success', 'data': account}))
        resp.headers['Access-Control-Allow-Origin'] = '*'
        return resp
