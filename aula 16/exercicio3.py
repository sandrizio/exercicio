

for s in range (0,3):
    senha=int(input("digite sua senha "))
    if senha==123456:
        print("ola!")
        break
    else:
        if senha!=123456 and s==0:
            print(f"voce errou voce tem mais duas tentativas")
       
        elif senha!=123456 and s==1:
            print("senha incorreta voce tem mais uma tentativa")

        elif senha!=123456 and s==2:
            print("sua senha foi bloqueada") 
            break

                 
                 