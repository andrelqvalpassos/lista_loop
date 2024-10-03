def controlar_estoque():
    # Inicializa um dicionário para armazenar os produtos e suas quantidades
    estoque = {}

    while True:
        # Solicita o nome do produto
        produto = input("Digite o nome do produto (ou 'FIM' para encerrar): ")

        # Verifica se o usuário quer encerrar o programa
        if produto.upper() == "FIM":
            break

        # Solicita a quantidade do produto
        try:
            quantidade = int(input(f"Digite a quantidade de {produto}: "))

            # Verifica se a quantidade é negativa
            if quantidade < 0:
                print("Erro: A quantidade não pode ser negativa. Tente novamente.")
                continue

            # Adiciona ou atualiza o produto no dicionário
            if produto in estoque:
                estoque[produto] += quantidade
            else:
                estoque[produto] = quantidade
        except ValueError:
            print("Erro: Digite um número válido para a quantidade.")

    # Exibe o número de tipos de produtos inseridos
    print(f"\nVocê inseriu {len(estoque)} tipo(s) de produto(s).")

    # Exibe o estoque final
    for produto, quantidade in estoque.items():
        print(f"{produto}: {quantidade} unidades")

# Chama a função para executar o programa
controlar_estoque()

