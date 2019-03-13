import unittest
import json
from datetime import date
from flask import json
from Model import SQLAlchemy, Doctor, Patient, Nurse, Appointment, Availability
from run import create_app
from classes.AccountAdapter import AccountAdapter
from app import json_doc, json_nur, json_pat, json_appointment, json_availability


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
            Appointment.__table__.create(bind=db.engine)
        testdoctor = AccountAdapter.createFromJSON('Doctor', json_doc)
        testpatient = AccountAdapter.createFromJSON('Patient', json_pat)
        testpatient.birth_day = date(1997, 9, 16)
        testnurse = AccountAdapter.createFromJSON('Nurse', json_nur)
        testappointment = Appointment(json_appointment['patient_card_number'],
                                                json_appointment['doctor_permit_number'], date(2019, 3, 11),
                                                    json_appointment['slots'], json_appointment['appointment_type'])
        testavailability = Availability(json_availability['availability_id'], json_availability['doctor_permit_number'],
                                        date(2019, 3, 11), json_availability['slots'])
        db.session.add_all([testdoctor, testnurse, testpatient, testappointment, testavailability])
        db.session.commit()

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
        response = self.test.delete('api/Appointment', data=json.dumps(dict(patient_card_number='sample2',
                                                                          doctor_permit_numbe='436545',
                                                                          date=date(2019, 3, 11),
                                                                          slots='[1, 2]',
                                                                          appointment_type='walk-in',
                                                                            appointment_id='1')))


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

        response = self.test.delete('api/Availability', data=json.dumps(dict(availability_id=1)))
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
