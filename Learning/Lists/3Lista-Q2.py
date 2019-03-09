continua=True
listaProdutos=[]
tamLista=0
prodNegados=0

while continua==True:
    produto=input("Digite um produto a ser inserido ")
    if produto!="FIM":
        cont=0
        achou=False
        while cont<tamLista:
            if listaProdutos[cont]==produto:
                achou=True
                prodNegados+=1
            cont+=1
        if achou==False:
            listaProdutos.append(produto)
            tamLista+=1
    else:
        continua=False
        print("Produtos:\n",listaProdutos,"\nForam cadastrados:",tamLista,"produtos")
        print("foram negados:",prodNegados,"produtos")
        
            
        
        
    
