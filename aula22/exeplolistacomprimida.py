lista1= [x**2 for x in range(10)] # numeros de 1 a 10 ao quadrado
print (lista1)

lista2=[x for x in range(1,20) if  x%2==0] #numeors pares somente
print(lista2)

lista3=[i for i in "HACKATHON" if i in ['A', 'E' ,  'I' , 'O' , 'U']] #OEGANDO SO AS LETRAS INDICADAS
print(lista3) 

lista4=[1,2,3,4]
lista4=[i**3 for i in lista4] #atribuindo novo valor a lista atraves de uma operaçao
print (lista4)