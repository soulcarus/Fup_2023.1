'''Faça um programa que permita ao usuário entrar com uma matriz de 5 x 5 números reais.
Em seguida, gere um vetor unidimensional contendo a soma dos números de cada coluna da
matriz e mostre na tela esse vetor.'''

def ler_matriz():
    matriz = []
    print("Digite os valores da matriz:")
    for i in range(5):
        linha = []
        for j in range(5):
            valor = float(input("Digite um valor: "))
            linha.append(valor)
        matriz.append(linha)
    return matriz

def gerar_vetor_soma_colunas(matriz):
    vetor_soma_colunas = [0] * 5
    for i in range(5):
        for j in range(5):
            vetor_soma_colunas[j] += matriz[i][j]
    return vetor_soma_colunas

matriz = ler_matriz()
vetor_soma_colunas = gerar_vetor_soma_colunas(matriz)

print("Vetor de soma das colunas:")
print(vetor_soma_colunas)
