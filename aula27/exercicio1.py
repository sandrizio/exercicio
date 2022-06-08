def voto():
    
    if ano >2007:
        print('voce nao é obrigado a votar')
    elif ano<2007:
        print ('obrigatorio o voto')

    elif ano == 2004 or ano ==2003 or ano== 2002:
        print('voto opcional ')    


ano=int(input('digite o seu ano de nascimento :'))

voto()