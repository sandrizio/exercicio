nome=(input("digite seu nome completo?"))
maiuscula=nome.upper()
minuscula=nome.lower()
letras=len (nome)-nome.count(" ")
primeironome=nome[0:nome.find(" ")]
print(minuscula,maiuscula)
print(letras)
print(primeironome)
