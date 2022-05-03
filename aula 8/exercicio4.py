import random

aluno1=input('diga o nome do primeiro aluno:  ')
aluno2=input('diga o nome do segundo aluno:  ')
aluno3=input('diga o nome do terceiro aluno:  ')
aluno4=input('diga o nome do quarto aluno:  ')
lista=[aluno1,aluno2,aluno3,aluno4]
sorteio=random.choice(lista)
print('o nome dos aluno sao {} , {} , {} , {} e o sortiado é o {}:  '.format(aluno1,aluno2,aluno3,aluno4,sorteio))
