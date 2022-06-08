import random
def maior():
    nmaior=max(lista)
    return nmaior
    
lista=[]

l=0

while l < 5:
    a=random.randint(0,10)
    lista.append(a)
    l=l+1


print (lista)
print(maior())