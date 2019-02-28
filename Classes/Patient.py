from .Account import Account


class Patient(Account):
    def __init__(self, firstname="", lastname="", email="", password="", hcnumber="", bday="", gender="", phonenum="", physaddress=""):
        Account.__init__(self, firstname,lastname,email,password)
        self.hCNumber = hcnumber
        self.bDay = bday
        self.gender = gender
        self.phoneNumber = phonenum
        self.physAddress = physaddress


pass

