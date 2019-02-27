from flask_restful import Resource
 
class DoctorUpdate(Resource):
    def get(self):
        return {"message": "from doctor update"}
