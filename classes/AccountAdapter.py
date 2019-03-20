import classes.AccountFactory


class AccountAdapter:

    def createFromJSON(type,jsonObject):
        newaccount = classes.AccountFactory.AccountFactory.get_account(type)
        newaccount.set_fields(jsonObject)
        return newaccount
        pass
    
    def updateFromJSON(account, jsonObject):
        account.set_fields(jsonObject)
        return account
        pass


pass

