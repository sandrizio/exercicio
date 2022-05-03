nota1=float(input('diga a primeira nota?  '))
nota2=float(input('diga a outra nota'))
media=(nota1+nota2)/2
if media<5 :
    print('o aluno foi reprovado')

if media>=5 and media <=6.9:
    print('voce pegou recuperaçao')
if media>=7:
    print('parabens voce passou')    
