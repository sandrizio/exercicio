from testefunçao import*

linhas=int(input('digite o numero de linhas'))
colunas=int(input('digite o numero de colunas'))
intervalo_inicial=int(input('informe o intervalo inicial'))
intervalo_final=int(input('informe o intervalo final '))

a=gerar_matriz(linhas,colunas,intervalo_inicial ,intervalo_final)
b=gerar_matriz(linhas,colunas,intervalo_inicial ,intervalo_final)

if len(a)==len(b) and len (a[0])==len(b[0]):
    print(f'matriz a= {a} \n matriz b: {b} \n matriz c (a+b)= {soma_matriz(a,b)} ')
else:
    print('AS MATRIZ NAO TEM A MESMA ORDEM')

