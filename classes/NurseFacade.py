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

class NurseFacade():
    instance = None
    db = None

    def __init__(self, db):
        if NurseFacade.instance != None:
            raise Exception("NurseFacade is a singleton")
        else:
            NurseFacade.db = db
            NurseFacade.instance = self

    def getInstance(db):
        if NurseFacade.instance == None:
            NurseFacade(db)
        return NurseFacade.instance

    def getAll(self):
        nurses = Nurse.query.all()
        nurses = nurses_schema.dump(nurses).data
        return nurses

    def getNursesByIdentifier(self, access_id_):
        nurse = Nurse.query.filter_by(access_id=access_id_).first()
        return nurse

    def register(self, json_data):
        # Validate and deserialize input
        data, errors = nurse_schema.load(json_data)
        if errors:
            return {'error': errors}
        nurse = Nurse.query.filter_by(access_id=data['access_id']).first()
        if nurse:
            return {'error': 'Nurse already exists'}
        nurse = AccountAdapter.createFromJSON('Nurse', json_data)
        db.session.add(nurse)
        db.session.commit()

        result = nurse_schema.dump(nurse).data
        return result

    def update(self, json_data):
        # Validate and deserialize input
        data, errors = nurse_schema.load(json_data)
        if errors:
            return {'error': errors}
        nurse = Nurse.query.filter_by(access_id=data['access_id']).first()
        if not nurse:
            return {'error': 'Category does not exist'}
        nurse = AccountAdapter.updateFromJSON('Nurse', nurse, json_data)
        db.session.commit()
        result = nurse_schema.dump(nurse).data
        return result

    def remove(self, json_data):
        # Validate and deserialize input
        data, errors = nurse_schema.load(json_data)
        if errors:
            return {'error': errors}
        nurse = Nurse.query.filter_by(access_id=data['access_id']).delete()
        db.session.commit()
        result = nurse_schema.dump(nurse).data
        return result
