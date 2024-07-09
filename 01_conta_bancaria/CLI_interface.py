from Bank_account import Bank_acount

def create_bank_account():
    i = True
    while i == True:
        try:
            user_name = input('Digite seu nome: ')
            user_balance = float(input('Saldo inicial da sua conta bancária: '))

            return Bank_acount(user_name, user_balance)
        except ValueError:
             print('Erro...\nValores inválidos...')
        


def cli_interface():
    user_bank_account = create_bank_account()
    i = True
    while i == True:
       option =  int(input('Opções:\n Digite 1 para depositar dinheiro\nDigite 2 para sacar\nDigite 3 para ver o saldo\nDigite 4 para fechar o programa\nDigite aqui: '))

       match option:
           case 1:
               cash = float(input('Digite o valor que deseja depositar: '))
               user_bank_account.cash_deposit(cash)
               print(f'Deposito de R${cash} realizado.\n')
               continue
           case 2:
               cash = float(input('Digite o valor que deseja sacar: '))
               user_bank_account.withdraw_money(cash)
               print(f'Saque de R${cash} realizado.\n')
               continue
           case 3:
               user_bank_account.check_balance()
               continue
           case 4:
               print('programa encerrado...\n')
               break
