n=float (input("digite um numero:  "))
n2=float (input("digite outro numero:  "))


print('\n. media pnderada, com o pesos 2 e 3, respectvamente  \n 2. quadrado da soma de 2 numeros \n2. cubo do maior numero {}')
op=int(input("escolha uma opçao:  "))

if op<1 or op>3:
    print('opçao invalida. ')
elif op ==1:
    media =(n*2 + n2*3)/5
    print("media ponderada calculada: {:.2f}".format(media))
elif op ==2:
    quadrado=(n+n2)**2
    print('quadrado da soma dos dois nuemro:  {:.2f}'.format (quadrado))
elif n<n2:
        cubo=n**3
        print('{} é o menor e seu cubo é {} '.format (n, cubo))
else:
    cubo=n2**3
    print('{} é o numero menor e seu cubo é {}'.format(n2,cubo))
