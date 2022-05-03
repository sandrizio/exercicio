maior=0
menor=0
for c in range (0,5):
    peso=float(input('diga o seu peso  '))
    if c==1:
        maior=peso
        menor=peso
    else:
        if maior<peso:
            maior=peso
        elif menor>peso:
            menor=peso
print(f'o maior pesso é {maior} e o menor é {menor}')             
