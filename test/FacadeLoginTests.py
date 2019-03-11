import unittest
from datetime import date

from Model import SQLAlchemy
from run import create_app
from Classes.AccountAdapter import AccountAdapter
from app import json_doc, json_nur, json_pat


class FacadeLoginTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        app = create_app("config")
        app.testing = True
        cls.test = app.test_client()
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        db = SQLAlchemy(app)
        testDoctor = AccountAdapter.createFromJSON('Doctor',json_doc)
        testPatient = AccountAdapter.createFromJSON('Patient', json_pat)
        testPatient.birth_day = date(1997, 9, 16)
        testNurse = AccountAdapter.createFromJSON('Nurse', json_nur)
        db.session.add(testDoctor)
        db.session.add(testNurse)
        db.session.add(testPatient)
        db.session.commit()



    def test_Login_Doctor(self):
        pass





