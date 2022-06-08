
from random import randrange

n=int(input('informe um valor para n'))

if n>0:
    #lista random 
    a=[randrange(1,11) for i in range(n)]

    b=[randrange(1,11) for i in range(n)]

    c=[]

    for i in range (n):
        c.append(a[i]+b[i])

    print (a)
    print (b)
    print (c)
else:
    print('erro: n deve ser maior q 0')
