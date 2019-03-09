'''
Universidade Federal de Pernambuco (UFPE) (http://www.ufpe.br)
Centro de Informática (CIn) (http://www.cin.ufpe.br)
Graduando em Sistemas de Informação
IF968 - Programação 1

Autor:	Gabriel Cavalcanti(gcm2)
Email:	gcm2@cin.ufpe.br
Data:	1998-10-13

Copyright(c) 2017 Gabriel Cavalcanti
'''
texto=input("Digite um texto ")
print("a)"+texto)

palavra=""
contagem=0
for caractere in  texto:
    if caractere!=" ":
        palavra+=caractere
    else:
        contagem+=1
print("b)"+palavra+" "+str(contagem)+".")

lista=[]
palavra=""
for caractere in texto:
    if caractere!=" ":
        palavra+=caractere
    else:
        lista.append(palavra)
        palavra=""
print("c)"+str(lista))

lista=[]
palavra=""
for caractere in  texto:
    if caractere!=" ":
        palavra+=caractere
    else:
        if palavra!="":
            lista.append(palavra)
            palavra=""
lista.append(palavra)
print("d)"+str(lista))
