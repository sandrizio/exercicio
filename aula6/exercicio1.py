from random import randint

computador=randint(0,5)
print("vou pensar em um numero de 0 a 5, tenta adivinhar o numero")
jogador=int(input("que numero estou pensando?"))

if jogador == computador:
    print('parabens voce acertou!!')


else:
    print("voce errou o numero que eu estava pensando era {}".format(computador))