from Model import db, Doctor, DoctorSchema, Nurse, NurseSchema, Patient, PatientSchema, Availability, Appointment, AppointmentSchema, AvailabilitySchema
from classes.AccountAdapter import AccountAdapter
from classes.ProxyObjectAdapter import ProxyObjectAdapter, customDateFormat, customSlotsFormat

# doctor schema
doctors_schema = DoctorSchema(many=True)
doctor_schema = DoctorSchema()
# nurse schema
nurses_schema = NurseSchema(many=True)
nurse_schema = NurseSchema()
# Patient schema
patients_schema = PatientSchema(many=True)
patient_schema = PatientSchema()
#availiblility schema
availabilityies_schema = AvailabilitySchema(many=True)
availability_schema = AvailabilitySchema()
#appointment schema
appointments_schema = AppointmentSchema(many=True)
appointment_schema = AppointmentSchema()

class AppointmentFacade():
    instance = None
    db = None

    def __init__(self, db):
        if AppointmentFacade.instance != None:
            raise Exception("AppointmentFacade is a singleton")
        else:
            AppointmentFacade.db = db
            AppointmentFacade.instance = self

    def getInstance(db):
        if AppointmentFacade.instance == None:
            AppointmentFacade(db)
        return AppointmentFacade.instance

    def getAll(self):
        result = db.engine.execute("SELECT appointment.patient_card_number, appointment.appointment_id, appointment.date, appointment.doctor_permit_number, appointment.appointment_type, appointment.slots,  patient.first_name patientFirstName,patient.last_name patientLastName,patient.phone_number patientPhone,patient.email patientEmail,patient.gender patientGender,doctor.first_name doctorFirstName,doctor.last_name doctorLastName,doctor.email doctorEmail,doctor.clinic_id FROM appointment INNER JOIN patient  ON appointment.patient_card_number = patient.card_number INNER JOIN doctor on appointment.doctor_permit_number = doctor.permit_number")
        glass = ProxyObjectAdapter.toArray(result, [customDateFormat, customSlotsFormat])
        #print(glass)
        return glass

    def getByIdentifier(self, patient_card_number_):
        availability = Appointment.query.filter_by(patient_card_number=patient_card_number_).first()
        return availability

    def register(self, json_data):
        # Validate and deserialize input
        data, errors = appointment_schema.load(json_data)
        if errors:
            return {'error': errors}
        print("FACADE DATE 1")
        print(json_data['date'])
        appointment = Appointment(
            patient_card_number=json_data['patient_card_number'],
            doctor_permit_number=json_data['doctor_permit_number'],
            date=json_data['date'],
            slots=json_data['slots'],
            appointment_type=json_data['appointment_type'],
        )
        print("FACADE DATE 2")
        print(appointment.date)
        db.session.add(appointment)
        db.session.commit()

        result = appointment_schema.dump(appointment).data

        return result

    def update(self, json_data):
        # Validate and deserialize input
        data, errors = appointment_schema.load(json_data)
        print(json_data['slots']);
        if errors:
            return {'error': errors}
        appointment = Appointment.query.filter_by(patient_card_number=data['patient_card_number']).first()
        if not appointment:
            return {'error': 'Category does not exist'}
        appointment.patient_card_number = json_data['patient_card_number'],
        appointment.doctor_permit_number = json_data['doctor_permit_number'],
        appointment.date = json_data['date'],
        appointment.appointment_type = json_data['appointment_type'],
        appointment.slots = None
        db.session.commit()

        appointment = Appointment.query.filter_by(patient_card_number=data['patient_card_number']).first()
        if not appointment:
            return {'error': 'Category does not exist'}
        appointment.patient_card_number = json_data['patient_card_number'],
        appointment.doctor_permit_number = json_data['doctor_permit_number'],
        appointment.date = json_data['date'],
        appointment.appointment_type = json_data['appointment_type'],
        appointment.slots = json_data['slots']
        db.session.commit()

        result = appointment_schema.dump(appointment).data

        return result

    def remove(self, json_data):

        # Validate and deserialize input
        data, errors = appointment_schema.load(json_data)
        if errors:
            {'error': errors}
        appointment = Appointment.query.filter_by(appointment_id=data['appointment_id']).delete()
        db.session.commit()

        result = appointment_schema.dump(appointment).data

        return result
