n=int(input('digite a quantidade de numeros a informar: '))
soma=0

for cont in range(n):
    num=float(input('digite um numero: '))
    soma+=num #soma = soma +1
media=soma/n
print('media = {media:.2f}')    