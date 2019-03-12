from flask import Blueprint
from flask_restful import Api
from resources.Hello import Hello
from resources.registerRoute import UserRegister
from resources.identifyRoute import Login, Logout
from resources.patientRoute import PatientMake, PatientUpdate, PatientCheck, PatientCancel
from resources.nurseRoute import NurseBook, NurseUpdate, NurseCancel, NurseCheckAll
from resources.doctorRoute import DoctorUpdate
from Classes.AccountAdapter import AccountAdapter

# from resources.Category import CategoryResource
# from resources.Comment import CommentResource
from resources.PatientResource import PatientResource
from resources.DoctorResource import DoctorResource
from resources.NurseResource import NurseResource
from resources.Appointment import AppointmentResource
from resources.Availability import AvailabilityResource
from resources.LoginResource import LoginResource

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

json_doc = {}
json_doc['last_name'     ] = "Nickel"
json_doc['first_name'    ] = "Peck"
json_doc['email'         ] = "me@you"
json_doc['password'      ] = "you@pass"
json_doc['permit_number' ] = "436545"
json_doc['location'      ] = "65767"
json_doc['specialty'     ] = "HELLO"

json_pat = {}
json_pat['last_name'    ] = 'OKOKOK'
json_pat['first_name'   ] = 'sample2'
json_pat["email"        ] = 'sample2'
json_pat["password"     ] = 'sample2'
json_pat['card_number'  ] = 'sample2'
json_pat['birth_day'    ] = '1997-09-16'
json_pat['gender'       ] = 'sample2'
json_pat['phone_number' ] = 'sample2'
json_pat['address'     ] = 'sample2'

json_nur = {}
json_nur['last_name'  ] = 'YOLO'
json_nur['first_name' ] = 'YOU3'
json_nur["email"      ] = 'sample3'
json_nur["password"   ] = 'sample3'
json_nur['access_id'  ] = 'sample3'

#test = AccountAdapter
nurse = AccountAdapter.createFromJSON("Patient",json_pat)
print(nurse.last_name)


# Routes
# register, login and logout
api.add_resource(UserRegister, '/register')
api.add_resource(Login, '/identify/login')
api.add_resource(Logout, '/identify/logout')
#schedule editing for patient
api.add_resource(PatientMake, '/schedule/patient/make')
api.add_resource(PatientUpdate, '/schedule/patient/update')
api.add_resource(PatientCheck, '/schedule/patient/check')
api.add_resource(PatientCancel, '/schedule/patient/cancel')
#schedule editing for nurse
api.add_resource(NurseBook, '/schedule/nurse/book')
api.add_resource(NurseUpdate, '/schedule/doctor/update')
api.add_resource(NurseCancel, '/schedule/doctor/cancel')
api.add_resource(NurseCheckAll, '/schedule/doctor/checkAll')
#schedule editing for doctor
api.add_resource(DoctorUpdate, '/schedule/doctor/update')
api.add_resource(Hello, '/Hello')


api.add_resource(PatientResource, '/Patient')
api.add_resource(DoctorResource, '/Doctor')
api.add_resource(NurseResource, '/Nurse')
api.add_resource(AppointmentResource, '/Appointment')
api.add_resource(AvailabilityResource, '/Availability')
api.add_resource(LoginResource, '/Login')
#includes login and logout
