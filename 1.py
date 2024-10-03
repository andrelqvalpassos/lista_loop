# Função para analisar as idades
def analisar_idade():
    # Inicializando variáveis e listas para armazenar os dados
    idades = []
    qtd_maior_ou_igual_25 = 0
    qtd_menor_que_25 = 0
    
    # Loop para coletar as idades até o usuário digitar -1
    while True:
        idade = int(input("Digite uma idade (ou -1 para encerrar): "))
        
        if idade == -1:
            break  # Encerra a entrada de dados quando -1 for digitado
        
        if idade >= 0:  # Considera apenas idades válidas
            idades.append(idade)
            if idade >= 25:
                qtd_maior_ou_igual_25 += 1
            else:
                qtd_menor_que_25 += 1
    
    # Verifica se há idades válidas para realizar os cálculos
    if idades:
        total_idades = len(idades)
        media_idades = sum(idades) / total_idades
        maior_idade = max(idades)
        menor_idade = min(idades)

        # Exibe os resultados
        print("\nAnálise das idades:")
        print(f"Total de idades válidas digitadas: {total_idades}")
        print(f"Média das idades: {media_idades:.2f}")
        print(f"Quantidade de idades >= 25: {qtd_maior_ou_igual_25}")
        print(f"Quantidade de idades < 25: {qtd_menor_que_25}")
        print(f"Maior idade: {maior_idade}")
        print(f"Menor idade: {menor_idade}")
    else:
        print("Nenhuma idade válida foi digitada.")

# Chamada da função para executar o programa
analisar_idade()
