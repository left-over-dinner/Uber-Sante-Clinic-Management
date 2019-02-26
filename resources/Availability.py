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

