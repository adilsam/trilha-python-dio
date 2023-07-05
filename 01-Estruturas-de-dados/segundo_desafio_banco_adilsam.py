#
# Potência Tech powered by iFood | Ciências de Dados com Python
# Otimização do Sistema de Banco de Dados. 
# Por Adilson Sampaio - Julho/2023

# Otimizar o sistema bancário com as operações: sacar, depositar e visualizar extrato.
# Todos os depósitos e saques devem ser armazenados em uma variável e exibidos na operação de extrato.
#
# Regras de negócio:
"""
    TODO: permitir realizar uma quantidade de saques diários. E há um limite máximo para saque.
    TODO: se não tiver saldo em conta, exibir uma mensagem informando que não será possível sacar o dinheiro
    TODO: O extrato deve exibir o saldo atual da conta. 
    TODO: Se não existir movimentações, exibir a mensagem: "Não foram realizadas movimentações."
"""

### Definições de Variáveis

CORRENTE = ("Corrente", 1000, 4)    # Definição de vários tipos de Conta. Tuplas com o valor
ESPECIAL = ("Especial", 2000, 5)    # limite para um único saque e o número de operações possíveis de saque.
POUPANCA = ("Poupança", 500, 3)
clientes = []                       # lista armazena os clientes do banco
NUM_CONTA = 1                       # sequencial que define o número da conta
extrato = []
menu = """

            [1] Criar Usuário
            [2] Cadastrar Conta 
            [3] Depositar
            [4] Sacar
            [5] Extrato
            [0] Sair

                        Digite a sua Opção => """

### FUNÇÕES 


def definir_cliente(op=""):
# faz a busca por um CPF existente retornando os dados do Usuários.
# Caso não exista permite criar um novo Usuário.
# Saida: um cliente (uma Lista).
# Entrada: não tem argumentos.
    send_cpf = str(input("\nDigite o CPF: "))
    # saber se o cpf já esta no sistema   
    cliente_filtro = [cada_cliente for  cada_cliente in clientes if cada_cliente["cpf"] == send_cpf]
    if  cliente_filtro: return cliente_filtro[0] 
    elif op == 1:
        return novo_cliente(send_cpf)
    else:
        print("CPF informado não pertence a um cliente do Banco. \n ")
        resp = str(input("Deseja incluir o novo Cliente? (S/N): ")).strip().upper()
        if resp[0] == "S": 
            return novo_cliente(send_cpf)
        

def novo_cliente(novo_cpf= ""):
# A função inclui um novo Cliente do  banco no programa.
# Entrada: parâmetro opcional é o número do CPF. 
#          Se for uma string vazia a opção escolhida foi o Cadastro de um novo Cliente.
#          Caso contrário se esta tentando incluir a Conta de um Cliente cadastrado.
#
    if novo_cpf == "": novo_cpf = str(input("\nDigite o CPF: "))
    nome = str(input("Digite o nome: ")).strip()
    data_n = str(input("Informe a data de nascimento: ")).strip()
    rua = str(input("Rua: ")).strip()
    numero = str(input("Número: ")).strip()
    bairro = str(input("Bairro: ")).strip()
    cidade = str(input("Cidade : ")).strip()
    estado = str(input("Estado: ")).split()
    address = [rua, numero, bairro, cidade, estado]
    contas = []
    qtd_saque = 0
    novo_cliente = {"nome":nome, "nasc": data_n, "cpf": novo_cpf, 
                    "end": address, "contas": contas, "qtd_saque": qtd_saque}
    clientes.append(novo_cliente)
    print("\nNovo Cliente cadastrado com sucesso.")
    return novo_cliente


def nova_conta(ncont):
    # função cria uma nova conta pra um cliente do banco. 
    # Caso o cliente não esteja inserido essa # ação pode ser feita. 
    # É possível criar 3 tipos de contas Corrente, Especial e de Poupança.
    # Cada tipo com um limite e uma quantidade sw saques possíveis.
    # Não Há Entrada ou Saída para essa função.

    cli = definir_cliente() #definir o usuário da nova conta.
    if cli:
        agencia = "001"
        numero = ncont 
        saldo = 0.0
        q_saques = 0
        user_conta_tipo = ()
        movimento = []
        resp_tipo = str(input("A Conta é: C - Corrente, E - Especial ou P - Poupança ? ")).upper()
        match resp_tipo:                     # define o Tipo da Conta. 
            case "C":                           # Estabelecendo o número de saques, 
                user_conta_tipo = CORRENTE      # o limite para cada saque e o Tipo da Conta
            case "E":
                user_conta_tipo = ESPECIAL
            case "P":
                user_conta_tipo = POUPANCA
        tipo = user_conta_tipo
        nova_conta =  [agencia, numero, tipo, saldo, q_saques, movimento]  
        cli["contas"].append(nova_conta)   # adiciona a conta criada ao cliente definido
        print(f"\nNova conta do Cliente {cli['nome']}  e do tipo {nova_conta[2][0]} cadastrado com sucesso.")
        return 

    
