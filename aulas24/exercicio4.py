import random
lista=[]
jogo=int(input('quantos jogos serao gerados da mega sena'))
for i in range (jogo):
    for l in range (6):
        num=random.randrange(1,60)
        lista.append(num)
    print (f'jogo {1+i} os numeros sorteados sao {lista}')
    lista.clear()   


    

