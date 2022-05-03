n=int(input('diga um numero?'))
n2=int(input('digite outro numer?'))
n3=int(input('fale mais un numero?'))
maior=n
if n2>maior:
    maior=n2
    

if n3>maior:
    maior=n3
    print(maior)
else:
    print('o numero maior é' , maior)  

menor=n
if n2<menor:
    menor=n2
if n3<menor:
    menor=n3
    print(menor)
else:
    print('o numero menor é' , menor)    
    



    