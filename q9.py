'''Leia uma matriz 4 x 4. Calcule a soma dos elementos que estão abaixo da diagonal
principal. Não use comandos nem funções do python ou de suas bibliotecas que já façam
isso.'''

matriz = [
    [1, 5, 3, 2], #i = 0 j = null
    [4, 9, 7, 6], #i = 1 j = i - 1
    [8, 3, 2, 0], #i = 2 j = i - 2
    [1, 2, 6, 4]  #i = 3 j = i - 3
]

def calcular_matriz(matriz):
    soma = 0

    for i in range(4):
        for j in range(0, i):
            soma += matriz[i][j]
            print(matriz[i][j])
    
    return soma

print(calcular_matriz(matriz))