x1=float(input('comprimento da primeira reta?  '))
x2=float(input('comprimento da segunda reta?  '))
x3=float(input('comprimento da terceira reta?  '))
if x1<x2+x3 and x2<x1+x3 and x3<x2+x1:
    print('é fossivel formar o triangulo')
    if x1==x2 and x1==x3 and x2==x3:
        print('triangulo equilatero')
    elif x1!=x2 and x1!=x3 and x3!=x2:
        print('triangulo escaleno')
    else:
        print("triangulo isoceles ")
else:
    print('nao pode formar o triangulo')

