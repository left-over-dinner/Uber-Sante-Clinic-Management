import unittest
from datetime import date
from flask import json
from Model import SQLAlchemy, Doctor, Patient, Nurse
from run import create_app
from classes.AccountAdapter import AccountAdapter
import json


class FacadeLoginTests(unittest.TestCase):
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
        with open('sampleData.json') as data_file:
            FacadeLoginTests.data = json.load(data_file)
        testdoctor  = AccountAdapter.createFromJSON('Doctor' , FacadeLoginTests.data["json_doc"])
        testpatient = AccountAdapter.createFromJSON('Patient', FacadeLoginTests.data["json_pat_case"])
        testnurse   = AccountAdapter.createFromJSON('Nurse'  , FacadeLoginTests.data["json_nur"])
        #correction to date
        testpatient.birth_day = date(1997, 9, 16)
        db.session.add_all([testdoctor, testnurse, testpatient])
        db.session.commit()

    def test_Login_Doctor(self):
        #Login credentials
        info = {
            'email'   :'me@you'  ,
            'password':'you@pass',
            'type'    :'Doctor'
        }
        #create the API call
        response = self.test.post('api/Login', data=json.dumps(info),headers={'Content-Type': 'application/json'})
        responsebytes = response.data
        responsejson = json.loads(responsebytes.decode('utf-8'))
        #assert the response
        assert responsejson['data'] == self.data["json_doc"]
        assert responsejson['status'] == 'success'
        assert response._status == '200 OK'
        assert response._status_code == 200

    def test_Login_Patient(self):
        info = {
            "email":"sample2", 
            "password":"sample2",
            "type":"Patient"
        }
        response = self.test.post('api/Login', data=json.dumps(info), headers={'Content-Type': 'application/json'})
        responsebytes = response.data
        responsejson = json.loads(responsebytes.decode('utf-8'))
        print(responsejson['data'])
        assert responsejson['data'] == self.data['json_pat_case']
        assert responsejson['status'] == 'success'
        assert response._status == '200 OK'
        assert response._status_code == 200

    def test_Login_Nurse(self):
        info = {
            "email":"sample3",
            "password":"sample3",
            "type":"Nurse"
        }
        response = self.test.post('api/Login', data=json.dumps(info),headers={'Content-Type': 'application/json'})
        responsebytes = response.data
        responsejson = json.loads(responsebytes.decode('utf-8'))
    
        assert responsejson['data'] == self.data['json_nur']
        assert responsejson['status'] == 'success'
        assert response._status == '200 OK'
        assert response._status_code == 200

    def test_Login_Nurse_Bad_Login(self):
        info = {
            "email":"FAKE",
            "password":"FAKE",
            "type":"Nurse"
        }
        response = self.test.post('api/Login', data=json.dumps(info),headers={'Content-Type': 'application/json'})
        responsebytes = response.data
        responsejson = json.loads(responsebytes.decode('utf-8'))
        assert responsejson['status'] == 'failure'
        assert responsejson['message'] == 'Invalid login'
        assert response._status == '200 OK'
        assert response._status_code == 200

    def test_No_Type_Error(self):
        try:
            response = self.test.post('api/Login', data=json.dumps(dict(email="sample3", password="sample3")))
        except KeyError:
            assert KeyError.__class__ == type and KeyError.__doc__ == "Mapping key not found."

    def test_No_Email_Error(self):
        try:
            response = self.test.post('api/Login', data=json.dumps(dict(password="sample3", type="Doctor")))
        except KeyError:
            assert KeyError.__class__ == type and KeyError.__doc__ == "Mapping key not found."

    def test_No_Password_Error(self):
        try:
            response = self.test.post('api/Login', data=json.dumps(dict(email="sample3", type="Doctor")))
        except KeyError:
            assert KeyError.__class__ == type and KeyError.__doc__ == "Mapping key not found."

