from Model import db, Doctor, DoctorSchema, Nurse, NurseSchema, Patient, PatientSchema
from Classes.AccountAdapter import AccountAdapter

# doctor schema
doctors_schema = DoctorSchema(many=True)
doctor_schema = DoctorSchema()
# nurse schema
nurses_schema = NurseSchema(many=True)
nurse_schema = NurseSchema()
# Patient schema
patients_schema = PatientSchema(many=True)
patient_schema = PatientSchema()


# follow the singleton patter https://www.tutorialspoint.com/python_design_patterns/python_design_patterns_singleton.htm
class DatabaseFacade():
    instance = None
    db = None

    def __init__(self, db):
        if DatabaseFacade.instance != None:
            raise Exception("DatabaseFacade is a singleton")
        else:
            DatabaseFacade.db = db
            DatabaseFacade.instance = self

    # Singleton pattern for DatabaseFacade
    def getInstance(db):
        if DatabaseFacade.instance == None:
            DatabaseFacade(db)
        return DatabaseFacade.instance

    def getDoctors(self):
        doctors = Doctor.query.all()
        doctors = doctors_schema.dump(doctors).data
        return doctors

    def getNurses(self):
        nurses = Nurse.query.all()
        nurses = nurses_schema.dump(nurses).data
        return nurses

    def getPatients(self):
        patients = Patient.query.all()
        patients = patients_schema.dump(patients).data
        return patients

    def login(self, type, email_, password_):
        if type == "Doctor":
            account = Doctor.query.filter_by(email=email_, password=password_).first()
            account = doctor_schema.dump(account).data
        elif type == "Patient":
            account = Patient.query.filter_by(email=email_, password=password_).first()
            account = patient_schema.dump(account).data
        else:
            account = Nurse.query.filter_by(email=email_, password=password_).first()
            account = nurse_schema.dump(account).data
        return account

    # Doctor modification
    def registerDoctor(self, json_data):
        # Validate and deserialize input
        data, errors = doctor_schema.load(json_data)
        if errors:
            return {'error': errors}
        doctor = Doctor.query.filter_by(permit_number=data['permit_number']).first()
        if doctor:
            return {'error': 'doctor already exists'}
        doctor = AccountAdapter.createFromJSON("Doctor", json_data)
        db.session.add(doctor)
        db.session.commit()

        result = doctor_schema.dump(doctor).data
        return result

    def updateDoctor(self, json_data):
        # Validate and deserialize input
        data, errors = doctor_schema.load(json_data)
        if errors:
            return {'error': errors}
        doctor = Doctor.query.filter_by(permit_number=data['permit_number']).first()
        if not doctor:
            return {'error': 'Category does not exist'}
        doctor = AccountAdapter.updateFromJSON("Doctor", doctor, json_data)
        db.session.commit()
        result = doctor_schema.dump(doctor).data
        return result

    def removeDoctor(self, json_data):
        # Validate and deserialize input
        data, errors = doctor_schema.load(json_data)
        if errors:
            return {'error': errors}
        doctor = Doctor.query.filter_by(permit_number=data['permit_number']).delete()
        db.session.commit()
        result = doctor_schema.dump(doctor).data
        return result

    # Nurse modification
    def registerNurse(self, json_data):
        # Validate and deserialize input
        data, errors = nurse_schema.load(json_data)
        if errors:
            return {'error': errors}
        nurse = Nurse.query.filter_by(access_id=data['access_id']).first()
        if nurse:
            return {'error': 'Nurse already exists'}
        nurse = AccountAdapter.createFromJSON("Nurse", json_data)
        db.session.add(nurse)
        db.session.commit()

        result = nurse_schema.dump(nurse).data
        return result

    def updateNurse(self, json_data):
        # Validate and deserialize input
        data, errors = nurse_schema.load(json_data)
        if errors:
            return {'error': errors}
        nurse = Nurse.query.filter_by(access_id=data['access_id']).first()
        if not nurse:
            return {'error': 'Category does not exist'}
        nurse = AccountAdapter.updateFromJSON("Nurse", nurse, json_data)
        db.session.commit()
        result = nurse_schema.dump(nurse).data
        return result

    def removeNurse(self, json_data):
        # Validate and deserialize input
        data, errors = nurse_schema.load(json_data)
        if errors:
            return {'error': errors}
        nurse = Nurse.query.filter_by(access_id=data['access_id']).delete()
        db.session.commit()
        result = nurse_schema.dump(nurse).data
        return result

    # Patient modification
    def registerPatient(self, json_data):
        # Validate and deserialize input
        data, errors = patient_schema.load(json_data)
        if errors:
            return {'error': errors}
        patient = Patient.query.filter_by(card_number=data['card_number']).first()
        if patient:
            return {'error': 'Patient already exists'}
        patient = AccountAdapter.createFromJSON("Patient", json_data)
        db.session.add(patient)
        db.session.commit()

        result = patient_schema.dump(patient).data
        return result

    def updatePatient(self, json_data):
        # Validate and deserialize input
        data, errors = patient_schema.load(json_data)
        if errors:
            return {'error': errors}
        patient = Patient.query.filter_by(card_number=data['card_number']).first()
        if not patient:
            return {'error': 'Category does not exist'}
        patient = AccountAdapter.updateFromJSON("Patient", patient, json_data)
        db.session.commit()
        result = patient_schema.dump(patient).data
        return result

    def removePatient(self, json_data):
        # Validate and deserialize input
        data, errors = patient_schema.load(json_data)
        if errors:
            return {'error': errors}
        patient = Patient.query.filter_by(card_number=data['card_number']).delete()
        db.session.commit()
        result = patient_schema.dump(patient).data
        return result
