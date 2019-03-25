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

class DoctorFacade():
    instance = None
    db = None

    def __init__(self, db):
        if DoctorFacade.instance != None:
            raise Exception("DoctorFacade is a singleton")
        else:
            DoctorFacade.db = db
            DoctorFacade.instance = self

    def getInstance(db):
        if DoctorFacade.instance == None:
            DoctorFacade(db)
        return DoctorFacade.instance

    def getAll(self):
        doctors = Doctor.query.all()
        doctors = doctors_schema.dump(doctors).data
        return doctors

    def getDoctorsByIdentifier(self, permit_number_):
        doctor = Doctor.query.filter_by(permit_number=permit_number_).first()
        return doctor

    def register(self, json_data):
        # Validate and deserialize input
        data, errors = doctor_schema.load(json_data)
        if errors:
            return {'error': errors}
        doctor = Doctor.query.filter_by(permit_number=data['permit_number']).first()
        if doctor:
            return {'error': 'doctor already exists'}
        doctor = AccountAdapter.createFromJSON('Doctor', json_data)
        db.session.add(doctor)
        db.session.commit()

        result = doctor_schema.dump(doctor).data
        return result

    def update(self, json_data):
        # Validate and deserialize input
        data, errors = doctor_schema.load(json_data)
        if errors:
            return {'error': errors}
        doctor = Doctor.query.filter_by(permit_number=data['permit_number']).first()
        if not doctor:
            return {'error': 'Category does not exist'}
        doctor = AccountAdapter.updateFromJSON('Doctor', doctor, json_data)
        db.session.commit()
        result = doctor_schema.dump(doctor).data
        return result

    def remove(self, json_data):
        # Validate and deserialize input
        data, errors = doctor_schema.load(json_data)
        if errors:
            return {'error': errors}
        doctor = Doctor.query.filter_by(permit_number=data['permit_number']).delete()
        db.session.commit()
        result = doctor_schema.dump(doctor).data
        return result
