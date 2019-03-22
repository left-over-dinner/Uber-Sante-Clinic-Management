import unittest
import json
from datetime import date
from flask import json
from Model import SQLAlchemy, Doctor, Patient, Nurse, Appointment, Availability
from run import create_app
from classes.AccountAdapter import AccountAdapter
import json


class FacadeRemoveTests(unittest.TestCase):
    data = None
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
            Appointment.__table__.create(bind=db.engine)
        with open('sampleData.json') as data_file:
            FacadeRemoveTests.data = json.load(data_file)
        testdoctor  = AccountAdapter.createFromJSON('Doctor' , FacadeRemoveTests.data["json_doc"])
        testpatient = AccountAdapter.createFromJSON('Patient', FacadeRemoveTests.data["json_pat"])
        testnurse   = AccountAdapter.createFromJSON('Nurse'  , FacadeRemoveTests.data["json_nur"])
        testpatient.birth_day = date(1997, 9, 16)
        testappointment = Appointment(data["json_app"])
        testavailability = Availability(data["json_ava"])
        db.session.add_all([testdoctor, testnurse, testpatient, testappointment, testavailability])
        db.session.commit()

    def test_Remove_Appointment(self):
        response = self.test.delete('api/Appointment', data=json.dumps(dict(patient_card_number='98989',
                                                                          doctor_permit_numbe='98989',
                                                                          date=date(1900, 1, 9),
                                                                          slots='[1, 3]',
                                                                          appointment_type='Checkup',
                                                                            appointment_id='76765')))
        # convert the result into json
        tmp = json.loads(response.data)
        # assertions
        # status is expected to be success
        assert response._status == '200 OK'
        assert tmp['status'] == 'success'
        # data returned by the remove operation is expected to be empty
        assert tmp['data'] == {}
        # no data in the table after delete
        # do a get operation after deletion to check it
        result = self.test.get('api/Appointment')
        tmp = json.loads(result.data)
        assert tmp['data'] == []

    def test_Remove_Availability(self):

        response = self.test.delete('api/Availability', data=json.dumps(dict(availability_id=99999)))
        # convert the result into json
        tmp = json.loads(response.data)

        # assertions
        # status is expected to be success
        assert response._status == '200 OK'
        assert tmp['status'] == 'success'
        # data returned by the remove operation is expected to be empty
        assert tmp['data'] == {}
        # no data in the table after delete
        # do a get operation after deletion to check it
        result = self.test.get('api/Availability')
        tmp = json.loads(result.data)
        assert tmp['data'] == []
