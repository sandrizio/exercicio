def escreve(msg):
    """"
    print de mensagem  imformada pelo usuario
    msg: entrada do usuario para programa
    """
    print('~')
    print(msg)
    print('~')
#escreve(input('digite uma frase'))

#help(escreve)


def teste (b):
    b+=4 #variavel de escopo local
    c=2
    print(f'a dentro da funçao vale {a} ')
    print(f'b dentro da funçao vale {b}')
    print(f'c dentro da funçao vale {c}')

a=5 #variavel de escopo global
teste(a) 
print (f'a fora da funçao vale {a}')

