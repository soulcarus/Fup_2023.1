'''Gere uma matriz 5 × 5 com inteiros aleatórios no intervalo [1, 20], encontrados a partir de
uma semente dada como entrada. Escreva um programa que transforme a matriz geradanuma matriz triangular inferior, ou seja, atribuindo zero a todos os elementos acima da
diagonal principal. Imprima a matriz original e a matriz transformada. Não use nenhum
comando de decisão (se/então/senão).'''

import random

def gerar_matriz(seed):
    random.seed(seed)
    matriz = []
    for j in range(5):
        for i in range(5):
            matriz.append(random.randint(1, 20))
    return matriz

def triangular_inferior(matriz):
    for i in range(len(matriz)):
        for j in range(i+1, len(matriz[0])):
            matriz[i][j] = 0
    return matriz

def imprimir_matriz(matriz):
    for linha in matriz:
        for valor in linha:
            print(f"{valor:4}", end="")
        print()

seed = int(input("Digite a semente: "))
matriz = gerar_matriz(seed)
print("Matriz original:")
imprimir_matriz(matriz)
matriz_triangular = triangular_inferior(matriz)
print("Matriz triangular inferior:")
imprimir_matriz(matriz_triangular)



#resultado = [numero for numero in range(100) if numero % 5 == 0 if numero % 6 == 0]