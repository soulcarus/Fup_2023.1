'''Leia uma matriz 4 x 4. Calcule a soma dos elementos que estão na diagonal secundária. Use
apenas um comando de repetição. Não use comandos nem funções do python ou de suas
bibliotecas que já façam isso.'''

matriz = [
    [1, 5, 3, 2], #i = 0 j = 3
    [4, 9, 7, 6], #i = 1 j = 2
    [8, 3, 2, 0], #i = 2 j = 1
    [1, 2, 6, 4]  #i = 3 j = 0
]


def calcular_matriz(matriz):
    soma = 0

    for i in range(4):
        for j in range(4):
            if (i + j) == 3:
                soma += matriz[i][j]
    
    return soma

print(calcular_matriz(matriz))