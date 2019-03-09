continua=True
listaNumeros=[]
tamLista=0
while continua:
    numero=input("Digite um numero ")
    if numero!="":
        listaNumeros.append(int(numero))
        tamLista+=1
    else:
        continua=False

achou=True
while achou:
    achou=False
    cont=0
    while cont<tamLista-1:
        if listaNumeros[cont]<listaNumeros[cont+1]:
            achou=True
            aux=listaNumeros[cont]
            listaNumeros[cont]=listaNumeros[cont+1]
            listaNumeros[cont+1]=aux
        cont+=1
    print(listaNumeros)
    
