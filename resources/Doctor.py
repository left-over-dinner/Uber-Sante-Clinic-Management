from flask import request
from flask_restful import Resource
from Model import db, Doctor, DoctorSchema

doctors_schema = DoctorSchema(many=True)
doctor_schema = DoctorSchema()


# this file has to be correctly implemented
class DoctorResource(Resource):

    def get(self):
        doctors = Doctor.query.all()
        doctors = doctors_schema.dump(doctors).data
        return {'status': 'success', 'data': doctors}, 200

    ...

    def post(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        # Validate and deserialize input
        data, errors = doctor_schema.load(json_data)
        if errors:
            return errors, 422
        doctor = Doctor.query.filter_by(permit_number=data['permit_number']).first()
        if doctor:
            return {'message': 'doctor already exists'}, 400
        doctor = Doctor(
            permit_number=json_data['permit_number'],
            last_name=json_data['last_name'],
            firs_name=json_data['firs_name'],
            speciality=json_data['speciality'],
            city=json_data['city'],
        )

        db.session.add(doctor)
        db.session.commit()

        result = doctor_schema.dump(doctor).data

        return {"status": 'success', 'data': result}, 201

