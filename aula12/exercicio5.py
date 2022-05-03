from math import sqrt


x1=float(input('diga a cordenada x do ponto 1:'))
y1=float(input('diga a cordenada y do ponto 1:'))

x2=float(input('diga a cordenada x do ponto 2:'))
y2=float(input('diga a cordenada y do ponto 2:'))

x3=float(input('diga a cordenada x do ponto 3:'))
y3=float(input('diga a cordenada y do ponto 3:'))

l1= sqrt(pow(x2-x1,2)+pow(y2-y1,2))
l2= sqrt(pow(x3-x1,2)+pow(y3-y1,2))
l3= sqrt(pow(x3-x2,2)+pow(y3-y2,2))

cond1= True
cond2= True
cond3= True

if l1==0 or l2 ==0 or l3 == 0:
    cond1=False
if l1>(l2+l3) or l2>(l1+l3) or l3>(l1+l2):
    cond2=False
if l1<=abs(l2-l3) or l2<=abs(l1-l3) or l3<=abs(l1-l2):
    cond3=False

triangulo= True

if cond1 == False or cond2 == False or cond3 == False:
    triangulo= False
    print('nenhum triangulo formado ..')

    if cond1 == False:
        print('pelo menos um dos lado é igual a 0 ')

    if cond2 == False:
        print('pelo menos um lado é maior que a soma de um dos lado ')

    if cond3 == False:
        print("um dos lado é menor ou igual ao modulo da diferença")

elif l1==l2==l3:
    print('triangulo equelatero')
elif l1!=l2!=l3:
    print('tiangulo ecaleno')
else:
    print('triangulo é isoceles')

if triangulo:
    print(f'medida do lado 1: {l1:.2f} \nmedida do lado 2 : {l2:.2f} \nmedida  do lado 3: {l3:.2f} ')            

