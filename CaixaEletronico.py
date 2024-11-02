# Função para exibir o menu e chamar as operações
def menu():
    print("\nEscolha uma das opções:")
    print("1) Saldo")
    print("2) Extrato")
    print("3) Saque")
    print("4) Depósito")
    print("5) Transferência")
    print("6) Sair")
    return input("Digite a opção desejada: ")

# Função para pedir e validar a senha
def validar_senha():
    senha = input("Digite sua senha: ")
    return senha == "3589"

# Função para exibir erro para opções inválidas
def erro():
    print("Opção inválida. Tente novamente.")

# Função para saudar o usuário ao acessar o sistema
def boas_vindas():
    nome = input("Digite seu nome: ")
    print(f"Olá {nome}, é um prazer ter você por aqui!")
    return nome

# Função para exibir o saldo com validação de senha
def exibir_saldo(saldo):
    if validar_senha():
        print(f"Seu saldo atual é: R${saldo:.2f}")
    else:
        print("Senha incorreta.")

# Função para exibir o extrato
def exibir_extrato(extrato):
    if validar_senha():
        print("Extrato:")
        for item in extrato:
            print(item)
    else:
        print("Senha incorreta.")

# Função para realizar saque com validações
def realizar_saque(saldo):
    if validar_senha():
        valor = float(input("Digite o valor do saque: "))
        if valor <= 0:
            print("Operação não autorizada: valor inválido.")
        elif valor > saldo:
            print("Operação não autorizada: saldo insuficiente.")
        else:
            saldo -= valor
            print(f"Saque de R${valor:.2f} realizado com sucesso.")
    else:
        print("Senha incorreta.")
    return saldo

# Função para realizar depósito com validação
def realizar_deposito(saldo):
    valor = float(input("Digite o valor do depósito: "))
    if valor <= 0:
        print("Operação não autorizada: valor inválido.")
    else:
        saldo += valor
        print(f"Depósito de R${valor:.2f} realizado com sucesso.")
    return saldo

# Função para realizar transferência com validações
def realizar_transferencia(saldo):
    if validar_senha():
        conta = input("Digite o número da conta de destino: ")
        if not conta.isdigit():
            print("Operação não autorizada: número de conta inválido.")
            return saldo

        valor = float(input("Digite o valor da transferência: "))
        if valor <= 0:
            print("Operação não autorizada: valor inválido.")
        elif valor > saldo:
            print("Operação não autorizada: saldo insuficiente.")
        else:
            saldo -= valor
            print(f"Transferência de R${valor:.2f} para a conta {conta} realizada com sucesso.")
    else:
        print("Senha incorreta.")
    return saldo

# Função principal do caixa eletrônico
def caixa_eletronico():
    saldo = 5000.0  # Saldo inicial fictício
    extrato = [
        "Depósito inicial: R$5000.00",
        "Compra: Supermercado R$200.00",
        "Compra: Padaria R$50.00",
        "Depósito: R$1000.00"
    ]  # Extrato fictício para consulta
    nome = boas_vindas()

    while True:
        opcao = menu()

        if opcao == "1":
            exibir_saldo(saldo)
        elif opcao == "2":
            exibir_extrato(extrato)
        elif opcao == "3":
            saldo = realizar_saque(saldo)
        elif opcao == "4":
            saldo = realizar_deposito(saldo)
        elif opcao == "5":
            saldo = realizar_transferencia(saldo)
        elif opcao == "6":
            print(f"{nome}, foi um prazer ter você por aqui!")
            break
        else:
            erro()

# Executa o programa
caixa_eletronico()
