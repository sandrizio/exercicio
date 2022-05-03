times=['América', 'Athletico' , 'Atlético-GO' , 'Atlético-MG' , 'Avaí' , 'Botafogo' , 'Bragantino' , 'Ceará', 'Corinthians ' , 'Coritiba' , 'Cuiabá' , 'Flamengo' , 'Fluminense' , 'Fortaleza' , 'Goiás' , 'Juventude' , 'Internacional' , 'Palmeiras' , 'Santos' , 'Chapecoense']
club=times.index('Chapecoense')
print (f'o time chapecoense esta na posiçao {club+1} ')
print(f'os 5 primeiros times sao {times[:5]}')
print(f'os ultimos colocadas sao os {times[-4:]}')
times.sort()
print(f'a ordem alfabetica dos time é {times}')
