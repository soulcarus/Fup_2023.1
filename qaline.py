import random

def matriz(m, n, semente, intervalo):
    random.seed(semente)
    matriz = []
    for i in range(m):
        linha = []
        for j in range(n):
            num = random.randint(inicio_intervalo, fim_intervalo)
            linha.append(num)
        matriz.append(linha)

    return matriz

m = int(input())
n = int(input())
semente = int(input())
inicio_intervalo = int(input())
fim_intervalo = int(input())
intervalo = (inicio_intervalo, fim_intervalo)
matrizaleatoria = matriz(m, n, semente, intervalo)

def media_cada_linha_par(m, matrizaleatoria):

    somaelemento = 0
    qntelementos = 0
	
    for m in range(len(matrizaleatoria)):
        if m % 2 ==0:
            for elemento in range(m):
                somaelemento += elemento
                qntelementos += 1
                media = somaelemento / qntelementos
    
    return media

medlinhapar = media_cada_linha_par(m, matrizaleatoria)

def contar_negativos_divisiveis_por_3(matrizaleatoria):

    qntnegsdiv3 = 0

    for linha in range(len(matrizaleatoria)):
        if linha % 2 != 0:
            for elemento in range(len(matrizaleatoria[0])):
                if matrizaleatoria[linha][elemento] < 0 and matrizaleatoria[linha][elemento] % 3 == 0:
                    qntnegsdiv3 += 1

    return qntnegsdiv3

qntnegsdiv3 = contar_negativos_divisiveis_por_3(matrizaleatoria) 

for linha in matrizaleatoria:
	print(*linha)

for linha in matrizaleatoria:
	print(medlinhapar)

for linha in matrizaleatoria:
	print(qntnegsdiv3)
        
