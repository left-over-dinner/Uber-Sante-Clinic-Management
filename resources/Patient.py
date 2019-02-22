from flask import request
from flask_restful import Resource
from Model import db, Patient, PatientSchema

patients_schema = PatientSchema(many=True)
patient_schema = PatientSchema()

# this file has to be correctly implemented
class CategoryResource(Resource):

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
        patient = Patient.query.filter_by(name=data['name']).first()
        if Patient:
            return {'message': 'patient already exists'}, 400
        patient = Patient(
            name=json_data['name']
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
            patient = Patient.query.filter_by(id=data['id']).first()
        if not patient:
            return {'message': 'patient does not exist'}, 400
            patient.name = data['name']
        db.session.commit()

        result = patient_schema.dump(patient).data

        return { "status": 'success', 'data': result }, 204

    ...

    def delete(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        # Validate and deserialize input
        data, errors = patient_schema.load(json_data)
        if errors:
            return errors, 422
        patient = Patient.query.filter_by(id=data['id']).delete()
        db.session.commit()

        result = patient_schema.dump(patient).data

        return {"status": 'success', 'data': result}, 204
