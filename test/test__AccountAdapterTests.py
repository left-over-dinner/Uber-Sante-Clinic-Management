import unittest
from Model import SQLAlchemy, Doctor, Patient, Nurse
from run import create_app
from classes.AccountAdapter import AccountAdapter
import json

class AccountAdapterTests(unittest.TestCase):
    data = None
    @classmethod
    def setUpClass(cls):
        app = create_app("test_config")
        app.testing = True
        cls.test = app.test_client()
        #Load the sample data
        with open('sampleData.json') as data_file:
            AccountAdapterTests.data = json.load(data_file)

    def test_create_Doctor_from_JSON(self):
        json_data = self.data["json_doc"]
        #create an Doctor account
        testdoctor = AccountAdapter.createFromJSON('Doctor', json_data)

        #assert all data passed are properly converted from json       
        assert testdoctor.last_name     == json_data["last_name"     ]
        assert testdoctor.first_name    == json_data["first_name"    ]
        assert testdoctor.email         == json_data["email"         ]
        assert testdoctor.password      == json_data["password"      ]
        assert testdoctor.permit_number == json_data["permit_number" ]
        assert testdoctor.location      == json_data["location"      ]
        assert testdoctor.specialty     == json_data["specialty"     ]

    def test_create_Patient_from_JSON(self):
        json_data = self.data["json_pat"]
        #create an Patient account
        testpatient = AccountAdapter.createFromJSON('Patient', json_data)

        assert testpatient.last_name    == json_data["last_name"   ]
        assert testpatient.first_name   == json_data["first_name"  ]
        assert testpatient.email        == json_data["email"       ]
        assert testpatient.password     == json_data["password"    ]
        assert testpatient.card_number  == json_data["card_number" ]
        assert testpatient.birth_day    == json_data["birth_day"   ]
        assert testpatient.gender       == json_data["gender"      ]
        assert testpatient.phone_number == json_data["phone_number"]
        assert testpatient.address      == json_data["address"     ] 

    def test_create_Nurse_from_JSON(self):
        json_data = self.data["json_nur"]
        #create an Nurse account
        testnurse = AccountAdapter.createFromJSON('Nurse', json_data)

        assert testnurse.last_name  == json_data["last_name" ]
        assert testnurse.first_name == json_data["first_name"]
        assert testnurse.email      == json_data["email"     ]
        assert testnurse.password   == json_data["password"  ]
        assert testnurse.access_id  == json_data["access_id" ]





