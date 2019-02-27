from flask import request
from flask_restful import Resource
from Model import db, Patient, PatientSchema

patients_schema = PatientSchema(many=True)
patient_schema = PatientSchema()


# this file has to be correctly implemented
class PatientResource(Resource):

    def get(self):
        patients = Patient.query.all()
        patients = patients_schema.dump(patients).data
        return {'status': 'success', 'data': patients}, 200

    ...

    def post(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        # Validate and deserialize input
        data, errors = patient_schema.load(json_data)
        if errors:
            return errors, 422
        patient = Patient.query.filter_by(card_number=data['card_number']).first()
        if patient:
            return {'message': 'patient already exists'}, 400
        patient = Patient(
            card_number=json_data['card_number'],
            birth_day=json_data['birth_day'],
            gender=json_data['gender'],
            phone_number=json_data['phone_number'],
            address=json_data['address'],
            email=json_data['email']
        )

        db.session.add(patient)
        db.session.commit()

        result = patient_schema.dump(patient).data

        return {"status": 'success', 'data': result}, 201

    ...

    def put(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        # Validate and deserialize input
        data, errors = patient_schema.load(json_data)
        if errors:
            return errors, 422
        patient = Patient.query.filter_by(card_number=data['card_number']).first()
        if not patient:
            return {'message': 'Patient does not exist'}, 400
        patient.card_number = json_data['card_number'],
        patient.birth_day = json_data['birth_day'],
        patient.gender = json_data['gender'],
        patient.phone_number = json_data['phone_number'],
        patient.address = json_data['address'],
        patient.email = json_data['email']

        db.session.commit()

        one = patient_schema.dump(patient).data

        print(one)

        return {"status": 'success', 'data': one}, 204

    ...

    def delete(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        # Validate and deserialize input
        data, errors = patient_schema.load(json_data)
        if errors:
            return errors, 422
        patient = Patient.query.filter_by(card_number=data['card_number']).delete()

        db.session.commit()

        result = patient_schema.dump(patient).data

        return {"status": 'success', 'data': result}, 204
