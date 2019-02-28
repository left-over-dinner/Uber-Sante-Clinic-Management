from .Account import Account


class Nurse(Account):
    def __init__(self, firstname="", lastname="", email="", password="", accessid=""):
        Account.__init__(self, firstname,lastname,email,password)
        self.accessId = accessid


pass

