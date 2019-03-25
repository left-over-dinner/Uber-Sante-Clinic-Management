import classes.AccountFactory
#import classes.Patient
#import classes.Doctor
#import classes.Nurse
from Model import Doctor, Nurse, Patient



class PatientAccountCreator(classes.AccountFactory.AccountFactory):

    @classmethod
    def get_account(cls):
        return Patient.createEmpty()
        pass

    pass


class DoctorAccountCreator(classes.AccountFactory.AccountFactory):

    @classmethod
    def get_account(cls):
        return Doctor.createEmpty()
        pass

    pass


class NurseAccountCreator(classes.AccountFactory.AccountFactory):

    @classmethod
    def get_account(cls):
        return Nurse.createEmpty()
        pass

    pass

