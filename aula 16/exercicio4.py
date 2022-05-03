nome=input("diga o nome do atelta")
tempo=float(input("tempo do atleta?"))
nmenor=nome
menor=tempo
maior=tempo
nmaior=nome
media=0
tempoloco=0
for c in (0,6):
 
    nome=input("diga o nome do atelta")
    tempo=float(input("tempo do atleta?"))

    if tempo<menor:
        nmenor=nome
        menor=tempo
    if tempo>maior:
        nmaior=nome
        maior=tempo
    if tempo>12 and tempo<15:
        tempoloco=+1

media+=1/7
print(f'o menor tempo foi do{nmenor} e o maior foi de  {nmaior} a media dos tempo foi de {media:.2f} e {tempoloco} ficaram entre 12 a 15 segundos')            


