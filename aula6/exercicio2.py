from cmath import inf


velocidade=float (input('qual a velocidade do carro?'))
if velocidade > 80:
    print('voce foi multado!')
    multa=(velocidade-80)*7
    print('voce recebeu uma multa de {}'.format(multa))
 
else:
     print('parabens voce esta dentro do limite de velocidade')

