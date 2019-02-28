from .Account import Account


class Doctor(Account):
    def __init__(self, firstname="", lastname="", email="", password="", permitnumber="", specialty="", location=""):
        Account.__init__(self, firstname,lastname,email,password)
        self.permitNumber = permitnumber
        self.specialty = specialty
        self.location = location


pass
