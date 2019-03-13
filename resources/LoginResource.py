from flask import request
from flask_restful import Resource
from Model import db
from classes.DatabaseFacade import DatabaseFacade

dbFacade = DatabaseFacade.getInstance(db)




class LoginResource(Resource):

    def post(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'status':'failure','message': 'No input data provided'}, 400
        account = dbFacade.login(json_data['type'], json_data['email'],json_data['password'])
        if 'email' not in account:
            return {'status': 'failure','message':'Invalid login'}, 400
        return {'status': 'success', 'data': account}, 200