class Account:

    def set_fields(self, fieldsdictionary):
        fields = fieldsdictionary.items()
        for key, value in fields:
            self.__setattr__(key, value)
        pass


pass
