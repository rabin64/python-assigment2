#15. Imagine you are designing a banking application. What would a
#customer look like? What attributes would she have? What methods
#would she have?

class account_holder:

    def __init__(self, account_name, account_type, account_number):
        self.account_name = account_name
        self.account_number = account_number
        self.account_type = account_type

    def account_details(self):
        pass

    def person_details(self):
        pass

    def deposit_amount(self, amount):
        pass

    def withdraw_amount(self, amount):
        pass

