listaCapitais=[]
continua=True
capital=" "
tamanhoLista=0

while capital!="":
    capital=input("digite uma capital")
    if capital!="":
        listaCapitais.append(capital)
        tamanhoLista+=1

comando=input("vc dejesa deletar alguma capital s/n ")
if comando=="s":
    deletar=input("Qual capital vc dejesa deletar ")
    cont=0
    achou=False
    while cont<tamanhoLista:
        if listaCapitais[cont]==deletar:
            del listaCapitais[cont]
            tamanhoLista-=1
            achou=True
        cont+=1
    if achou!=True:
         print("a capital não foi encontrada")
        
print(listaCapitais,tamanhoLista)
