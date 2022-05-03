
salario=float (1500)
comissao=float (200)
corretor=input("digite o nome do corretor?")
venda=int(input("quantidade de imoveis vendido?"))
venda_total=float(input("valor total de venda?"))

salario_final=salario+(comissao*venda)+(venda_total*0.05)

print('salario final do' , corretor , 'é de' , salario_final)