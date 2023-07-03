'''Faça um programa que gere uma matriz m × n de inteiros aleatórios. Mostre a matriz e
calcule e mostre a média dos elementos das linhas pares da matriz e a quantidade de
números negativos e divisíveis por 3 das linhas ímpares da matriz. A quantidade de linhas m,
a quantidade de colunas n, a semente dos números aleatórios e o intervalo de geração serão
dados como entrada para o programa.'''

import random

def gerar_matriz(m, n, semente, valor_min, valor_max):
    random.seed(semente)
    matriz = []
    matriz = [[random.randint(valor_min, valor_max) for j in range(n)] for i in range(m)]
    return matriz



def calcular_media(matriz):
    total = 0
    contagem = 0
    for i in range(len(matriz)):
        if i % 2 == 0:
            total += sum(matriz[i])
            contagem += len(matriz[i])
    return total / contagem

def contar_negativos_divisiveis_por_3(matriz):
    contagem = 0
    for i in range(len(matriz)):
        if i % 2 == 1:
            for j in range(len(matriz[0])):
                if matriz[i][j] < 0 and matriz[i][j] % 3 == 0:
                    contagem += 1
    return contagem

def imprimir_matriz(matriz):
    for linha in matriz:
        for valor in linha:
            print(f"{valor:4}", end="")
        print()

m = int(input("Digite a quantidade de linhas: "))
n = int(input("Digite a quantidade de colunas: "))
semente = int(input("Digite a semente dos números aleatórios: "))
valor_min = int(input("Digite o valor mínimo: "))
valor_max = int(input("Digite o valor máximo: "))

matriz = gerar_matriz(m, n, semente, valor_min, valor_max)
media = calcular_media(matriz)
contagem_negativos_divisiveis_por_3 = contar_negativos_divisiveis_por_3(matriz)

print("Matriz:")
imprimir_matriz(matriz)
print(f"Média dos elementos das linhas pares: {media:.2f}")
print(f"Quantidade de números negativos e divisíveis por 3 nas linhas ímpares: {contagem_negativos_divisiveis_por_3}")
