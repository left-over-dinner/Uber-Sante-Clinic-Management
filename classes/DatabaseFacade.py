from datetime import date
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

    def getDoctorsByPermitNumber(self, permit_number_):
        doctor = Doctor.query.filter_by(permit_number=permit_number_).first()
        return doctor

    def getNurses(self):
        nurses = Nurse.query.all()
        nurses = nurses_schema.dump(nurses).data
        return nurses

    def getNursesByAccessId(self, access_id_):
        nurse = Nurse.query.filter_by(access_id=access_id_).first()
        return nurse

    def getPatients(self):
        patients = Patient.query.all()
        patients = patients_schema.dump(patients).data
        return patients

    def getPatientsByCardNumber(self, card_number_):
        patient = Patient.query.filter_by(card_number=card_number_).first()
        return patient

    def getAvailibilities(self):
        availabilities = Availability.query.all()
        availabilities = availabilityies_schema.dump(availabilities).data
        return availabilities

    def getAvailabilityByAvailabiityId(self, availability_id_):
        availability = Availability.query.filter_by(availability_id=availability_id_).first()
        return availability

    def getAppointments(self):
        appointments = Appointment.query.all()
        appointments = appointments_schema.dump(appointments).data
        return appointments

    def getAppointmentByPatientCard(self, patient_card_number_):
        availability = Appointment.query.filter_by(patient_card_number=patient_card_number_).first()
        return availability

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
        doctor = AccountAdapter.createFromJSON('Doctor', json_data)
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
        doctor = AccountAdapter.updateFromJSON('Doctor', doctor, json_data)
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
        nurse = AccountAdapter.createFromJSON('Nurse', json_data)
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
        nurse = AccountAdapter.updateFromJSON('Nurse', nurse, json_data)
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
        patient = AccountAdapter.createFromJSON('Patient', json_data)
        patient.birth_day = date(1990,1,1)
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
        patient = AccountAdapter.updateFromJSON('Patient', patient, json_data)
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

    def registerAvailability(self, json_data):
        # Validate and deserialize input
        data, errors = availability_schema.load(json_data)
        if errors:
            return {'error': errors}
        availability = Availability(
            doctor_permit_number=json_data['doctor_permit_number'],
            date=json_data['date'],
            slots=json_data['slots'],
        )

        db.session.add(availability)
        db.session.commit()

        result = availability_schema.dump(availability).data

        return result

    def updateAvailibility(self, json_data):
        data, errors = availability_schema.load(json_data)
        print(json_data['slots']);
        if errors:
            return {'error': errors}
        availability = Availability.query.filter_by(availability_id=data['availability_id']).first()
        if not availability:
            return {'error': 'Category does not exist'}
        availability.doctor_permit_number = json_data['doctor_permit_number'],
        availability.date = json_data['date'],
        availability.slots = None
        db.session.commit()

        availability = Availability.query.filter_by(availability_id=data['availability_id']).first()
        if not availability:
            return {'error': 'Category does not exist'}
        availability.doctor_permit_number = json_data['doctor_permit_number'],
        availability.date = json_data['date'],
        availability.slots = json_data["slots"]
        db.session.commit()

        result = availability_schema.dump(availability).data

        return result

    def removeAvailability(self, json_data):
        # Validate and deserialize input
        data, errors = availability_schema.load(json_data)
        if errors:
            return {'error': errors}
        availability = Availability.query.filter_by(availability_id=data['availability_id']).delete()
        db.session.commit()

        result = availability_schema.dump(availability).data

        return result

    def registerAppointment(self, json_data):
        # Validate and deserialize input
        data, errors = appointment_schema.load(json_data)
        if errors:
            return {'error': errors}
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

        return result


    def updateAppointment(self, json_data):
        # Validate and deserialize input
        data, errors = appointment_schema.load(json_data)
        if errors:
            return {'error': errors}
        appointment = Appointment.query.filter_by(patient_card_number=data['patient_card_number']).first()
        if not appointment:
            return {'error': 'Category does not exist'}
        appointment.patient_card_number = json_data['patient_card_number'],
        appointment.doctor_permit_number = json_data['doctor_permit_number'],
        appointment.date = json_data['date'],
        appointment.slots = json_data['slots'],
        appointment.appointment_type = json_data['appointment_type'],
        db.session.commit()

        result = appointment_schema.dump(appointment).data

        return result

    def removeAppointemt(self, json_data):

        # Validate and deserialize input
        data, errors = appointment_schema.load(json_data)
        if errors:
            {'error': errors}
        appointment = Appointment.query.filter_by(appointment_id=data['appointment_id']).delete()
        db.session.commit()

        result = appointment_schema.dump(appointment).data

        return result
