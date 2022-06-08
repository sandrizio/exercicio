atletas=[]
tempos=[]

for x in range (7):
    nome=input('diga o nome do atleta : ')
    tempo=float(input('o tempo do atleta :'))
    atletas.append(nome)
    tempos.append(tempo)

indici_melhor=tempos.index(min(tempos))

indici_pior=tempos.index(max(tempos))

media_tempos=sum(tempos)/len(tempo)

print(f'{atletas[indici_melhor]} tem o melhor tempo ')
print(f'{atletas[indici_pior]} tem o pior tempo')
print(f'media dos tempos {media_tempos:.2f}')