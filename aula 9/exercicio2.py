


numero=int(input('Diga um numero inteiro?  '))
print("\n1.numero binario \n2.numero octal \n3.numero hexadecimal")
op=input("escolha uma opçao?  ")

if op<1 or op>3:
    print('a opçao esta invalida')
elif op==1:
    bi= bin(numero)
    print("a forma binaria é{}".format(bi))
elif op==2:
    octal=oct(numero)
    print('a forma octal é{}'.format(octal))
elif op==3:
    hexa= hex(numero)
    print("a forma hexadecimal é{}".format(hexa))
        






