'''Faça um programa que leia duas matrizes A e B de tamanho 4 x 5 cada uma. Calcule a
matriz C = A + B. Não use comandos nem funções do python ou de suas bibliotecas que já
façam isso.'''

def ler_matriz():
    matriz = []
    print("Digite os valores da matriz:")
    for i in range(4):
        linha = []
        for j in range(5):
            valor = float(input("Digite um valor: "))
            linha.append(valor)
        matriz.append(linha)
    return matriz

matriz1 = ler_matriz()
matriz2 = ler_matriz()

def somar_matrizes(matriz1, matriz2):
    matriz_c = []
    valor = 0

    for i in range(4):
        linha = []
        for j in range(5):
            valor = matriz1[i][j] + matriz2[i][j]
            linha.append(valor)
        matriz_c.append(linha)
    return matriz_c

def printar_matriz(matriz):

    for linha in matriz:
        for valor in linha:
            print(f" {valor} ", end="")
        print()

matriz3 = somar_matrizes(matriz1, matriz2)
printar_matriz(matriz3)