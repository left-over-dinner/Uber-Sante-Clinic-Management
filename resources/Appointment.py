from flask import request
from flask_restful import Resource
from Model import db, Appointment, AppointmentSchema

appointments_schema = AppointmentSchema(many=True)
appointment_schema = AppointmentSchema()


# this file has to be correctly implemented
class AppointmentResource(Resource):

    def get(self):
        appointments = Appointment.query.all()
        appointments = appointments_schema.dump(appointments).data
        return {'status': 'success', 'data': appointments}, 200

    ...

    def post(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        # Validate and deserialize input
        data, errors = appointment_schema.load(json_data)
        if errors:
            return errors, 422
        appointment = Appointment(
            patient_card_number=json_data['patient_card_number'],
            doctor_permit_number=json_data['doctor_permit_number'],
            date=json_data['date'],
            slots=json_data['slots'],
            appointment_type=json_data['appointment_type'],
        )

        db.session.add(appointment)
        db.session.commit()

        result = appointment_schema.dump(appointment).data

        return {"status": 'success', 'data': result}, 201
    ...

    def put(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        # Validate and deserialize input
        data, errors = appointment_schema.load(json_data)
        if errors:
            return errors, 422
        appointment = Appointment.query.filter_by(patient_card_number=data['patient_card_number']).first()
        if not appointment:
            return {'message': 'Category does not exist'}, 400
        appointment.patient_card_number = json_data['patient_card_number'],
        appointment.doctor_permit_number = json_data['doctor_permit_number'],
        appointment.date = json_data['date'],
        appointment.slots = json_data['slots'],
        appointment.appointment_type = json_data['appointment_type'],
        db.session.commit()

        result = appointment_schema.dump(appointment).data

        return {"status": 'success', 'data': result}, 204

    ...

    def delete(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        # Validate and deserialize input
        data, errors = appointment_schema.load(json_data)
        if errors:
            return errors, 422
        appointment = Appointment.query.filter_by(appointment_id=data['appointment_id']).delete()
        db.session.commit()

        result = appointment_schema.dump(appointment).data

        return {"status": 'success', 'data': result}, 204

