from Model  import Doctor, Nurse, Patient

class AccountFactory:
    def getAccount(accounttype):
        if accounttype == "Doctor":
            return Doctor(permit_number="", last_name="", first_name="", speciality="", location="", email="",password="")
        elif accounttype == "Patient":
            return Patient(card_number ="", birth_day="", gender="", phone_number="", address="", email="", first_name="",last_name="",password="")
        elif accounttype == "Nurse":
            return Nurse(access_id="",password="",last_name="",first_name="",email="")


pass


