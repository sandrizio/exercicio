from random import randint

computador=randint(0,5)
print("vou pensar em um numero de 0 a 5, tenta adivinhar o numero")
palpites=0
for j in range (0,6):
    jogador=int(input("que numero estou pensando?"))
    palpites+=1
    if jogador == computador:
        print(f"parabens vc acertou com {palpites}",)
        break
    else:
        print("vc errou")
            
