from Model import db, Doctor, DoctorSchema, Nurse, NurseSchema, Patient, PatientSchema, Availability, Appointment, AppointmentSchema, AvailabilitySchema
from classes.AccountAdapter import AccountAdapter

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

class PatientFacade():
    instance = None
    db = None

    def __init__(self, db):
        if PatientFacade.instance != None:
            raise Exception("PatientFacade is a singleton")
        else:
            PatientFacade.db = db
            PatientFacade.instance = self

    def getInstance(db):
        if PatientFacade.instance == None:
            PatientFacade(db)
        return PatientFacade.instance

    def getAll(self):
        patients = Patient.query.all()
        patients = patients_schema.dump(patients).data
        return patients

    def getPatientsByIdentifier(self, card_number_):
        patient = Patient.query.filter_by(card_number=card_number_).first()
        return patient

    def register(self, json_data):
        # Validate and deserialize input
        data, errors = patient_schema.load(json_data)
        if errors:
            return {'error': errors}
        patient = Patient.query.filter_by(card_number=data['card_number']).first()
        if patient:
            return {'error': 'Patient already exists'}
        patient = AccountAdapter.createFromJSON('Patient', json_data)
        db.session.add(patient)
        db.session.commit()

        result = patient_schema.dump(patient).data
        return result

    def update(self, json_data):
        # Validate and deserialize input
        data, errors = patient_schema.load(json_data)
        if errors:
            return {'error': errors}
        patient = Patient.query.filter_by(card_number=data['card_number']).first()
        if not patient:
            return {'error': 'Category does not exist'}
        patient = AccountAdapter.updateFromJSON(patient, json_data)
        db.session.commit()
        result = patient_schema.dump(patient).data
        return result

    def remove(self, json_data):
        # Validate and deserialize input
        data, errors = patient_schema.load(json_data)
        if errors:
            return {'error': errors}
        patient = Patient.query.filter_by(card_number=data['card_number']).delete()
        db.session.commit()
        result = patient_schema.dump(patient).data
        return result
