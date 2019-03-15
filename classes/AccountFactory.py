class AccountFactory:

    @classmethod
    def get_account(cls, account_type):
        creators_module = __import__('classes.AccountCreators')
        return getattr(creators_module.AccountCreators, account_type+'AccountCreator').get_account()
        pass

    pass


