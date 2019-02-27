from flask import Blueprint
from flask_restful import Api
from resources.Hello import Hello
from resources.Patient import PatientResource
from resources.Doctor import DoctorResource
from resources.Nurse import NurseResource
from resources.Appointment import AppointmentResource
from resources.Availability import AvailabilityResource

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# Routes

api.add_resource(Hello, '/Hello')
api.add_resource(PatientResource, '/Patient')
api.add_resource(DoctorResource, '/Doctor')
api.add_resource(NurseResource, '/Nurse')
api.add_resource(AppointmentResource, '/Appointment')
api.add_resource(AvailabilityResource, '/Availability')