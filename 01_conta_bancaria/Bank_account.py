class Bank_acount:
    def __init__(self, holder_name, balance):
        self.holder_name = holder_name
        self.balance = float(balance)

    def cash_deposit(self,num):
        self.balance = self.balance + float(num)

        return print(f'O saldo é de R${self.balance} agora')
    
    def withdraw_money(self,number):
        self.balance = self.balance - float(number)

        return print(f'Você sacou R${number} e restou na sua conta ${self.balance}')
    
    def check_balance(self):
        return print(f'você tem R${self.balance}')
