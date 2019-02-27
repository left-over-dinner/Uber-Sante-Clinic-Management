from flask import request
from flask_restful import Resource
from Model import db, Nurse, NurseSchema
#
nurses_schema = NurseSchema(many=True)
nurse_schema = NurseSchema()


# this file has to be correctly implemented
class NurseResource(Resource):

    def get(self):
        nurses = Nurse.query.all()
        nurses = nurses_schema.dump(nurses).data
        return {'status': 'success', 'data': nurses}, 200

    ...

    def post(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        # Validate and deserialize input
        data, errors = nurse_schema.load(json_data)
        if errors:
            return errors, 422
        nurse = Nurse.query.filter_by(access_id=data['access_id']).first()
        if nurse:
            return {'message': 'nurse already exists'}, 400
        nurse = Nurse(
            access_id=json_data['access_id'],
            password=json_data['password'],
        )

        db.session.add(nurse)
        db.session.commit()

        result = nurse_schema.dump(nurse).data

        return {"status": 'success', 'data': result}, 201

    ...

    def put(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        # Validate and deserialize input
        data, errors = nurse_schema.load(json_data)
        if errors:
            return errors, 422
        nurse = Nurse.query.filter_by(access_id=data['access_id']).first()
        if not nurse:
            return {'message': 'Category does not exist'}, 400
        nurse.access_id = json_data['access_id'],
        nurse.password = json_data['password'],
        db.session.commit()

        result = nurse_schema.dump(nurse).data

        return {"status": 'success', 'data': result}, 204

    ...

    def delete(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        # Validate and deserialize input
        data, errors = nurse_schema.load(json_data)
        if errors:
            return errors, 422
        nurse = Nurse.query.filter_by(access_id=data['access_id']).delete()
        db.session.commit()

        result = nurse_schema.dump(nurse).data

        return {"status": 'success', 'data': result}, 204
