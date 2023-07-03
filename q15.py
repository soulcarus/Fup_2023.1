'''Faça um programa que leia duas matrizes A e B de tamanho 5 x 5 cada uma. Calcule a
matriz C = A * B. Não use comandos nem funções do python ou de suas bibliotecas que já
façam isso.'''

def ler_matriz():
    matriz = []
    print("Digite os valores da matriz:")
    for i in range(5):
        linha = []
        for j in range(5):
            valor = float(input("Digite um valor: "))
            linha.append(valor)
        matriz.append(linha)
    return matriz

matriz1 = ler_matriz()  
matriz2 = ler_matriz()

def multiplicar_matrizes(matriz1, matriz2):
    matriz_c = [[0 for i in range(5)] for j in range(5)]

    for i in range(5):
        for j in range(5):
            for k in range(5):
                matriz_c[i][j] += matriz1[i][k] * matriz2[k][j]
    return matriz_c

def printar_matriz(matriz):

    for linha in matriz:
        for valor in linha:
            print(f" {valor} ", end="")
        print()

matriz_c = multiplicar_matrizes(matriz1, matriz2)
printar_matriz(matriz_c)