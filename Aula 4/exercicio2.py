from math import sqrt
x1=int (input("qual o x1?"))
x2=int (input("qual o x2?"))
y1=int (input("qual y1?"))
y2=int (input("qualy2?"))
p1=(x1-x2)**2
p2=(y1-y2)**2
p1=p1*p1
p2=p2*p2
d= sqrt(p1+p2)
print("A distanci do p1 para o p2 é de {:.2f}".format(d))