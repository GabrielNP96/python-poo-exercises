from .Agency import Agency

class Bank_account(Agency):
    def __init__(self,name, address, number, holder, balalce):
        super().__init__(name, address, number)
        self.__holder = holder
        self.__balance = balalce