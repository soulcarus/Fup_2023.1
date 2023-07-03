#Leia uma matriz 4 × 4 de inteiros, conte e escreva quantos valores maiores que 10 ela possui

def contar_valores(matriz):
    contador = 0;

    for linha in matriz:
        for valor in linha:
            if valor > 10:
                contador += 1;
    
    return contador

def ler_matriz():
    matriz = [];
    for i in range(4):
        linha = [];
        for j in range(4):
            valor = int(input(f"Digite o valor da posição [{i}][{j}]: "));
            linha.append(valor);
        matriz.append(linha);
    return matriz;

print("Digite os valos da matriz: ");
matriz = ler_matriz();

quantidade = contar_valores(matriz);

print(f"A matriz possui {quantidade} valores maior que 10");