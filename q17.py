def ler_matriz():
    matriz = []
    for i in range(12):
        linha = []
        for j in range(13):
            valor = float(input())
            linha.append(valor)
        matriz.append(linha)
    return matriz

def é_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def dividir_primo(matriz):
    matriz_modificada = []
    for i in range(len(matriz[0])):
        coluna = [linha[i] for linha in matriz] 
        ''' CRIAR UMA COLUNA PARA CADA LINHA NA MATRIZ'''
        primos = [x for x in coluna if é_primo(abs(x))]
        if len(primos) > 0:
            max_primo = max(primos)
            coluna_modificada = [elemento / max_primo for elemento in coluna]
        else:
            min_valor = min(coluna)
            coluna_modificada = [elemento / min_valor for elemento in coluna]
        matriz_modificada.append(coluna_modificada)
    matriz_modificada = [[linha[i] for linha in matriz_modificada] for i in range(len(matriz_modificada[0]))]
    return matriz_modificada

def imprimir_matriz(matriz):
    for linha in matriz:
        for valor in linha:
            print(f"{valor:8.2f}", end="")
        print()

matriz = ler_matriz()
matriz_modificada = dividir_primo(matriz)
#print("Matriz original:")
imprimir_matriz(matriz)
#print("Matriz modificada:")
imprimir_matriz(matriz_modificada)
