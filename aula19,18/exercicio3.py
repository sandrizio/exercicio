
numero=int(input('digite um numero inteiro '))
soma=0
soma+=numero
divisao=0
divisao+=1
maior=numero
menor=numero
while True:
    numero=int(input('digite outro numero inteiro?  ' ))
    simounao=input('voce deseja continuar digitando valores S/N ? ' ).strip().upper()
   
    soma+=numero
    divisao+=1
    media=soma/divisao

    
    if numero>maior:
        maior=numero
    if numero<menor:
        menor=numero
    if simounao== "N":
        break
       
print(f"o menor numero é {menor} o maior numero é {maior} e a media é {media:.2f} e a soma deles é {soma}")