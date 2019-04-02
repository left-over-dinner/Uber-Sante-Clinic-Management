import unittest
import json
from run import create_app

from Model import db
from classes.DatabaseFacade import DatabaseFacade


app = create_app("config")
app.app_context().push()


class test_DataBaseFacade(unittest.TestCase):


    def test_registerDoctor(self):
        with open('sampleData.json') as data_file:
            data = json.load(data_file)
        database_facade = DatabaseFacade.getInstance(db)
        database_facade.register("Doctor", data['json_doc'])
        doctor = database_facade.getByIdentifier("Doctor", "56765")
        assert doctor.last_name == "Nickel"
        database_facade.remove("Doctor", data['json_doc'])

    def test_registerNurse(self):
        with open('sampleData.json') as data_file:
            data = json.load(data_file)
        database_facade = DatabaseFacade.getInstance(db)
        database_facade.register("Nurse", data['json_nur'])
        nurse = database_facade.getByIdentifier("Nurse", "3434")
        assert nurse.last_name == "YOLO"
        database_facade.remove("Nurse", data['json_nur'])

    def test_registerPatient(self):
        with open('sampleData.json') as data_file:
            data = json.load(data_file)
        database_facade = DatabaseFacade.getInstance(db)
        database_facade.register("Patient", data['json_pat'])
        patient = database_facade.getByIdentifier("Patient", "989898")
        assert patient.card_number == "989898"
        assert patient.birth_day.strftime('%Y-%m-%d') == "1997-09-16"
        database_facade.remove("Patient", data['json_pat'])

    def test_registerAvailability(self):
        with open('sampleData.json') as data_file:
            data = json.load(data_file)
        database_facade = DatabaseFacade.getInstance(db)
        database_facade.register("Availability", data['json_ava'])
        ava = database_facade.getByIdentifier("Availability", "99999")
        assert ava.doctor_permit_number == '12345'
        assert ava.slots == "[1,4,5]"
        database_facade.remove("Availability", data['json_ava'])

    def test_registerAppointment(self):
        with open('sampleData.json') as data_file:
            data = json.load(data_file)
        database_facade = DatabaseFacade.getInstance(db)
        database_facade.register("Appointment", data['json_app'])
        app = database_facade.getByIdentifier("Appointment", "98989")
        assert app.doctor_permit_number == '12345'
        database_facade.remove("Appointment", data['json_app'])

    def test_updateDoctor(self):
        with open('sampleData.json') as data_file:
            data = json.load(data_file)
        database_facade = DatabaseFacade.getInstance(db)
        database_facade.register("Doctor", data['json_doc'])
        database_facade.update("Doctor", data['json_doc1'])
        doctor = database_facade.getByIdentifier("Doctor", "56765")
        assert doctor.last_name == "Line"
        assert doctor.first_name == "Ghanem"
        assert doctor.email == "me@you"
        assert doctor.password == "pass"
        assert doctor.permit_number == "56765"
        assert doctor.location == "Montreal"
        assert doctor.specialty == "chirurgie"
        database_facade.remove("Doctor", data['json_doc'])

    def test_updateNurse(self):
        with open('sampleData.json') as data_file:
            data = json.load(data_file)
        database_facade = DatabaseFacade.getInstance(db)
        database_facade.register("Nurse", data['json_nur'])
        database_facade.update("Nurse", data['json_nur1'])
        nurse = database_facade.getByIdentifier("Nurse", "3434")
        assert nurse.last_name == "YOLO1"
        assert nurse.first_name == "YOU31"
        assert nurse.email == "sample31"
        assert nurse.password == "sample31"
        assert nurse.access_id == "3434"
        database_facade.remove("Nurse", data['json_nur'])

    def test_updatePatient(self):
        with open('sampleData.json') as data_file:
            data = json.load(data_file)
        database_facade = DatabaseFacade.getInstance(db)
        database_facade.register("Patient", data['json_pat'])
        database_facade.update("Patient", data['json_pat1'])
        patient = database_facade.getByIdentifier("Patient", "989898")
        assert patient.last_name == "Lara1"
        assert patient.first_name == "sample21"
        assert patient.email == "sample21"
        assert patient.password == "sample21"
        assert patient.card_number == "989898"
        assert patient.birth_day.strftime('%Y-%m-%d') == '1997-09-16'
        assert patient.gender == "sample21"
        assert patient.phone_number == "sample21"
        assert patient.address == "sample21"
        database_facade.remove("Patient", data['json_pat'])

    def test_updateAvailability(self):
        with open('sampleData.json') as data_file:
            data = json.load(data_file)
        database_facade = DatabaseFacade.getInstance(db)
        database_facade.register("Availability", data['json_ava'])
        database_facade.update("Availability", data['json_ava1'])
        ava = database_facade.getByIdentifier("Availability", "99999")
        assert ava.doctor_permit_number == '12345'
        assert ava.slots == "[1,4,6]"
        database_facade.remove("Availability", data['json_ava'])

    def test_registerAppointment(self):
        with open('sampleData.json') as data_file:
            data = json.load(data_file)
        database_facade = DatabaseFacade.getInstance(db)
        database_facade.register("Appointment", data['json_app'])
        database_facade.update("Appointment", data['json_app1'])
        app = database_facade.getByIdentifier("Appointment", "98989")
        assert app.doctor_permit_number == '12345'
        database_facade.remove("Appointment", data['json_app'])

if __name__ == '__main__':
    unittest.main()

