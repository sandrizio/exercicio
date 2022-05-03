sexo=input('informe seu sexo [m/f]: ').strip().upper()
while sexo not in 'mf':
    sexo=input('dados invalidos. por favor, informe seu sexo [m/f]: ').strip().upper()
print(f'sexo {sexo} registrado com sucesso.')
    