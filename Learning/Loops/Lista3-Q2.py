'''
Universidade Federal de Pernambuco (UFPE) (http://www.ufpe.br)
Centro de Informática (CIn) (http://www.cin.ufpe.br)
Graduando em Sistemas de Informação
IF968 - Programação 1

Autor:	Gabriel Cavalcanti de Melo (gcm2)
Email:	gcm2@cin.ufpe.br
Data:	AAAA-MM-DD

Descrição:Criei uma copia da lista verifiquei com if se existia desordenação,
mas não consegui terminar. no final ele só faz a ordenacao uma vez.


Copyright(c) 2017 Gabriel Cavalcanti de Melo
'''
original=[]
tamLista=0
numero=input("insira um numero")
if numero=="":
    print("sua lista eh vazia")
else:
    while numero.isdigit():
        if numero.isdigit():
            original.append(int(numero))
            tamLista+=1
        numero=input("insira um numero")
    print("a)",original)

    comando=False
    cont=0
    while cont<tamLista-1:
        if original[cont]<original[cont+1]:
            comando=True
        cont+=1
    print("b)",comando)

    copia=[]
    copia=original[:]
    cont=0
    while cont<tamLista-1:
        if copia[cont]>copia[cont+1]:
            temp=copia[cont+1]
            copia[cont+1]=copia[cont]
            copia[cont]=temp
        cont+=1
    print("c)",copia)

    continua=True
    while continua:
        continua=False
        cont=0
        while cont<tamLista-1:
            if copia[cont]>copia[cont+1]:
                comando=True
                temp=copia[cont+1]
                copia[cont+1]=copia[cont]
                copia[cont]=temp
            cont+=1
            

    print("d)",copia) 
        
        
        

    
    

    

    

    
