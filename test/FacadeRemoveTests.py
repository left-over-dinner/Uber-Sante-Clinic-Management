import unittest
from datetime import date
from flask import json
from Model import SQLAlchemy, Doctor, Patient, Nurse, Appointment, Availability
from run import create_app
from Classes.AccountAdapter import AccountAdapter
from app import json_doc, json_nur, json_pat, json_appointment


class FacadeRemoveTests(unittest.TestCase):

    # --- Sets up the testing database that will live in the RAM for the duration of the tests
    # and sets up the flask testing client --- #
    @classmethod
    def setUpClass(cls):
        app = create_app("test_config")
        app.testing = True
        cls.test = app.test_client()
        db = SQLAlchemy(app)
        with app.app_context():
            Doctor.__table__.create(bind=db.engine)
            Patient.__table__.create(bind=db.engine)
            Nurse.__table__.create(bind=db.engine)
            Availability.__table__.create(bind=db.engine)
            # Appointment.__table__.create(bind=db.engine)
        testdoctor = AccountAdapter.createFromJSON('Doctor', json_doc)
        testpatient = AccountAdapter.createFromJSON('Patient', json_pat)
        testpatient.birth_day = date(1997, 9, 16)
        testnurse = AccountAdapter.createFromJSON('Nurse', json_nur)
        # testappointment = Appointment.__init__(json_appointment['patient_card_number'],
        #                                        json_appointment['doctor_permit_number'],json_appointment['date'],
        #                                        json_appointment['slots'], json_appointment['appointment_type'])
        # db.session.add_all([testdoctor, testnurse, testpatient])
        # db.session.commit()

    # def test_Remove_Patient(self):
    #     response = self.test.delete('api/Patient', data=json_pat)
    #     responsebytes = response.data
    #     responsejson = json.loads(responsebytes.decode('utf-8'))
    #     print(response)
    #     print(responsebytes)
        #assertions

        # assert responsejson['data'] == json_pat
        # assert responsejson['status'] == 'success'
        # assert response._status == '200 OK'
        # assert response._status_code == 200

    def test_Remove_Appointment(self):
        # response = self.test.delete('api/Appointment', data=json_appointment)
        response = "hello"
        print(response)