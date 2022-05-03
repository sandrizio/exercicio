from math import hypot
numero=float(input("comprimento do cateto adjacente?"))
numero2=float(input("comprimento do cateto oposto?"))
hipo= hypot(numero , numero2)
print ("A hipotenusa do triangulo retangulo é {:.2f}".format (hipo))