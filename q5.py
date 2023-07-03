'''Leia uma matriz 5 × 5. Leia também um valor X. O programa deverá fazer uma busca desse
valor na matriz e, ao final, escrever a localização (linha e coluna) ou uma mensagem de
"Nao encontrado".'''

def criar_matriz():
    matriz = []

    for i in range(5):
        linha = []
        for j in range(5):
            valor = int(input(f"Digite o valor da posição [{i}][{j}]: "));
            linha.append(valor)
        matriz.append(linha)
    
    return matriz

def ler_matriz(matriz):
    for linha in matriz:
        for valor in linha:
            print(f" {valor} ", end='')
        print()

def procurar_valor(matriz, x):
    
    linha = 0
    coluna = 0

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == x:
                linha = i + 1
                coluna = j + 1
    
    return linha, coluna

x = int(input("Insira qual numero irá buscar!"))
#matriz = criar_matriz()

matriz = [
    [1, 5, 3, 2],
    [4, 9, 7, 6],
    [8, 3, 2, 0],
    [1, 2, 6, 4]
]

linha, coluna = procurar_valor(matriz, x)   
ler_matriz(matriz)

print(f"Posição do elemento {x}: [{linha}][{coluna}]")