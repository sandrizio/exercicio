from random import shuffle , choice
rifas=[]
escolhido=''
for r in range (3):
    nrifa=input('Nome da pessoa que comprpou a rifa? ')
    rifas.append(nrifa)

shuffle(rifas)
escolhido=choice(rifas)


print(escolhido)
