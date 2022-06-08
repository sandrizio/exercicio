from testefunçao import*
linhas=int(input('digite o numero de linhas'))
colunas=int(input('digite o numero de colunas'))
intervalo_inicial=int(input('informe o intervalo inicial'))
intervalo_final=int(input('informe o intervalo final '))

m1=gerar_matriz(linhas,colunas,intervalo_inicial ,intervalo_final)
costante=int(input('informe a costante'))
print(f'matriz gerada : {m1} \n matriz c (m1 * costante)= {multiplicaçao_matriz_por_constante(m1,costante)}')