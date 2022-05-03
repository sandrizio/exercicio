km_percorrido=float(input('diga a quantidade de km percorrida por um carro alugado?'))
dias_carro_alugado=float(input('qual foi a quantidade de dias que o carro foi alugado'))
preço_do_carro=(60*dias_carro_alugado)+(0.15*km_percorrido)
print('o valor do aluguel do carro saiu por {:.2f}:  '.format(preço_do_carro))