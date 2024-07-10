from .Agency import Agency

class Bank_account(Agency):
    def __init__(self,name, address, number, holder, balalce):
        super().__init__(name, address, number)
        self.__holder = holder
        self.__balance = balalce


    def __str__(self):
        f'Nome do banco: {self._name}\nEndereço do Banco: {self._address}\nNúmero da agência: {self._number}\nTitular da conta: {self.__holder}\nSaldo: {self.__balance}R$'

    def deposit(self,number):
        if float(number):
           self._balance += float(number)
           return print(f'Você depositou {number}R$')
        return print('Erro... \nVocê deve digitar um número.')
    
    def to_withdraw(self, number):
        if float(number):
            self.__balance -= float(number)
            return print(f'Você sacou {number}R$')
        return print('Erro... \nVocê deve digitar um número.')
    
    def show_balance(self):
        return print(f'Seu saldo atual é {self.__balance}R$')