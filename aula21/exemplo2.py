#menor valor
#numeros pares
#maior numero
#ocorrencia
#media elementos
#soma dos numeros negativos

lista= [12, - 2, 4, 8, 29, 45, 78, 36, -17, 2, 12, 8, 3, 3 , -52]
maiorvalor=lista [0]
menorvalor=lista [0]
listapares=[]
ocorrencia=0
mediaelementos=0
somanegativa=0
for index in range(0,len(lista)):
    if maiorvalor<lista[index]:
        maiorvalor=lista[index]
    if menorvalor>lista[index]:
        menorvalor=lista[index]
    if lista[index]%2==0:
        listapares.append(lista[index])
    if lista[index] == lista[0]:
        ocorrencia+=1   
    mediaelementos+=lista[index]

    if lista[index]<0:
        somanegativa+=lista[index]
mediaelementos/=len(lista)


print (f'o menor valor é {menorvalor}')
print (f'os numeros pares sao {listapares}')            
print (f'o maior numero é o {maiorvalor}')
print (f'numero de ocorrencias do primeiro elemento {ocorrencia}')        
print (f'media de elementos {mediaelementos}') 
print (f' a soma dos numeros negativa é {somanegativa}')