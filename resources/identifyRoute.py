from flask_restful import Resource
#
class Login(Resource):
    def get(self):
        return {"message": "from login"}

class Logout(Resource):
    def get(self):
        return {"message": "from logout"}