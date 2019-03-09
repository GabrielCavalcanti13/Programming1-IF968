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

def converter(i,string):
    if i > len(string):
        return 0
    else:
        return int(string[i-1])*(2**(len(string)-i))+converter(i+1,string)
#------------------------------------------------------------------------------#
def decodificar(string):
    if len(string) == 8:
        return chr(converter(1,string))
    else:
        #selecionar os oito primeiros items da string
        caractere=""
        cont=0
        for x in range(8):
            caractere+=string[x]
        #tirar os oito primeiros
        newString=""
        for i in range(8,len(string)):
            newString+=string[i]
        return chr(converter(1,caractere))+decodificar(newString)
#------------------------------------------------------------------------------#               
print(decodificar("01100001011011010110111101110010"))
