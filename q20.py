'''Na matriz de 20 × 20 abaixo, quatro números ao longo de uma diagonal foram marcados em
negrito. O produto desses números é 26 × 63 × 78 × 14 = 1788696. Qual é o maior produto
de quatro números adjacentes em qualquer direção (vertical, horizontal ou diagonal) na
matriz de 20 × 20? A matriz 20 × 20 será dada como entrada, e o programa deve exibir o
valor da multiplicação, a posição (linha e coluna) de onde começam os números, e a direção
(cima, baixo, esquerda, direita, direita cima, esquerda cima, direita baixo, esquerda baixo).
No caso da matriz abaixo, o maior número é 89 × 94 × 97 × 87 = 70600674, começando na
posição de linha 12 e coluna 6, e na diagonal esquerda baixo.'''


import random

def max_product(matrix):
    max_product = 0
    max_coords = None
    max_direction = None
    directions = {
        "right": (0, 1),
        "down": (1, 0),
        "down-right": (1, 1),
        "down-left": (1, -1)
    }
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            for direction, (di, dj) in directions.items():
                try:
                    product = matrix[i][j] * matrix[i+di][j+dj] * matrix[i+2*di][j+2*dj] * matrix[i+3*di][j+3*dj]
                    if product > max_product:
                        max_product = product
                        max_coords = (i, j)
                        max_direction = direction
                except IndexError:
                    pass
    return max_product, max_coords, max_direction

matrix = [[random.randint(0, 99) for j in range(20)] for i in range(20)]
max_prod, coords, direction = max_product(matrix)
#print("Max product:", max_prod)
#print("Starting coordinates:", coords)
#print("Direction:", direction)
print(max_prod)
print(coords)
print(direction)