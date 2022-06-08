from random import randint


def gerarmatriz(n1,n2):
    m=[]
    for l in range (n1):
        for c in range (n2):
            n=randint(0,11)
            m.append(n)
    return m     

def funçao(m):
    t=[]
    for l in range (len(m)):
        for c in range (len(m)):
            if l == c :
                t.append(m[l][c])      
    return t
        

linha=int(input('diga o numero de linhas da matrix '))
coluna=int(input('diga o numero de colunas da matrix '))
matriz=gerarmatriz(linha,coluna)

print (f'a matriz gerada é {matriz}')


print (f'a funçao da matriz é {funçao(matriz)}')







   