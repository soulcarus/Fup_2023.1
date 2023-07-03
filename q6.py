# Função para criar uma matriz 4x4
def criar_matriz_zeros():
    matriz = []
    for i in range(4):
        linha = [0] * 4
        matriz.append(linha)
    return matriz

# Função para ler uma matriz 4x4
def ler_matriz():
    matriz = criar_matriz_zeros()
    print("Digite os valores da matriz:")
    for i in range(4):
        for j in range(4):
            valor = int(input(f"Digite o valor para a posição [{i}][{j}]: "))
            matriz[i][j] = valor
    return matriz

# Função para criar uma terceira matriz com os maiores valores de cada posição
def criar_matriz_maiores(matriz1, matriz2):
    matriz_maiores = criar_matriz_zeros()
    for i in range(4):
        for j in range(4):
            valor1 = matriz1[i][j]
            valor2 = matriz2[i][j]
            maior_valor = valor1 if valor1 > valor2 else valor2
            matriz_maiores[i][j] = maior_valor
    return matriz_maiores

# Função para exibir uma matriz
def exibir_matriz(matriz):
    for linha in matriz:
        for valor in linha:
            print(f"{valor:2d}", end=' ')
        print()

# Lendo as duas matrizes
print("Matriz 1:")
matriz1 = ler_matriz()
print("\nMatriz 2:")
matriz2 = ler_matriz()

# Criando a terceira matriz com os maiores valores
matriz_maiores = criar_matriz_maiores(matriz1, matriz2)

# Exibindo a terceira matriz
print("\nTerceira matriz (maiores valores):")
exibir_matriz(matriz_maiores)
