casa=float(input('diga o valor da casa?   '))
salario_comprador=float(input('diga o salario do comprador?  '))
tempo_pagando=float(input('quanto tempo o comprador vai ficar pagando em meses?  '))

prestaçao=casa/tempo_pagando
l=salario_comprador*0.30
if prestaçao>l:
    print('nao pode fazer o emprestimo')
else:
    print ('pode fazer o emprestimo')    



