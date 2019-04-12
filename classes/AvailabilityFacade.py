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

class AvailabilityFacade():
    instance = None
    db = None

    def __init__(self, db):
        if AvailabilityFacade.instance != None:
            raise Exception("AvailabilityFacade is a singleton")
        else:
            AvailabilityFacade.db = db
            AvailabilityFacade.instance = self

    def getInstance(db):
        if AvailabilityFacade.instance == None:
            AvailabilityFacade(db)
        return AvailabilityFacade.instance

    def getAll(self):
        result = db.engine.execute("SELECT availability.availability_id, availability.date, availability.doctor_permit_number, availability.slots,doctor.first_name doctorFirstName,doctor.last_name doctorLastName,doctor.email doctorEmail,doctor.location doctorLocation,doctor.specialty doctorSpecialty,doctor.clinic_id, clinics.name clinicName  FROM availability INNER JOIN doctor on availability.doctor_permit_number = doctor.permit_number INNER JOIN clinics  ON clinics.clinic_id = doctor.clinic_id" )
        result = ProxyObjectAdapter.toArray(result, [customDateFormat, customSlotsFormat])
        return result

    def getAvailabilityByIdentifier(self, availability_id_):
        availability = Availability.query.filter_by(availability_id=availability_id_).first()
        return availability

    def register(self, json_data):
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

    def update(self, json_data):
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

    def remove(self, json_data):
        # Validate and deserialize input
        data, errors = availability_schema.load(json_data)
        if errors:
            return {'error': errors}
        availability = Availability.query.filter_by(availability_id=data['availability_id']).delete()
        db.session.commit()

        result = availability_schema.dump(availability).data

        return result
