import unittest
from run import create_app

from Model import db
from Classes.DatabaseFacade import DatabaseFacade

json_doc = {}
json_doc['last_name'     ] = "Line"
json_doc['first_name'    ] = "Ghanem"
json_doc['email'         ] = "me@you"
json_doc['password'      ] = "you@pass"
json_doc['permit_number' ] = "987654"
json_doc['location'      ] = "65767"
json_doc['speciality'     ] = "HELLO"

json_nur = {}
json_nur['last_name'  ] = 'YOLO'
json_nur['first_name' ] = 'YOU3'
json_nur["email"      ] = 'sample3'
json_nur["password"   ] = 'sample3'
json_nur['access_id'  ] = '343434'

json_pat = {}
json_pat['last_name'    ] = "Lara"
json_pat['first_name'   ] = "sample2"
json_pat['email'        ] = "sample2"
json_pat['password'     ] = "sample2"
json_pat['card_number'  ] = "98765498"
json_pat['birth_day'    ] = "sample2"
json_pat['gender'       ] = "sample2"
json_pat['phone_number' ] = "9876543"
json_pat['address'     ] = "sample2"

app = create_app("config")
app.app_context().push()


class TestDataBaseFacade(unittest.TestCase):

    def test_registerDoctor(self):
        database_facade = DatabaseFacade.getInstance(db)
        database_facade.registerDoctor(json_doc)
        doctor = database_facade.getDoctorsByPermitNumber("987654")
        print(doctor)
        assert doctor.last_name == "Line"
        database_facade.removeDoctor(json_doc)

    def test_registerNurse(self):
        database_facade = DatabaseFacade.getInstance(db)
        database_facade.registerNurse(json_nur)
        nurse = database_facade.getNursesByAcessId("343434")
        print(nurse)
        assert nurse.last_name == "YOLO"
        database_facade.removeNurse(json_nur)

    def test_registerPatient(self):
        database_facade = DatabaseFacade.getInstance(db)
        database_facade.registerPatient(json_pat)
        #patient = database_facade.getPatients()
        patient = database_facade.getPatientsByCardNumber("98765498")
        print(patient)
        assert patient.card_number == "98765498"
        #database_facade.removePatient(json_pat)

if __name__ == '__main__':
    unittest.main()

