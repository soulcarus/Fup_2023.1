'''Faça um programa que preenche uma matriz de tamanho nxn com o produto do valor da
linha e da coluna de cada elemento. Em seguida, imprima na tela a matriz, em forma de
tabela.'''

def criar_matriz_produto(n):
    matriz = []
    for i in range(n):
        linha = []
        for j in range(n):
            valor = (i + 1) * (j + i)
            linha.append(valor)
        matriz.append(linha);
    return matriz

def exibir_matriz(matriz):
    for linha in matriz:
        for valor in linha:
            print(f' {valor} ', end="")
        print()

n = int(input("Digite o valor de n: "))

matriz = criar_matriz_produto(n);

exibir_matriz(matriz);