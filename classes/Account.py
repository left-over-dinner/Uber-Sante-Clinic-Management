class Account:

    # removes all the account's current fields and sets them to the fields in the dictionary object
    def set_fields(self, fields_dictionary):
        del self.__dict__
        fields = fields_dictionary.items()
        for key, value in fields:
            self.__setattr__(key, value)
        pass

    pass
