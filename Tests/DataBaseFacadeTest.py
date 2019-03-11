import unittest
from run import create_app

from Model import db
from Classes.DatabaseFacade import DatabaseFacade

json_doc = {}
json_doc['last_name'     ] = "Line"
json_doc['first_name'    ] = "Ghanem"
json_doc['email'         ] = "me@you"
json_doc['password'      ] = "you@pass"
json_doc['permit_number' ] = "436546"
json_doc['location'      ] = "65767"
json_doc['speciality'     ] = "HELLO"

app = create_app("config")
app.app_context().push()


class TestDataBaseFacade(unittest.TestCase):

    def test_registerDoctor(self):
        database_facade = DatabaseFacade.getInstance(db)
        database_facade.registerDoctor(json_doc)
        doctor = database_facade.getDoctorsByPermitNumber("436545")
        assert doctor.last_name == "Nickel"

if __name__ == '__main__':
    unittest.main()

