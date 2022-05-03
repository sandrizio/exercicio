numero1=int(input('fale um numero?  '))
numero2=int(input('fale loutro numero?  '))
maior=numero1
if numero2>maior:
    maior=numero2
if numero1==numero2:
    print('nenhum numero é o maior')    
else:
    print('o numero maior é {}'.format(maior))
    