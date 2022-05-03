salario=float (input('qual o salario do funcionario?'))
aumento=salario*0.15 if  salario<=1250 else salario*0.10
salario_f=salario+aumento
print('o aumento do salario vai ser de {:.2f} e o salario final é {:.2f}'.format(aumento,salario_f))