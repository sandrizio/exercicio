
print('\n1. calcular a tençao \n2. calcular a ressistencia \n3. calcular a corrente')
op=int (input('escolha uma opçao'))
if op<1 or op>3:
    print('opçao invalida')
 
elif op==1:

    r=float(input('qual a ressistencia?  '))   
    c=float(input('qual a corrente?  '))
    t=r*c
    print('a tençao é de {} voltz'.format(t))

elif op ==2:

    t=float(input('qual a tençao?  '))
    c=float(input('qual a corrente?  '))
    r=t/c
    print('a ressistencia é {}'.format(r))
elif op== 3:
    
    t=float(input('qual o valor da tençao?  '))
    r=float(input('qula o valor da ressistencia?  '))
    c=t/r

    print('a corrente é de {}'.format(c))