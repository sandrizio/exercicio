from turtle import end_fill


termo=int(input('Digite o primeiro termo da PA:'))
razao=int(input('Digite a razao da PA:'))
x=termo+9*razao

for c in range(termo,razao+x, razao):
    print((c), end='-> ')