def listar_contas(cli):
    # função lista a conta dos clientes dentro das Operações de sacar e depositar.
    # Entrada: os dados de um cliente em uma Lista.
    print(f"As Contas do Cliente: {cli['nome']} CPF: {cli['cpf']}")
    if len(cli['contas']) > 0:
        print("Número      Tipo        Saldo")
        for c in cli["contas"]:
            print(c[1], "\t   ", c[2][0], "\t R$ ", c[3])
    else: print ("Não há contas para esse cliente.") 
    return 


def sacar(*,  extrato, nome, conta):
    # Responsável pelo saque. Entrada do valor, teste de condições relacionada com a operação
    # e atualização do saldo da conta.

    saque = float(input("Entre com o valor do saque: ")) # estabelece o valor
    if (saque > conta[3]):  # se o saque é maior que o saldo
        print(f"Saque não realizado. Saldo insuficiente. Saldo: R$ {conta[3]:.2f}")
        return
    elif (conta[4] >= conta[2][2]): # se a qtd saques esta dentro do limite para o tipo de conta
        print(f"Saque não realizado. Excedeu Limite para {conta.tipo[2]} Saques.")
        return
    elif (saque > conta[2][1]): # se o saque esta dentro do limite para saque
        print(f"Saque não realizado. Excedeu Limite para de {conta[2][1]} reais para Sacar.")
        return
    conta[3] -= saque # atualiza o saldo que esta na terceira posição
    conta[4] += 1
    op = len(extrato)
    feito_global = f"{op} - Cliente: {nome} - conta: {conta[1]} - Saque: R$ {saque:.2f}"
    feito_conta = f"{op} - Saque: R$ {saque:.2f}"
    extrato.append(feito_global)
    conta[5].append(feito_conta)
    print ("Saque realizado com sucesso")


def depositar(extrato, nome, conta, /):
    valor = float(input("Entre com o valor do Deposito: ")) # estabelece o valor
    conta[3] += valor
    op = len(extrato)
    feito_global = f"{op} - Cliente: {nome} - conta: {conta[1]} - Deposito: R$ {valor:.2f}"
    feito_conta = f"{op} - Deposito: R$ {valor:.2f}"
    extrato.append(feito_global)
    conta[5].append(feito_conta)
    print ("Deposito realizado com sucesso")

def mostra_extrato():
    for cliente in clientes:
        qtd_contas = len(cliente['contas'])
        print(f"\nNome: {cliente['nome']} CPF: {cliente['cpf']}")
        if len(cliente['contas']) > 0:
            print("\nNúmero      Tipo        Saldo")
            for conta in cliente["contas"]:
                print(conta[1], "\t   ", conta[2][0], "\t R$ ", conta[3])
                print("------------------------------------------------------------")
                print("Movimentações da Conta: ")
                for op in conta[5]:
                    print(op)

### PROGRAMA PRINCIPAL
while True:
        op = input(menu)
        cli = []

        if op == "1":
            cli = definir_cliente(1)
        elif op == "2": # criar conta
            nova_conta(NUM_CONTA)    
            NUM_CONTA += 1
        elif op == "3": # depositar
            cli = definir_cliente()
            if cli:
                listar_contas(cli)
                resp = int(input("\nQual conta você deseja depositar? "))
                conta_escolhida = [conta for  conta in cli['contas'] if conta[1] == resp]
                depositar(extrato, cli["nome"], conta_escolhida[0])
        elif op == "4": # 4 - sacar
            cli = definir_cliente()
            if cli:
                listar_contas(cli)
                resp = int(input("\nQual conta você deseja sacar? "))
                conta_escolhida = [conta for  conta in cli['contas'] if conta[1] == resp]
                sacar(extrato=extrato, nome=cli["nome"], conta=conta_escolhida[0])
        elif op == "5":
            mostra_extrato()
        elif op == "0":
            break
        else:
            print("\nOperação inválida, por favor selecione novamente a operação desejada.")
