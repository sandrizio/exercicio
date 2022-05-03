'''cupula'''
'''dias= ('domingo' , 'segunda' , 'terca' , 'quarta' , 'quinta' , 'sexta' , 'sabado')'''

'''texto='python'
print (tuple(texto)) 
p , y , t , h , o , n'''


'''lista=[1,2,3,4]
lista[2]=8
print (tuple(lista))
1 , 2 , 8 , 4'''


'''lista=[3,5]
tupla=(1,2,lista)
print(tupla)
(1,2 [3 , 5])'''

'''print(len(***)===> saber o tamanho da tupla'''

'''print (***.cout (numero)===> contar quantas vezes aparece '''

'''lista=['python' , 1 , 2 , 'java']
print (lista)
pode ser dados diferente numeros e letra'''


'''meses=['janeiro' ,'fevereiro' , 'março' , 'abril' , 'maio' , 'junho' , 'julho' , 'agosto' , 'setembro' , 'outubro' , 'novembro' , 'dezemrbo']
n=1
while n<4:
    mes=int(input('escolha o mes [1-12'))
    if 1<=mes<13:
        print (f'o mes é {meses[mes-1]}')
    n+=1 '''   

#escolha 4 meses e o programa fala o mes q esclheu 


'''meses=['janeiro' ,'fevereiro' , 'março' , 'abril' , 'maio' , 'junho' , 'julho' , 'agosto' , 'setembro' , 'outubro' , 'novembro' , 'dezemrbo']

print(meses[:3])'''
#ta falando pra ele ir no indicie 0 ate o 3
#se usar indice negativo exemplo= print (meses[:-3])  ele ta tirando os ultimos 3


'''meses=['janeiro' ,'fevereiro' , 'março' , 'abril' , 'maio' , 'junho' , 'julho' , 'agosto' , 'setembro' , 'outubro' , 'novembro']
#falto um mes
meses.append('dezembro')'''
#adiciona algo na lista comando .append'''



'''meses=['janeiro' ,'fevereiro' , 'março' , 'abril' , 'maio' , 'junho' , 'julho' , 'agosto' , 'setembro' , 'outubro' , 'novembro' , 'dezemrbo']
meses+=['mes13' , 'mes14']
#adiciona a lista'''
'''print (meses*2) 
#multiplica e mostra duas vezes''' 



'''meses=['janeiro' ,'fevereiro' , 'março' , 'abril' , 'maio' , 'junho' , 'julho' , 'agosto' , 'setembro' , 'outubro' , 'novembro' , 'dezemrbo']
#imprimir um embaixo do outro
    for mes in meses:
    print(mes)'''
    
'''meses=['janeiro' ,'fevereiro' , 'março' , 'abril' , 'maio' , 'junho' , 'julho' , 'agosto' , 'setembro' , 'outubro' , 'novembro' , 'dezemrbo']
for mes in meses:
    print(mes, end= ' ')'''