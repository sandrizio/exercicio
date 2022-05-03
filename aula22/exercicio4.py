n= int(input('digite im numero impar , maior que 1: '))
if n <=1 or n%2==0:
    print('numero invalido')
else:
    L=[]
    for x in range (n):
        num=int(input('digite um numero maior ou igual a zero:'))
        L.append(num)

meio=int(len(L)/2)
elementomeio=L[meio]
fatorial=1
#fatorial = 1*2*3*4*5=120
for n in range(2 , elementomeio+1):
    fatorial*=n
print(f'lista: {L}')
print(f'o elemento do centro da lista é {elementomeio} e seu fatorial é {fatorial} ')    