from  exemplo1 import *

escolha=int(input('escolha uma opçao: \n1.soma \n2.subtraçao \n3.divisao \n4.multiplicaçao \n5. todas as opçao'))

num1=int(input('digite o primeiro numero  '))
num2=int(input('digite o segundo numero  '))

if escolha < 0 or escolha > 5:
    print('opçao invalida')

elif escolha==1:
    s=soma(num1,num2)
    print (f'A soma dos numero é {s}')
elif escolha==2:
    s2=subtraçao(num1,num2)
    print(f'A subtraçao dos numero é {s2}')
elif escolha==3:
    d=divisao(num1,num2)
    print (f'A divisao dos numero é {d}')
elif escolha==4:
    m=multiplicaçao(num1,num2)
    print (f'A multiplicaçao dos numero é {m}')
elif escolha ==5:
    c=calculadora(num1,num2)
    print (f'a soma é {c[0]} a subtraçao é {c[1]} a divisao é {c[2]} e a multiplicaçao é {c[3]}')


