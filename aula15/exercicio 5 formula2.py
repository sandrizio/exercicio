from operator import truediv
from random import randint

computador=randint(0,5)
print("vou pensar em um numero de 0 a 5, tenta adivinhar o numero")
acertou=False
palpite=0

while not acertou:
    jogador=int(input("qual seu palpite?  "))
    palpite+=+1
    if jogador== computador:
        acertou=True
    else:
        if jogador%computador:
            print("voce errou tente mais uma vez")
print(f"acertou com {palpite} tentativa. parabens!")             