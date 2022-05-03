idade=int(input('diga a sua idade??'   ))
maior=idade
menor=idade
while True:
    idade=int(input('diga a sua idade??'   ))

    if idade<0:
        break
    
    if idade>maior:
        maior=idade
    elif idade<menor:
        menor=idade
media=(menor+maior)/2        
print (f'{maior}  {menor} {media} ')





