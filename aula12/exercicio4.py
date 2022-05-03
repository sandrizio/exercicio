copo1='laranja'
copo2='acerola'


print("o copo 1 é de laranja  eo copo 2 é de acerola vamos trocalo?  ")


print("\n1. trocar sucos de copo \n2. nao trocar sucos ")
op=int (input('escolha uma opçao ?'))
if op<1 or op>2:
    print("opçao invalida")
elif op==1:
    print(f"o copo 1 virou de {copo2} , o copo 2 virou de {copo1} ")
elif op==2:
   
    print(f"o copo 1 continua de {copo1} e o copo 2 continua de {copo2} ")    






         