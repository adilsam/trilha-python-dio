# Criar um sistema bancário com as operações: sacar, depositar e visualizar extrato.
# Todos os depósitos e saques devem ser armazenados em uma variável e exibidos na operação de extrato.
#
# Regras de negócio:
"""
    TODO: permitir realizar 3 saques diários. Onde o limite máximo de R$ 500,00 por saque.
    TODO: se não tiver saldo em conta, exibir uma mensagem informando que não será possível sacar o dinheiro
    TODO: O extrato deve exibir o saldo atual da conta. 
    TODO: Se não existir movimentações, exibir a mensagem: "Não foram realizadas movimentações."
"""
menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
movimento = 0

while True:

    opcao = input(menu)

    if opcao == "1":
        deposito = float(input("Entre com o valor do depósito: "))
        saldo += deposito
        movimento += 1
        extrato += f"Depósito: R$ {deposito:.2f}\n"
        print("Depósito realizado com sucesso")
    elif opcao == "2":
        saque = float(input("Entre com o valor do saque: "))
        if (saque > saldo):
            print(f"Saque não realizado. Saldo insuficiente. Saldo: R$ {saldo:.2f}")
            continue
        elif (numero_saques == LIMITE_SAQUES):
            print("Saque não realizado. Excedeu Limite para 3 Saques.")
            continue
        elif (saque > limite):
            print("Saque não realizado. Excedeu Limite para de 500 reais para Sacar.")
            continue
        saldo -= saque
        numero_saques += 1
        movimento += 1
        extrato += f"Saque: R$ {saque:.2f}\n"
        print ("Saque realizado com sucesso")
    elif opcao == "3":
        print("\n================ EXTRATO ================")
        if movimento != 0:
            print(extrato)
            print(f"\nSaldo: R$ {saldo:.2f}")
        else:
            print (f"Saldo Atual: R$ {saldo:.2f}")
            print("Não houve movvimentações nessa conta.")
        print("==========================================")
    elif opcao == "0":
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")