def criar_matriz():
    matriz = []
    for i in range(1, 11):
        linha = []
        for j in range(1, 11):
            if i < j:
                elemento = 2 * i + 7 * j - 2
            elif i > j:
                elemento = 4 * i**3 - 5 * j**2 + 1
            elif i == j:
                elemento = 3 * i**2 - 1
            linha.append(elemento)
        matriz.append(linha)
    return matriz

def ver_matriz(matriz):
    for linha in matriz:
        for valor in linha:
            print(f"{valor:4}", end=" ")
        print()

matriz = criar_matriz()
ver_matriz(matriz)
