ano_de_nacimento=int(input('diga o ano de nacimento?  '))
idade=2022-ano_de_nacimento
passou=idade-18
alistamento=18-idade
if idade>18:
    print('ja passou a epoca de alistamento foi a {} anos atras'.format(passou))
if idade<18:
    print("ainda nao esta na epoca de alistamento falta {} anos".format(alistamento))
if idade==18:
    print('esta na epoca do seu alistamento')
