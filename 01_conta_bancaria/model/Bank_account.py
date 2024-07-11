from Agency import Agency

class Bank_account(Agency):
    def __init__(self,name, address, number, holder, balalce):
        super().__init__(name, address, number)
        self._holder = holder
        self._balance = balalce


    def __str__(self):
        return f'Nome do banco: {self._name}\nEndereço do Banco: {self._address}\nNúmero da agência: {str(self._number)}\nTitular da conta: {self._holder}\nSaldo: {str(self._balance)}R$\n'

    def deposit(self,number):
        if float(number):
           self._balance += float(number)
           return print(f'Você depositou {number}R$\n')
        return print('Erro... \nVocê deve digitar um número.')
    
    def to_withdraw(self, number):
        if float(number):
            self._balance -= float(number)
            return print(f'Você sacou {number}R$\n')
        return print('Erro... \nVocê deve digitar um número.')
    
    def show_balance(self):
        return print(f'Seu saldo atual é {self._balance}R$\n')

my_account = Bank_account('Siveirinha', 'Gotham', 1, 'Tim Drake', 7000)
print(my_account)

my_account.deposit(15000)
my_account.to_withdraw(1100)
my_account.show_balance()