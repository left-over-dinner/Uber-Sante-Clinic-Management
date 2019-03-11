import os
import unittest
import tempfile
from mock import Mock
from mock import patch
import run
from run import create_app

from Model import db, Doctor, DoctorSchema
from Classes.DatabaseFacade import DatabaseFacade

json_doc = {}
json_doc['last_name'     ] = "Nickel"
json_doc['first_name'    ] = "Peck"
json_doc['email'         ] = "me@you"
json_doc['password'      ] = "you@pass"
json_doc['permit_number' ] = "436545"
json_doc['location'      ] = "65767"
json_doc['speciality'     ] = "HELLO"

app = create_app("config")
app.app_context().push()


class TestDataBaseFacade(unittest.TestCase):

    def test_registerDoctor(self):
        dataBaseFacade = DatabaseFacade.getInstance(db)
        dataBaseFacade.registerDoctor(json_doc)
        doctorData = dataBaseFacade.getDoctorsByPermitNumber("436545")
        print(doctorData)
        #doctorData.last_name




if __name__ == '__main__':
    unittest.main()

