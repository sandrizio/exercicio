pares=0
par=[]
n=0
for p in range (0,5):
    numeros=int (input("digite um numero? "))
    if 0== numeros % 2:
        par.append(numeros)
        n=n+1
        

        
print(f'existe {par} pares, um total de {n}')        
