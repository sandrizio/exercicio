maior=0
menor=0
for c in range (0,7):
    ano=int(input('diga o ano de nascimento?  '))
    if  ano<=2004:
        maior=maior+1
    else:
        menor=menor+1
print(f'sao maiores de idade {maior} e sao menor de idade {menor}')            
        
    