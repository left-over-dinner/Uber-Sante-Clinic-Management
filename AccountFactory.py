from Classes.Doctor import Doctor
from Classes.Nurse import Nurse
from Classes.Patient import Patient


class AccountFactory:
    def getAccount(accounttype):
        if accounttype == "Doctor":
            return Doctor()
        elif accounttype == "Patient":
            return Patient()
        elif accounttype == "Nurse":
            return Nurse()


pass


