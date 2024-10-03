def controlar_estoque():
    # Inicializa um dicionário para armazenar os produtos e suas quantidades
    media = {}

    for nota in range(5):
        print(f"Digite sua nota para o produto de 1 a 5{nota}: ")
    if nota < 6 :
        print("Nota valida")
    else:
        print("Nota invalida, tente novamente")

    nota_media = nota / 5

    print(f"a media do produto e: {nota_media:.2f}")