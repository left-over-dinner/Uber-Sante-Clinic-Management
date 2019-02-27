from flask_restful import Resource
#
class PatientMake(Resource):
    def get(self):
        return {"message": "from patient make"}

class PatientUpdate(Resource):
    def get(self):
        return {"message": "from patient update"}

class PatientCheck(Resource):
    def get(self):
        return {"message": "from patient check"}

class PatientCancel(Resource):
    def get(self):
        return {"message": "from patient cancel"}