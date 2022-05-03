nome=input('diga seu nome completo?  ')
primeiro_nome=nome[0:nome.find(" ")]
ultimo_nome=nome.split()

print(f'seu primeiro nome é {primeiro_nome} e seu ultimo é {ultimo_nome[len (ultimo_nome)-1]}')