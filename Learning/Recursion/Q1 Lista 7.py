'''
Universidade Federal de Pernambuco (UFPE) (http://www.ufpe.br)
Centro de Informática (CIn) (http://www.cin.ufpe.br)
Graduando em Sistemas de Informação
IF968 - Programação 1

Autor:	Gabriel Cavalcati (gcm2)
Email:	gcm2@cin.ufpe.br
Data:	24-11-2017

Copyright(c) 2017 Gabriel Cavalcanti de Melo
'''
def minimo(lista):
    if len(lista)==1:
        return lista[0]
    else:
        if lista[0]>=lista[1]:
            del lista[0]
        else:
            del lista[1]
        return minimo(lista)
#------------------------------------------------------------------------------
def selection(lista):
    if lista==[]:
        return []
    else:
        menor = minimo(lista[:])
        listaResultado = []
        for x in lista:
            if x != menor:
                listaResultado.append(x)
            else:
                menor2=menor
                menor=""
        return [menor2]+selection(listaResultado)
        
