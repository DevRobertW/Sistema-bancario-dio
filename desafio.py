# Define o menu de opções para o usuário escolher a operação desejada
menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

# Inicializa as variáveis essenciais para o funcionamento do sistema bancário
saldo = 0                    # Saldo inicial da conta
limite = 500                 # Limite máximo para cada saque
extrato = []                 # Lista para armazenar as movimentações (depósitos e saques)
numero_saques = 0            # Contador de saques realizados
LIMITE_SAQUES = 3            # Limite máximo de saques permitidos por dia

# Inicia o loop principal do programa, que continuará até o usuário escolher sair
while True:
    # Solicita ao usuário que escolha uma das opções do menu
    opcao = input(menu)

    # Se o usuário escolher 'd', a opção de depósito é selecionada
    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        # Verifica se o valor informado para o depósito é positivo
        if valor > 0:
            saldo += valor                           # Adiciona o valor depositado ao saldo
            extrato.append(f"Depósito: R$ {valor:.2f}")  # Registra o depósito no extrato
        else:
            print("Operação falhou! O valor informado é inválido.")  # Informa erro em caso de valor inválido

    # Se o usuário escolher 's', a opção de saque é selecionada
    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        # Verifica se o saque pode ser realizado conforme as regras definidas
        excedeu_saldo = valor > saldo                # Verifica se o valor do saque excede o saldo disponível
        excedeu_limite = valor > limite              # Verifica se o valor do saque excede o limite permitido
        excedeu_saques = numero_saques >= LIMITE_SAQUES  # Verifica se o número máximo de saques foi atingido

        # Aplica as regras para decidir se o saque pode ou não ser realizado
        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")
        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")
        elif valor > 0:
            saldo -= valor                           # Deduz o valor sacado do saldo
            extrato.append(f"Saque: R$ {valor:.2f}")  # Registra o saque no extrato
            numero_saques += 1                       # Incrementa o contador de saques realizados
        else:
            print("Operação falhou! O valor informado é inválido.")  # Informa erro em caso de valor inválido

    # Se o usuário escolher 'e', a opção de extrato é selecionada
    elif opcao == "e":
        print("\n================ EXTRATO ================")
        
        # Verifica se houve movimentações e exibe o extrato
        if not extrato:
            print("Não foram realizadas movimentações.")  # Informa se não houve movimentações
        else:
            for movimentacao in extrato:
                print(movimentacao)                      # Exibe cada movimentação registrada
        
        print(f"\nSaldo: R$ {saldo:.2f}")                 # Exibe o saldo atual da conta
        print("==========================================")

    # Se o usuário escolher 'q', o programa será encerrado
    elif opcao == "q":
        break   # Encerra o loop e finaliza o programa

    # Se o usuário inserir uma opção inválida, o programa solicita que escolha novamente
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
