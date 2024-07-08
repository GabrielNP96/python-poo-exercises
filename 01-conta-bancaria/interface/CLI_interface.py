from models.bank_account import Bank_acount


def cli_interface():

    user_name = input('Digite seu nome: ')
    user_balance = int(input('Saldo inicla da sua conta bancária: '))
    i = True
    while i == True:
        print('Opções:\n Digite 1 para depositar dinheiro\nDigite 2 para sacar\nDigite 3 para ver o saldo.')