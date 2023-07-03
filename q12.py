'''Leia uma matriz 4 x 4. Calcule e imprima sua transposta. Não use comandos nem funções
do python ou de suas bibliotecas que já façam isso'''

matriz = [
    [1, 5, 3, 2], #i = 0 #j = 3
    [4, 9, 7, 6], #i = 1 #j = 2
    [8, 3, 2, 0], #i = 2 #j = 1
    [1, 2, 6, 4]  #i = 3 #j = 0
]

transp = [
    [1, 4, 8, 1],
    [5, 9, 3, 2],
    [3, 7, 2, 6],
    [2, 6, 0, 4 ]
]








def transpostar(matriz):
    
    nova_matriz = []

    for i in range(4):
        linha = []
        for j in range(4):
            linha.append(matriz[j][i])
        print(linha)
    

transpostar(matriz)
