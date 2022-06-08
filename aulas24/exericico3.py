from random import randrange
from math import sqrt
n=int(input('digite um numeno para N'))
if n>1:
    
    a=[randrange(1,11) for i in range(n)]

menor=min(a)
maior=max(a)
media=sqrt(menor*maior)

print (a)
print (f'a media geometrica é {media:.2f}')

