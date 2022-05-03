
numero=int(input("fale um numero qualquer ?"))
c=numero
f=1
print("calculando {}! = ". format(numero), end='')

while c>0:
    print(f"{c}", end='')
    print("x" if c> 1 else ' = ', end='')
    f*=c
    c-=1
print('{}'.format(f))    
