from flask_restful import Resource
#
class UserRegister(Resource):
    def get(self):
        return {"message":"register new user"}