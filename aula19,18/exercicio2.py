soma=0
tentativas=0
while True:
    numero=int(input('digite numeros para soma e o programa sera finaçizado quando digitar 999??  '))
    if numero != 999:
        soma+=numero
        tentativas+=1
    else:
        break
print(f'foi digitado {tentativas} e a soma entre eles é {soma}')                


