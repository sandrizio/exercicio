
print("informe seu sexo [f/m] e sua idade assim que acabar os aluno digite uma letra aleatoria e uma idade negativo")
homens=0
mulher=0


for n in range (0,1000):
    sexo=input("qual seu sexo[F/M]? ").strip().upper()
    idade=int(input("qual a sua idade? "))
    if sexo=="M" and idade>18:
        homens+=+1
    else:
        if sexo=="F" :
            mulher+=+1
        else:

            if idade  < 0 :
                break         
print(f"na sala tem {homens} com mais de 18 anos e {mulher} mulheres")            


