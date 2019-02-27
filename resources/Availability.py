from flask import request
from flask_restful import Resource
from Model import db, Availability, AvailabilitySchema

availabilitys_schema = AvailabilitySchema(many=True)
availability_schema = AvailabilitySchema()


# this file has to be correctly implemented
class AvailabilityResource(Resource):

    def get(self):
        availabilitys = Availability.query.all()
        availabilitys = availabilitys_schema.dump(availabilitys).data
        return {'status': 'success', 'data': availabilitys}, 200

    ...

    def post(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        # Validate and deserialize input
        data, errors = availability_schema.load(json_data)
        if errors:
            return errors, 422
        availability = Availability(
            availability_id=json_data['availability_id'],
            doctor_permit_number=json_data['doctor_permit_number'],
            date=json_data['date'],
            slots=json_data['slots'],

        )

        db.session.add(availability)
        db.session.commit()

        result = availability_schema.dump(availability).data

        return {"status": 'success', 'data': result}, 201
    ...

    def put(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        # Validate and deserialize input
        data, errors = availability_schema.load(json_data)
        if errors:
            return errors, 422
        availability = Availability.query.filter_by(availability_id=data['availability_id']).first()
        if not availability:
            return {'message': 'Category does not exist'}, 400
        availability.doctor_permit_number = json_data['doctor_permit_number'],
        availability.date = json_data['date'],
        availability.slots = json_data['slots'],
        db.session.commit()

        result = availability_schema.dump(availability).data

        return {"status": 'success', 'data': result}, 204

    ...

    def delete(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        # Validate and deserialize input
        data, errors = availability_schema.load(json_data)
        if errors:
            return errors, 422
        availability = Availability.query.filter_by(availability_id=data['availability_id']).delete()
        db.session.commit()

        result = availability_schema.dump(availability).data

        return {"status": 'success', 'data': result}, 204


