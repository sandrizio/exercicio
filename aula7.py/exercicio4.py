n=int(input('diga um valor de uma reta?'))
n2=int(input('diga outro valor?'))
n3=int(input('diga mais um valor?'))
if n> n2+n3:
    print('nao pode fazer o triagulo')

else:
    print('pode fazer o triagulo')
    if n2>n+n3:
        print('nao pode formar o triangulo')
    else:
        print(' pode fazer o triangulo')
        if n3>n+n2:
            print('naopode fazer o triagulo')
        else:
            print('pode fazer o triangulo')             


