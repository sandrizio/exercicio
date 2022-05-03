numero=int(input('digite um numero inteiro?'))
n1=0
n2=1
print(f'{n1,n2}', end='-')
for n in range (numero):
    n3=n1+n2
    print(f'{n3}', end='-')
    n1=n2
    n2=n3
