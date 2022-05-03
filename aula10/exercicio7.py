salaraiob=float(input('diga o salario base da empresa.. '))
print('\n1. progamador de sistema \n2. analista de sistema \n3. analista de banco de dados')
op=int(input ('escolha um cargo 1 programador 2 analista de sistema e 3 analista de banco de dados  '))
if op<1 or op>3:print('opçao invalida') 
elif op==1:
    salario1=salaraiob*0.30
    salariof=salaraiob+salario1
    print(f'seu salirio é de {salariof}')
elif  op==2:
    salario2=salaraiob*0.20
    salariof=salaraiob+salario2
    print(f'seu lario é de {salariof}')
else :
    salario3=salaraiob*0.15
    salariof=salaraiob+salario3
    print(f'o salario vai ser de {salariof}')


