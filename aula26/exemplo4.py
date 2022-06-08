import re


def calculomedia(lista):
    soma=0
    for valor in lista:
        soma+=valor
    return float(soma/len(lista))

def calculodivisaopadrao(lista):
    n=len(lista)
    m=calculomedia(lista)
    soma=0
    from math import pow , sqrt
    for valor in lista:
        soma+=pow(valor-m,2)
    return sqrt(1/(n-1)*soma)

lista=[3,6,2,9,10,45,36,78,42,100]

print(calculodivisaopadrao(lista))