from classes.AccountFactory import AccountFactory
from classes.Doctor import Doctor
from classes.Nurse import Nurse
from classes.Patient import Patient


class PatientAccountCreator(AccountFactory):

    @classmethod
    def get_account(cls):
        return Patient()
        pass
    pass


class DoctorAccountCreator(AccountFactory):

    @classmethod
    def get_account(cls):
        return Doctor()
        pass

    pass


class NurseAccountCreator(AccountFactory):

    @classmethod
    def get_account(cls):
        return Nurse()
        pass

    pass

