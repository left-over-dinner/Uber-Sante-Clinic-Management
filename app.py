from flask import Blueprint
from flask_restful import Api
from resources.Hello import Hello
from resources.PatientResource import PatientResource
from resources.DoctorResource import DoctorResource
from resources.NurseResource import NurseResource
from resources.Appointment import AppointmentResource
from resources.Availability import AvailabilityResource
from resources.LoginResource import LoginResource

api_bp = Blueprint('api', __name__)
api = Api(api_bp)


# Routes
# register, login and logout
api.add_resource(Hello, '/Hello')


api.add_resource(PatientResource, '/Patient')
api.add_resource(DoctorResource, '/Doctor')
api.add_resource(NurseResource, '/Nurse')
api.add_resource(AppointmentResource, '/Appointment')
api.add_resource(AvailabilityResource, '/Availability')
api.add_resource(LoginResource, '/Login')
#includes login and logout
