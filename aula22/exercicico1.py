numeros=[]
numerosp=[]
for n in range (4):
    numero=int(input("escreva um numero?  "))
    numeros.append(numero)
    if numero %2==0:
        numerosp.append(numero)

print (f'{numeros.count(9)}')
print (f'{numeros.index(3)}')
print(f'os numeros pares sao {numerosp}')     