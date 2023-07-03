'''Leia um número n e crie uma matriz n×n. Preencha com 1 a diagonal principal e com 0 os
demais elementos. Escreva ao final a matriz obtida, em forma de tabela. Use comandos de
repetição.'''

n = int(input("Insira o valor para n: "));

matriz = []

for i in range(n):
    linha = []
    for j in range(n):
        if (i == j):
            linha.append(1);
        else:
            linha.append(0);
    matriz.append(linha);


for linha in matriz:
    for valor in linha:
        print(f" {valor} ", end="");
    print()


