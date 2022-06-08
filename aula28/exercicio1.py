from testefuncoes import *

escolha=int(input('escolha uma opçao: \n1.retangulo \n2.triangulo \n3.circulo')) 

num=int(input('digite o primeiro numero  '))
num2=int(input('digite o segundo numero  '))

if escolha < 0 or escolha > 5:
    print('opçao invalida')

elif escolha == 1:
    r=retangulo(num,num2)
    print (f'A area do retangulo é {r}')
elif escolha == 2 :
    t=triangulo(num,num2)
    print (f'A area de um triangulo é {t}')
elif escolha ==  3:
    c=circulo(num,num2)
    print (f'A area de um circulo é {c}')
          