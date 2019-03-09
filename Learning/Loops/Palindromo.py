continua=True
while continua:
    palavraInversa=""
    palavra=input("digite uma palavra ")
    cont=len(palavra)
    if palavra!="":
        while cont>0:
            palavraInversa+=palavra[cont-1]
            cont-=1
    else:
        continua=False
    if palavra==palavraInversa:
        print(True)
    else:
        print(False)
    
        
    
        
