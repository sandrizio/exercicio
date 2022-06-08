import random
def sorte():
    
    lista=[]

    l=0

    while l < 5:
        a=random.randint(0,10)
        lista.append(a)
        l=l+1
    return lista
def somarp (lista):
    l=0
    print(lista)

    lista2 = []

    for l in lista:
        if l %2==0:
            lista2.append(l)
    print(sum(lista2))

somarp(sorte())      
        