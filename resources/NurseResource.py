from flask import request
from flask_restful import Resource
from Model import db, Nurse, NurseSchema
from classes.DatabaseFacade import DatabaseFacade
#
nurses_schema = NurseSchema(many=True)
nurse_schema = NurseSchema()

dbFacade = DatabaseFacade.getInstance(db)

# this file has to be correctly implemented
class NurseResource(Resource):

    def get(self):
        nurses = dbFacade.getNurses()
        return {'status': 'success', 'data': nurses}, 200

    ...

    def post(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        result = dbFacade.registerNurse(json_data)
        if 'error' in result:
            return {"status": 'failure', 'message': result['error']}, 400
        return {"status": 'success', 'data': result}, 201

    ...

    def put(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        result = dbFacade.updateNurse(json_data)
        if 'error' in result:
            return {"status": 'failure', 'message': result['error']}, 400
        return {"status": 'success', 'data': result}, 200

    ...

    def delete(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        result = dbFacade.removeNurse(json_data)
        if 'error' in result:
            return {"status": 'failure', 'message': result['error']}, 400
        return {"status": 'success', 'data': result}, 200

