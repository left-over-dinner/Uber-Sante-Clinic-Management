import unittest
from Model import SQLAlchemy, Doctor, Patient, Nurse
from run import create_app
from classes.AccountAdapter import AccountAdapter
import json


class AccountAdapterTests(unittest.TestCase):

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

    def test_create_Doctor_from_JSON(self):

        with open('sampleData.json') as data_file:
            data = json.load(data_file)
        testdoctor = AccountAdapter.createFromJSON('Doctor', data['json_doc'])

        # assert type last name is 'Nickel'
        assert testdoctor.last_name == 'Nickel'

        # assert type first name is 'Peck'
        assert testdoctor.first_name == 'Peck'

        # assert type email is 'me@you'
        assert testdoctor.email == 'me@you'

        # assert type password is 'you@pass'
        assert testdoctor.password == 'you@pass'

        # assert type permit number is '436545'
        assert testdoctor.permit_number == '436545'

        # assert type location is '65767'
        assert testdoctor.location == '65767'

        # assert type specialty is 'HELLO'
        assert testdoctor.specialty == 'HELLO'

    def test_create_Patient_from_JSON(self):

        with open('sampleData.json') as data_file:
            data = json.load(data_file)
        testpatient = AccountAdapter.createFromJSON('Patient', data['json_pat'])

        # assert type last name is 'OKOKOK'
        assert testpatient.last_name == 'OKOKOK'

        # assert type first name is 'sample2'
        assert testpatient.first_name == 'sample2'

        # assert type email is 'sample2'
        assert testpatient.email == 'sample2'

        # assert type password is 'sample2'
        assert testpatient.password == 'sample2'

        # assert type card number is 'sample2'
        assert testpatient.card_number == 'sample2'

        # assert type birthday is '1997-09-16'
        assert testpatient.birth_day == '1997-09-16'

        # assert type gender is 'sample2'
        assert testpatient.gender == 'sample2'

        # assert type phone number is 'sample2'
        assert testpatient.phone_number == 'sample2'

        # assert type address is 'sample2'
        assert testpatient.address == 'sample2'

    def test_create_Nurse_from_JSON(self):

        with open('sampleData.json') as data_file:
            data = json.load(data_file)
        testnurse = AccountAdapter.createFromJSON('Nurse', data['json_nur'])

        # assert type last name is 'YOLO'
        assert testnurse.last_name == 'YOLO'

        # assert type first name is 'YOU3'
        assert testnurse.first_name == 'YOU3'

        # assert type email is 'sample3'
        assert testnurse.email == 'sample3'

        # assert type password is 'sample3'
        assert testnurse.password == 'sample3'

        # assert type access id is 'sample3'
        assert testnurse.access_id == 'sample3'





