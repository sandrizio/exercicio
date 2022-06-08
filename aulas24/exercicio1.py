lista=('laranja'  ,  2.00,
       'cenoura'  ,  4.20,
       'maça'  ,  3.00,
       'uva'  ,  1.50 ,
       'melancia'  ,  5.00)
for l in range (0,len(lista)):
    if l %2 == 0:
        print (f'{lista [l]}' , end=' ')
    else:
        print(f'{lista [l]:.2f}')
