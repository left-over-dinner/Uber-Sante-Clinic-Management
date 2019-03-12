import unittest
import ast
from datetime import date

from flask import json, jsonify

from Model import SQLAlchemy, Doctor, Patient, Nurse
from run import create_app
from Classes.AccountAdapter import AccountAdapter
from app import json_doc, json_nur, json_pat


class FacadeLoginTests(unittest.TestCase):

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
        testdoctor = AccountAdapter.createFromJSON('Doctor',json_doc)
        testpatient = AccountAdapter.createFromJSON('Patient', json_pat)
        testpatient.birth_day = date(1997, 9, 16)
        testnurse = AccountAdapter.createFromJSON('Nurse', json_nur)
        db.session.add_all([testdoctor, testnurse, testpatient])
        db.session.commit()

    def test_Login_Doctor(self):
        response = self.test.post('api/Login', data=json.dumps(dict(email="me@you", password="you@pass",type="Doctor")))
        responsebytes = response.data
        responsejson = json.loads(responsebytes.decode('utf-8'))
        assert responsejson['data'] == json_doc
        assert responsejson['status'] == 'success'
        assert response._status == '200 OK'
        assert response._status_code == 200






