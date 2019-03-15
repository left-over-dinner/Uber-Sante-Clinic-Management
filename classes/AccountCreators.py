import classes.AccountFactory
import classes.Patient
import classes.Doctor
import classes.Nurse


class PatientAccountCreator(classes.AccountFactory.AccountFactory):

    @classmethod
    def get_account(cls):
        return classes.Patient.Patient()
        pass

    pass


class DoctorAccountCreator(classes.AccountFactory.AccountFactory):

    @classmethod
    def get_account(cls):
        return classes.Doctor.Doctor()
        pass

    pass


class NurseAccountCreator(classes.AccountFactory.AccountFactory):

    @classmethod
    def get_account(cls):
        return classes.Nurse.Nurse()
        pass

    pass

