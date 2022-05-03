somaidade=0
maioridadehomem=0
nomemaisvelho=''
mulhermenor=0
for n in range(0,4):

    nome=input('qual seu nome? '). strip()
    idade=int(input('qual sua idade? '))
    sexo=input('qual seu sexo   [F/M]? ').strip().upper()
    somaidade+=idade
    if n==1 and sexo in  'M':
        maioridadehomem=idade
        nomemaisvelho=nome
    if sexo in 'M ' and idade > maioridadehomem :
        maioridadehomem=idade
        nomemaisvelho=nome
    if sexo in 'F' and idade < 20:
        mulhermenor=+1  
mediaidade=somaidade/4
print(f'a media de idade é de {mediaidade:.1f} o homem mais velho é o {nomemaisvelho} e exitem {mulhermenor} mulher com menos de 20 anos ')            
 


