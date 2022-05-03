altura1=float(input("digita uma estatura..?"))
altura2=float(input("diga outra estatura.. ?"))
altura3=float(input("diga mais uma estatura.. ?"))
maior=altura1
menor=altura1
meio=altura1
if altura1>altura2 and altura1 > altura3:
    maior=altura1
    if altura2>altura3:
        meio=altura2
        menor=altura3
    else:
        meio=altura3
        menor=altura2
elif altura2>altura1 and altura2>altura3:
    maior=altura2
    if altura1>altura3:
        meio=altura1
        menor=altura3
    else:
        media=altura3
        menor=altura1
else:
    maior=altura3
    if altura1>altura2:
        meio=altura1
        menor=altura2
    else:
        meio=altura2
        menor=altura1    
        
        
print(f' a maior é {maior} a menor é a`{menor} e a do meio é {meio}')                              
             
