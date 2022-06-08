from random import randrange
linha=int(input('diga o numero de linhas da matrix '))
coluna=int(input('diga o numero de colunas da matrix '))
m=[]
soma=0
for l in range (linha):
    
    for c in range (coluna):
        n=randrange(0,2)
        m.append(n)
        
          
for s in m:
    soma+=s
    if soma == 0 :
        print (f'a matriz {m} e nula')
    else :
        print (f' a matriz {m} nao é nula')    
print (f' o numero de linhas é {linha}')
print (f'o numero de coluna é {coluna}')
        

  
