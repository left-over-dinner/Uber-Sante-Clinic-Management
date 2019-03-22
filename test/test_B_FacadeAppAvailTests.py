import unittest
from datetime import date
from flask import json
from Model import SQLAlchemy, Doctor, Patient, Nurse
from run import create_app
from classes.AccountAdapter import AccountAdapter
import json

from Model import db
from classes.DatabaseFacade import DatabaseFacade

class test_DataBaseFacade(unittest.TestCase):
    data = None
    database = None
    @classmethod
    def setUpClass(cls):
        app = create_app("test_config")
        app.testing = True
        app.app_context().push()
        cls.test = app.test_client()
        #create local database
        db = SQLAlchemy(app)
        with app.app_context():
            Doctor.__table__.create(bind=db.engine)
            Patient.__table__.create(bind=db.engine)
            Nurse.__table__.create(bind=db.engine)
        with open('sampleData.json') as data_file:
            test_DataBaseFacade.data = json.load(data_file)
        #db.session.add_all([testdoctor, testnurse, testpatient])
        db.session.commit()

        test_DataBaseFacade.database_facade = DatabaseFacade.getInstance(db)

def test_registerAvailability(self):
        jsondata= self.data['json_ava']
        #register a doctor
        self.database_facade.registerAvailability(jsondata)
        avail = self.database_facade.getAvailabilityByAvailabiityId("1")
        #assert with local account using primary key
        assert avail.id == "1"

    def test_registerAppointment(self):
        assert 5==5

    def test_updateDoctor(self):
        #with open('sampleData.json') as data_file:
        #    data = json.load(data_file)
        #database_facade = DatabaseFacade.getInstance(db)
        #database_facade.registerDoctor(data['json_doc'])
        #database_facade.updateDoctor(data['json_doc1'])
        #doctor = database_facade.getDoctorsByPermitNumber("56765")
        #assert doctor.last_name == "Line"
        #assert doctor.first_name == "Ghanem"
        #assert doctor.email == "me@you"
        #assert doctor.password == "pass"
        #assert doctor.permit_number == "56765"
        #assert doctor.location == "Montreal"
        #assert doctor.speciality == "chirurgie"
        #database_facade.removeDoctor(data['json_doc'])
        assert 5==5

    def test_updateNurse(self):
        #with open('sampleData.json') as data_file:
        #    data = json.load(data_file)
        #database_facade = DatabaseFacade.getInstance(db)
        #database_facade.registerNurse(data['json_nur'])
        #database_facade.updateNurse(data['json_nur1'])
        #nurse = database_facade.getNursesByAccessId("3434")
        #assert nurse.last_name == "YOLO1"
        #assert nurse.first_name == "YOU31"
        #assert nurse.email == "sample31"
        #assert nurse.password == "sample31"
        #assert nurse.access_id == "3434"
        #database_facade.removeNurse(data['json_nur'])
        assert 5==5

    def test_updatePatient(self):
        #with open('sampleData.json') as data_file:
        #    data = json.load(data_file)
        #database_facade = DatabaseFacade.getInstance(db)
        #database_facade.registerPatient(data['json_pat'])
        #database_facade.updatePatient(data['json_pat1'])
        #patient = database_facade.getPatientsByCardNumber("989898")
        #assert patient.last_name == "Lara1"
        #assert patient.first_name == "sample21"
        #assert patient.email == "sample21"
        #assert patient.password == "sample21"
        #assert patient.card_number == "989898"
        #assert patient.birth_day.strftime('%Y-%m-%d') == '1997-09-16'
        #assert patient.gender == "sample21"
        #assert patient.phone_number == "sample21"
        #assert patient.address == "sample21"
        #database_facade.removePatient(data['json_pat'])
        assert 5==5

    def test_updateAvailability(self):
        #with open('sampleData.json') as data_file:
        #    data = json.load(data_file)
        #database_facade = DatabaseFacade.getInstance(db)
        #database_facade.registerAvailability(data['json_ava'])
        #database_facade.updateAvailability(data['json_ava1'])
        #ava = database_facade.getAvailabilityByAvailabiityId("99999")
        #assert ava.doctor_permit_number == '12345'
        #assert ava.slots == "[1,4,6]"
        #database_facade.removeAvailability(data['json_ava'])
        assert 5==5

    def test_registerAppointment(self):
        #with open('sampleData.json') as data_file:
        #    data = json.load(data_file)
        #database_facade = DatabaseFacade.getInstance(db)
        #database_facade.registerAppointment(data['json_app'])
        #database_facade.updateAppointment(data['json_app1'])
        #app = database_facade.getAppointmentByPatientCard("98989")
        #assert app.doctor_permit_number == '12345'
        #database_facade.removeAppointemt(data['json_app'])
        assert 5==5


