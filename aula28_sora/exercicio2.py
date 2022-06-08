from testefunçao import*

linhas=int(input('digite o numero de linhas'))
colunas=int(input('digite o numero de colunas'))
intervalo_inicial=int(input('informe o intervalo inicial'))
intervalo_final=int(input('informe o intervalo final '))

m=gerar_matriz(linhas, colunas, intervalo_inicial, intervalo_final)
print(f'matriz gerada: {m}')

if len (m)==len(m[0]):
    print(f'treaço da matriz gerado: {caluclar_traço_matriz(m)}')

else:
    print('nao é possivel calcular')    