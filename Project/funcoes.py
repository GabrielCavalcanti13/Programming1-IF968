'''
Universidade Federal de Pernambuco (UFPE) (http://www.ufpe.br)
Centro de Informática (CIn) (http://www.cin.ufpe.br)
Graduando em Sistemas de Informação
IF968 - Programação 1

Autor:	Gabriel Cavalcati (gcm2)
Email:	gcm2@cin.ufpe.br
Data:	13/11/2017

Copyright(c) 2017 Gabriel Cavalcanti de Melo
'''
#---------------------------------------------------
from datetime import datetime
bancoUsuarios={}
bancoElementos={}
#_______________________________LER_TXT__________________________________
def loadUsers():
    '''Essa funcao vai ler todo o txt de usuarios e descritografara
colocando no dicionarios de usuarios q sera usado no resto do programa.
o txt esta organizado de maneira em q a cada tres linhas respresentam um
um usuario. seguindo a ordem: login, senha, nivel de acesso'''
    usuarios=open("usuarios.txt","r")
    continua=True
    while continua:
        login=descriptografar(usuarios.readline()," ")
        senha=descriptografar(usuarios.readline()," ")
        nivel=descriptografar(usuarios.readline()," ")
        if login=="":
            continua=False
        else:
            bancoUsuarios[login]=(senha,nivel)
    usuarios.close()
#_______________________________LER_TXT___________________________________
def loadAnimals():
    '''Essa funcao vai ler o txt de elementos. descriptografando cada linha. a primeira linha do arquivo será sempre para
guardar a informação do contador de ID dos animais. por isso sempre q comecar
o programa a primeira linha sera lida antes do laco. depois segue a ordem
de id de cada animal, especie, idade, peso e por ultimo o sexo'''
    global contadorId
    elementos=open("elementos.txt","r")
    contadorId=int(descriptografar(elementos.readline()," "))
    continua=True
    while continua:
        idAnimal=descriptografar(elementos.readline()," ")
        especie=descriptografar(elementos.readline()," ")
        idade=descriptografar(elementos.readline()," ")
        peso=descriptografar(elementos.readline()," ")
        sexo=descriptografar(elementos.readline()," ")
        if idAnimal=="":
            continua=False
        else:
            bancoElementos[idAnimal]=(especie,idade,peso,sexo)
    elementos.close()
#-----------------------------------------------------------
def criptografar(string):
    '''Para cada caractere da string se ela nao for a ultima eu codifico
e coloco espaco para separar cada string. se nao eh adicionado \n para terminar
a linha'''
    palavra=""
    contador=1
    for x in string:
        if contador<len(string):
            palavra+=str(ord(x)+37)+" "
        elif contador==len(string):
            palavra+=str(ord(x)+37)+"\n"
        contador+=1
    return palavra
#-----------------------------------------------------------
def descriptografar(string, separador):
    '''enquanto nao for \n a funcao vai juntando os caracteres ate chegar num
num espaco. entao ele faz a decodificacao e parte para o proximo conjunto de
 numeros q formam um caractere codificado. chegando no \n retorna o resultado
 por exemplo: 125 136 123. ele vai junto numero por numero. 1 depois 12 depois
 125. chegou espaço. o 125 sera decoficado e o caractere desse codigo eh adicio
 nado ao resultado e assim vai ate o \n'''
    continua=True
    caractere=""
    resultado=""
    for x in string:
        if x!="\n":
            if x != separador:
                caractere+=x
            else:
                resultado+=chr(int(caractere)-37)
                caractere=""
        else:
            if caractere!="1" and caractere!="3" and caractere!="2" and caractere!="4": 
                resultado+=chr(int(caractere)-37)
            else:
                resultado+=caractere
    return resultado
#-------------------------------------------------
def salvarLog(usuario, acao, arquivo):
    '''essa funcao vai receber o usuario q esta logado, a acao realizada
e qual arquivo sera adicionado o log. por exemplo: salvarLog(adm, cadastrou,
log.txt)'''
    data = datetime.now()
    arquivo.write(usuario+" "+acao+" em "+str(data.day)+"/"+str(data.month)+"/"+str(data.year)+" as "+str(data.hour)+":"+str(data.minute)+"\n")




