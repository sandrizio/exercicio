from random import randint

n=(randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10))

print('os valores sortiados foram: ', end='')
for num in n:
    print(f'{num}', end=' ')
print(f'\no maior valor sorteado foi {max(n)}')
print(f'o menor valor sorteado foi {min(n)}')
