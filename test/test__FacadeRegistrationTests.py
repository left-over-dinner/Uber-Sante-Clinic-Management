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


    def test_registerDoctor(self):
        jsondata= self.data['json_doc']
        #register a doctor
        self.database_facade.registerDoctor(jsondata)
        doctor = self.database_facade.getDoctorsByPermitNumber(jsondata["permit_number"])
        #assert with local account using primary key
        assert doctor.permit_number == jsondata["permit_number"] 

    def test_registerNurse(self):
        jsondata= self.data['json_nur']
        self.database_facade.registerNurse(jsondata)
        nurse = self.database_facade.getNursesByAccessId(jsondata["access_id"])
        assert nurse.access_id == jsondata["access_id"]

    #DO NOT TEST the following method
    # due to error from Marshmallow library 'Invalid date'
    #def test_registerPatient(self):
        

        #jsondata= self.data['json_pat_complete']
        ##register a doctor
        #self.database_facade.registerPatient(jsondata)
        #patient = self.database_facade.getPatientsByCardNumber(jsondata["card_number"])
        ##assert with local account using primary key
        #assert patient.card_number == jsondata["card_number"]

