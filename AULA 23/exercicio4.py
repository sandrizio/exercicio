termo=int(input('informe o termo da P.A '))
numerostermo=int(input('informe o numero do termos da P.A '))
razao=int(input('informe a razao  da P.A'))
pa= [termo]

termo_anterior=termo

for x in range (numerostermo-1):
    termoatual=termo_anterior+razao
    pa.append(termoatual)
    termo_anterior=termoatual
print (pa)

soma=sum(pa)

print(f'somas dos elementos da pa é = {soma}')