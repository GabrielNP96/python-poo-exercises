from models.bank_account import Bank_acount


def cli_interface():
    i = True
    while i == True:
        user_name = input('Digite seu nome: ')
        user_balance = float(input('Saldo inicial da sua conta bancária: '))
        if len(user_name) > 0 and user_balance == float:
            user_bank_account = Bank_acount(user_name, user_balance)
            break
        else:
            print('Digite um nome de usuário e um saldo incial válido.')
    i = True
    while i == True:
       option =  int(input('Opções:\n Digite 1 para depositar dinheiro\nDigite 2 para sacar\nDigite 3 para ver o saldo\nDigite 4 para fechar o programa\nDigite aqui: '))

       match option:
           case 1:
               cash = float(input('Digite o valor que deseja depositar: '))
               Bank_acount.cash_deposit(cash)
               print(f'Deposito de R${cash} realizado.\n')
               continue
           case 2:
               cash = float(input('Digite o valor que deseja sacar: '))
               Bank_acount.withdraw_money(cash)
               print(f'Saque de R${cash} realizado.\n')
               continue
           case 3:
               Bank_acount.check_balance()
               continue
           case 4:
               print('programa encerrado...\n')
               break

cli_interface()