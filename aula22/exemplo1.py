lista=[ 'maria' , 'janaina' , 'jose' , 'carlos ']
listaa=['jose' , 'sandrizio']
#for n in range(0, len(lista)):  @@loop da lista
#lista.append('jorge') @@ adiciona no final a lista
#lista.insert(0, 'jorge')  @@ adiciona na posiçao indicada
#lista.sort() @ordem cresente
#lista.sort(reverse=True) @@ oredena decresente
#del lista[-1] @@tira o ultimo 

#lista.remove("janaina") @@ exclui oq vc ordenou
#lista.pop(0) @@exclui o item indicado
#lista.clear()@@ limpa a lista



#listaa=lista @vinculaa uma lista na outra

##listaa=lista[:]
##lista.append('jose')
#           VAI VINCULAR AS LISTAS MAIS VAI ADICIONAR O JOSE SO NA LISTA E N NA LISTAA

#lista.extend(listaa) @@ adiciona uma lista na outra


##print(lista.cont('jose'))
#                   mostra quantas vezes aparece

#print(lista.index('janaina')) @@possisao da palavra

for indice, nome in enumerate(lista):
    print(f'{nome} esta armazenado no indice {indice}')   