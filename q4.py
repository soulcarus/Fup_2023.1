'''Leia uma matriz 4 × 4, imprima a matriz, imprima a localização (linha e coluna) do maior
valor e imprima o maior valor.'''

def criar_matriz(n):
    matriz = []
    for i in range(n):
        linha = []
        for j in range(n):
            valor = int(input(f"Digite o valor da posição [{i}][{j}]: "));
            linha.append(valor);
        matriz.append(linha);
    
    return matriz

def encontrar_maior_valor(matriz):
    maior_valor = matriz[0][0]
    linha_maior_valor = 0
    coluna_maior_valor = 0

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] > maior_valor:
                maior_valor = matriz[i][j]
                linha_maior_valor = i + 1
                coluna_maior_valor = j + 1

    return linha_maior_valor, coluna_maior_valor, maior_valor

def exibir_matriz(matriz):
    for linha in matriz:
        for valor in linha:
            print(f" {valor} ", end="")
        print()

n = 4;

matriz = criar_matriz(n);
exibir_matriz(matriz);

linha_maior, coluna_maior, maior_valor = encontrar_maior_valor(matriz)

print(f"\nMaior valor: {maior_valor} com posição: [{linha_maior}][{coluna_maior}]")