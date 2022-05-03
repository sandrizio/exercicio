contagem=('zero' , 'um' , 'dois' , 'tres' , 'quatro' , 'cinco' , 'seis' , 'sete' , 'oito' , 'nove' , 'dez' , 'onze' , 'doze' , 'treze' , 'catorze' , 'quinze' , 'dezesseis' , 'dezessete' , 'dezoito' , 'dezenome' , 'vinte')

while True:
    num=int(input("digite um numero entre 0 a 20: "))
    if 0<=num<=20:
        break
    print('tente novamente ', end= ' ')
print(f'voce digitou o numero {contagem[num]}')
