'''Faça um programa que carregue uma matriz 12 x 13 e divida todos os elementos de cada
linha pelo maior elemento em módulo daquela linha. Escreva a matriz original e a
modificada.'''

def ler_matriz():
    matriz = []
    print("Digite os valores da matriz:")
    for i in range(12):
        linha = []
        for j in range(13):
            valor = float(input("Digite um valor: "))
            linha.append(valor)
        matriz.append(linha)
    return matriz

def dividir_maior(matriz):
    matriz_modificada = []
    for linha in matriz:
        maior_elemento = max(map(abs, linha))
        linha_modificada = [elemento / maior_elemento for elemento in linha]
        matriz_modificada.append(linha_modificada)
    return matriz_modificada

matriz = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],
    [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13],
    [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26],
    [-2, -4, -6, -8, -10, -12, -14, -16, -18, -20, -22, -24, -26],
    [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39],
    [-3, -6, -9, -12, -15, -18, -21, -24, -27, -30, -33, -36, -39],
    [4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52],
    [-4, -8, -12, -16, -20, -24, -28, -32, -36, -40, -44, -48, -52],
    [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65],
    [-5, -10, -15, -20, -25, -30, -35, -40, -45, -50, -55, -60, -65],
    [6, 12, 18, 24, 30, 36, 42, 48, 54, 60, 66, 72, 78],
    [-6, -12, -18, -24, -30, -36, -42, -48, -54, -60, -66, -72, -78]
]
  
matriz_modificada = dividir_maior(matriz)

def printar_matriz(matriz):

    for linha in matriz:
        for valor in linha:
            print(f"{valor:8.2f}", end="")
        print()

printar_matriz(matriz_modificada)