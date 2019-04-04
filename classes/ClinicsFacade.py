from Model import db, Clinics, ClinicsSchema
from classes.AccountAdapter import AccountAdapter

# clinic schema
clinics_schema = ClinicsSchema(many=True)
clinic_schema = ClinicsSchema()

class ClinicsFacade():
    instance = None
    db = None

    def __init__(self, db):
        if ClinicsFacade.instance != None:
            raise Exception("ClinicsFacade is a singleton")
        else:
            ClinicsFacade.db = db
            ClinicsFacade.instance = self

    def getInstance(db):
        if ClinicsFacade.instance == None:
            ClinicsFacade(db)
        return ClinicsFacade.instance

    def getAll(self):
        clinics = Clinics.query.all()
        clinics = clinics_schema.dump(clinics).data
        return clinics
