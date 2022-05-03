from math import sqrt
L=[]
while True:
    numeros=int(input('digite numeros inteiros e 0 para parar '))
    if numeros>0:
        L.append (numeros)

    if numeros == 0:
        break
maior=max(L)
menor=min(L)

geometica=sqrt (maior*menor)

print(f'a forma geometrica entre o maior e o menor numero é {geometica}')

