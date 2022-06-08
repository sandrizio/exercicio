from random import randrange

lin=int(input('digite a linha'))
col=int(input('digite a coluna'))

a=[[randrange(1,11) for i in range(col)] for j in range (lin)]

b=[[randrange(1,11) for i in range(col)] for j in range (lin)]

abaixodp=0
acimadp=0

for i in range (lin):
    for j in range (col):
        if i>j:
            abaixodp+=a[i][j]
    if i<j:
        acimadp+=b[i][j]

print('matriz A : ')
for i in range (lin):
    for j in range (col):
        print(a[i][j], end=' ')
    print ()  
print('matriz B : ')
for i in range (lin):
    for j in range (col):
        print(b[i][j], end=' ')
    print ()

print(f'soma = {abaixodp+acimadp}')                   
