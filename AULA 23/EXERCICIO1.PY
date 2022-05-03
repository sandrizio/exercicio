matrix=[[],[]]
lin=int(input('diga o numero de linhas da matrix A'))
col=int(input('diga o numero de colunas da matrix A'))

for l in range (lin):
    for c in range (col):
        matrix[l][c]=int(input(' digite um numero da matrix a'))
       

matrixb=[[],[]]
lin=int(input('diga o numero de linhas da matrix B'))
col=int(input('diga o numero de colunas da matrix B'))

for l in range (lin):
    for c in range (col):
        matrixb [l][c]=int(input(' digite um numero da matrix B'))

soma=matrix[1][0]+matrixb[0][1]
print(matrix)
print(matrixb)
print(matrix[1][0])
print(matrixb[0][1])

print(f'a soma é {soma}')




