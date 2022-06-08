def gerar_matriz(linhas,colunas, intervalo_inicial, intervalo_final):
    from random import randrange
    m=[[randrange(intervalo_inicial, intervalo_final)for i in range (colunas)] for j in range (linhas)]
    return m

def caluclar_traço_matriz(matriz):
    traco=[]
    soma=0
    for i in range (len(matriz)):
        traco.append(matriz[i][soma])
        soma+=1

    return sum(traco) 

def soma_matriz(a,b):
    c=[]
    for i in range(len(a)):
        c.append([])
        for j in range (len(a[i])):
            c[i].append(a[i][j]+b[i][j])
    return c   

def multiplicaçao_matriz_por_constante(matriz, costante):
    m=[]
    for i in range (len(matriz)):
        m.append([])
        for j in matriz [i]:
            m[i].append(j*costante)
    return m

def obtem_dados_funcionario():
    func=[['ana ' , 'f'] , ['beatriz', 'f'] , ['carla' , 'f'], ['daniela' ,  'f'] , ['emilio' , 'm'], ['fernando' , 'm'] ,['italo' , 'm']]
    return func

def retornar_num_hom_mul(matriz):
    h=m=0
    linha=len(matriz)
    
    for nome, dados in matriz:
        print(nome , dados)
    for i in range (linha):
        if matriz[i][1]=='f':
            m+=1
        else:
            h=+1
    return f'\nquantidade de mulher cadastradas: {m} \n quantidade de homes cadastrados : {h}'                                                 