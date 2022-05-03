
print("informe o nome e o preco de 5 remedios")
remedio=input("nome do remedio? ")
preco=float(input("diga o preço do remedio?"))
 
rmenor=remedio
menor=preco

for c in range(4):
    remedio=input("nome do remedio? ")
    preco=float(input("diga o preço do remedio?"))
    if preco<menor:
        rmenor=remedio
        menor=preco
print(f"o nome do remedio menor é {menor}") 
