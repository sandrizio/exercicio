

linha=int(input('diga o numero de linhas da matrix '))
coluna=int(input('diga o numero de colunas da matrix '))
m=[]
for l in range (linha):
    linhas=[]
    for c in range (coluna):
        n=int(input('diga os numeros da matrix '))
        linhas.append(n)
    m.append(linhas)    


for l in range (linha):
    for c in range (coluna):
        if l < c :
            if (m[l][c] != 0):
                triangular = 0
            else:
                triangular=1    
                         

if triangular == 1 :
    print(' a matriz é triangular')
else:
    print(' a matriz nao é triagular')    


