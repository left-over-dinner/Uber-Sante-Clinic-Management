from flask import Blueprint
from flask_restful import Api
from resources.Hello import Hello
from resources.PatientResource import PatientResource
from resources.DoctorResource import DoctorResource
from resources.NurseResource import NurseResource
from resources.Appointment import AppointmentResource
from resources.Availability import AvailabilityResource
from resources.LoginResource import LoginResource
from resources.ClinicResource import ClinicsResource
import classes.AccountAdapter

api_bp = Blueprint('api', __name__)
api = Api(api_bp)


#SAMPLE DATA, to be put in a respective file for better code
#can be done for iteration 2
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

json_appointment = {}
json_appointment['patient_card_number'] = "sample2"
json_appointment['doctor_permit_number'] = "436545"
json_appointment['date'] = '2019-03-11'
json_appointment['slots'] = '[1, 2]'
json_appointment['appointment_type'] = "walk-in"

json_availability = {}
json_availability['availability_id'] = '1'
json_availability['doctor_permit_number'] = '436545'
json_availability['date'] = '2019-03-11'
json_availability['slots'] = '[1, 2, 3, 4, 5]'

#test = AccountAdapter
nurse = classes.AccountAdapter.AccountAdapter.createFromJSON("Patient",json_pat)
print(nurse.last_name)

# Routes
# register, login and logout
api.add_resource(Hello, '/Hello')


api.add_resource(PatientResource, '/Patient')
api.add_resource(DoctorResource, '/Doctor')
api.add_resource(NurseResource, '/Nurse')
api.add_resource(AppointmentResource, '/Appointment')
api.add_resource(AvailabilityResource, '/Availability')
api.add_resource(ClinicsResource, '/Clinics')
api.add_resource(LoginResource, '/Login')
#includes login and logout
