numero=int(input('Digite um numero '))
sentidoCont=[]
sentidoNormal=[]
tamLista=0

while numero!=0:
    numeroInverso=numero%10
    sentidoCont.append(numeroInverso)
    numero=numero//10
    tamLista+=1

cont=tamLista
while cont>0:
    sentidoNormal.append(sentidoCont[cont-1])
    cont -=1


cont=0
achou=False
while cont<tamLista:
    if sentidoNormal[cont]!=sentidoCont[cont]:
        achou=True
    cont+=1
    
        
if achou==False:
    print("o numero digitedo eh um palindromo")
else:
    print("o numero digitado nao eh um palindromo")
                    
