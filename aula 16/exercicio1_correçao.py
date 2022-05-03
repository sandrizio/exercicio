from pickle import TRUE


mulheres=0
homens18=0

while True:
    idade=int(input("idade"))
    if idade<0:
        break
    sexo=input("sexo").upper()
    if sexo=='F':
        mulhures=+1 
    elif sexo=='M'and idade>18:
        homens18=+1
print(f"total de mulheres {mulheres} \n total de homens acima de 18 anos {homens18}")        



