# Função para contar as solicitações de cada serviço
def contar_solicitacoes():
    # Inicializando os contadores
    banho = 0
    tosa = 0
    banho_e_tosa = 0
    outros = 0

    # Solicitando o código do serviço para 10 cachorros
    for i in range(1, 11):
        print(f"\nCachorro {i}:")
        servico = input("Digite o código do serviço (1 - Banho; 2 - Tosa; 3 - Banho e Tosa; 4 - Outros): ")

        # Verifica o código do serviço e atualiza o contador correspondente
        if servico == '1':
            banho += 1
        elif servico == '2':
            tosa += 1
        elif servico == '3':
            banho_e_tosa += 1
        elif servico == '4':
            outros += 1
        else:
            print("Código inválido! Tente novamente.")
            i -= 1  # Repete a solicitação caso o código seja inválido

    # Exibe a quantidade de solicitações para cada serviço
    print("\nResumo das solicitações:")
    print(f"Banho: {banho} solicitação(ões)")
    print(f"Tosa: {tosa} solicitação(ões)")
    print(f"Banho e Tosa: {banho_e_tosa} solicitação(ões)")
    print(f"Outros: {outros} solicitação(ões)")

# Chamada da função para executar o programa
contar_solicitacoes()
