class Message:
    key="message"
class NoInputMessage(Message):
    value = "No input data provided"
class RegistrationCompleteMessage(Message):
    value = "Registration Complete"
class UpdateCompleteMessage(Message):
    value = "Update Complete"
class InvalidLoginMessage(Message):
    value = "Invalid login"
class CustomMessage(Message):
    def __init__(self, myMessage):
        self.value = myMessage

