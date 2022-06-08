palavras=('casa' , 'carro' , 'computador' , 'cachorro' , 'lapis' , 'sandrizio' , 'apartemento' )

for p in palavras:
    print (f'\n a palavratemos {p.upper()} temos'  , end= ' ') 
    for letra in p:
        if letra.lower() in 'a e i o u':
            print (letra , end=' ')


    