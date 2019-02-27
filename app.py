from flask import Blueprint
from flask_restful import Api
from resources.Hello import Hello
from resources.registerRoute import UserRegister
from resources.identifyRoute import Login, Logout
from resources.patientRoute import PatientMake, PatientUpdate, PatientCheck, PatientCancel
from resources.nurseRoute import NurseBook, NurseUpdate, NurseCancel, NurseCheckAll
from resources.doctorRoute import DoctorUpdate

# from resources.Category import CategoryResource
# from resources.Comment import CommentResource
from resources.PatientResource import PatientResource
from resources.DoctorResource import DoctorResource
from resources.NurseResource import NurseResource
from resources.Appointment import AppointmentResource
from resources.Availability import AvailabilityResource

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

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
#includes login and logout
