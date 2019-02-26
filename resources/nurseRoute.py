from flask_restful import Resource
class NurseBook(Resource):
    def get(self):
        return {"message": "from nurse book"}

class NurseUpdate(Resource):
    def get(self):
        return {"message": "from nurse update"}

class NurseCancel(Resource):
    def get(self):
        return {"message": "from nurse cancel"}

class NurseCheckAll(Resource):
    def get(self):
        return {"message": "from nurse check all"}