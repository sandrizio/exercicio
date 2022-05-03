
while True:
    numero=int(input("digite um numero para mostrar a tabuada"))
    if numero <0:
        break
    for c in range(0,11):
        print(f'{numero} x {c} = {numero * c}')

