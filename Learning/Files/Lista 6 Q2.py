'''
Universidade Federal de Pernambuco (UFPE) (http://www.ufpe.br)
Centro de Informática (CIn) (http://www.cin.ufpe.br)
Graduando em Sistemas de Informação
IF968 - Programação 1

Autor:	Gabriel Cavalcati (gcm2)
Email:	gcm2@cin.ufpe.br
Data:	2017-10-20

Copyright(c) 2017 Gabriel Cavalcanti de Melo
'''
def tokenizar(string, separador):
    palavra=""
    lista=[]
    for x in string:
        if x!=separador:
            palavra+=x
        else:
            lista.append(palavra)
            palavra=""
    if palavra!="":
        lista.append(palavra)
    return lista
#------------------------------------------------
contador=0
voos={}
while contador<3:
    entrada=input("Digite o voo e o numero de vagas.\n")
    listaEntrada=tokenizar(entrada, " ")
    voos[listaEntrada[0]]=int(listaEntrada[1])
    contador+=1
#------------------------------------------------
continua=True
listaAtualizados=[]
listaNegados=[]
while continua:
    entrada=input("Digite o codigo do voo e o nome da pessoa.\n")
    if entrada=="fim" or entrada=="Fim":
        continua=False
    else:
        listaEntrada=tokenizar(entrada, " ")
        if listaEntrada[0] in voos:
            if voos[listaEntrada[0]]>0:
                listaAtualizados.append((listaEntrada[0],listaEntrada[1])
                voos[listaEntrada[1]]-=1
                print("Reserva no voo: "+listaEntrada[0]+" atualizada\n")
            else:
                print("Nao ha vagas disponiveis no voo: "+listaEntrada[0])
                listaNegados.append(listaEntrada[1])
        else:
            print("Voo nao existente!\n")

print(listaAtualizado)



if listaNegados!=[]:
    print("Nao conseguiram reserva:")
    for x in listaNegados:
        print(x)
    
        

         

            
            
    

    
    
    
