def ajuda (n):
    print (help(n))

while True:
    n=input('fale um comando que deseja saber? ')
    
    ajuda(n)

    fim=input('se deseja finalizar o programa digite *fim* se nao o programa se repetira: ').lower()
    if fim == 'fim':
        print('programa finalizado')
        break 
    


