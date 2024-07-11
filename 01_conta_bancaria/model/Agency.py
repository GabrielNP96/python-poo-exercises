from Bank import Bank

class Agency(Bank):
    def __init__(self,name, address, number):
        super().__init__(name, address)
        self._number = number

    def __str__(self):
        return f'{self._name.ljust(25)} | {self._address.ljust(25)} | {str(self._number)}'

