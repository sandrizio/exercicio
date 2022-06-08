
import random
while True:
    lin=int(input('diga o numero de linhas da matrix A'))
    col=int(input('diga o numero de colunas da matrix A'))
    if lin > 0 and col > 0:
        matrix=[]
        for l in range (lin):
            linha = []
            for c in range (col):
                numeros= random.randint(1,11)
                linha.append(numeros)
            matrix.append(linha)
        break
print (matrix)


while True:
    lin=int(input('diga o numero de linhas da matrix A'))
    col=int(input('diga o numero de colunas da matrix A'))
    if lin > 0 and col > 0:
        matrixb=[]
        for l in range (lin):
            linha = []
            for c in range (col):
                numeros= random.randint(1,11)
                linha.append(numeros)
            matrixb.append(linha)
        break
print (matrixb)





       






