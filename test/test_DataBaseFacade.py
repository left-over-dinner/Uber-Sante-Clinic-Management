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

json_doc1 = {}
json_doc['last_name'     ] = "Line1"
json_doc['first_name'    ] = "Ghanem1"
json_doc['email'         ] = "me@you1"
json_doc['password'      ] = "you@pass1"
json_doc['permit_number' ] = "987654"
json_doc['location'      ] = "657671"
json_doc['speciality'     ] = "HELLO1"

json_nur = {}
json_nur['last_name'  ] = 'YOLO'
json_nur['first_name' ] = 'YOU3'
json_nur["email"      ] = 'sample3'
json_nur["password"   ] = 'sample3'
json_nur['access_id'  ] = '343434'

json_nur1 = {}
json_nur['last_name'  ] = 'YOLO1'
json_nur['first_name' ] = 'YOU31'
json_nur["email"      ] = 'sample31'
json_nur["password"   ] = 'sample31'
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

json_pat1 = {}
json_pat['last_name'    ] = "Lara1"
json_pat['first_name'   ] = "sample21"
json_pat['email'        ] = "sample21"
json_pat['password'     ] = "sample21"
json_pat['card_number'  ] = "987654981"
json_pat['birth_day'    ] = "sample21"
json_pat['gender'       ] = "sample21"
json_pat['phone_number' ] = "98765431"
json_pat['address'     ] = "sample21"

app = create_app("config")
app.app_context().push()


class test_DataBaseFacade(unittest.TestCase):

    def test_registerDoctor(self):
        database_facade = DatabaseFacade.getInstance(db)
        database_facade.registerDoctor(json_doc)
        doctor = database_facade.getDoctorsByPermitNumber("987654")
        print(doctor)
        assert doctor.last_name == "Line"
        database_facade.removeDoctor(json_doc)

    def test_updateDoctor(self):
        database_facade = DatabaseFacade.getInstance(db)
        database_facade.registerDoctor(json_doc)
        database_facade.updateDoctor(json_doc1)
        doctor = database_facade.getDoctorsByPermitNumber("987654")
        assert doctor.last_name == "Line1"
        assert doctor.first_name == "Ghanem1"
        assert doctor.email == "me@you1"
        assert doctor.password == "you@pass1"
        assert doctor.permit_number == "987654"
        assert doctor.location == "657671"
        assert doctor.speciality == "HELLO1"
        database_facade.removeDoctor(json_doc1)

    def test_registerNurse(self):
        database_facade = DatabaseFacade.getInstance(db)
        database_facade.registerNurse(json_nur)
        nurse = database_facade.getNursesByAcessId("343434")
        print(nurse)
        assert nurse.last_name == "YOLO"
        database_facade.removeNurse(json_nur)

    def test_updateNurse(self):
        database_facade = DatabaseFacade.getInstance(db)
        database_facade.registerNurse(json_nur)
        database_facade.updateNurse(json_nur1)
        nurse = database_facade.getNursesByAccessId("343434")
        assert nurse.last_name == "YOLO1"
        assert nurse.first_name == "YOU31"
        assert nurse.email == "sample31"
        assert nurse.password == "sample31"
        assert nurse.access_id == "343434"
        database_facade.removeNurse(json_nur1)

    def test_registerPatient(self):
        database_facade = DatabaseFacade.getInstance(db)
        database_facade.registerPatient(json_pat)
        #patient = database_facade.getPatients()
        patient = database_facade.getPatientsByCardNumber("98765498")
        print(patient)
        assert patient.card_number == "98765498"
        #database_facade.removePatient(json_pat)

    def test_updatePatient(self):
        database_facade = DatabaseFacade.getInstance(db)
        database_facade.registerPatient(json_pat)
        database_facade.updatePatient(json_pat1)
        patient = database_facade.getPatientsByCardNumber("98765498")
        assert patient.last_name == "Lara1"
        assert patient.first_name == "sample21"
        assert patient.email == "sample21"
        assert patient.password == "sample21"
        assert patient.card_number == "98765498"
        assert patient.birth_day == "sample21"
        assert patient.gender == "sample21"
        assert patient.phone_number == "98765431"
        assert patient.address == "sample21"
        database_facade.removePatient(json_pat1)

if __name__ == '__main__':
    unittest.main()

