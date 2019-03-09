'''
Universidade Federal de Pernambuco (UFPE) (http://www.ufpe.br)
Centro de Informática (CIn) (http://www.cin.ufpe.br)
Graduando em Sistemas de Informação
IF968 - Programação 1

Autor:	Gabriel Cavalcati (gcm2)
Email:	gcm2@cin.ufpe.br
Data:	AAAA-MM-DD

Copyright(c) 2017 Gabriel Cavalcanti de Melo
'''
#---------------------------------------------------------------
def tokenizar(string,separador):
    listaPalavras=[]
    palavra=''
    for x in string:
        if x != " ":
            palavra+=x
        else:
            listaPalavras.append(palavra)
            palavra=""
    if palavra != "" or palavra!= " ":
        listaPalavras.append(palavra)
    return listaPalavras
#---------------------------------------------------------------
def filtragem(posicaoFiltro,filtro,dicionario):
    itensFiltrados={}
    for x in dicionario.items():
        if x[1][posicaoFiltro]==filtro:
            itensFiltrados[x[0]]=x[1]
    return itensFiltrados  
#--------------------------------------------------------------
def tipoFiltro(filtro):
    if filtro=="tipo" or filtro=="Tipo":    #Essa funcao vai trocar a string por um inteiro
        filtro=0                        #q vai servir para a posicao d item na tupla.
    elif filtro=="Fabricante" or filtro=="fabricante":
        filtro=1
    elif filtro=="Modelo" or filtro=="modelo":
        filtro=2
    elif filtro=="Portas/Capacidade":
        filtro=3
    return filtro
#---------------------------------------------------------------
def searchList(,dicionario):
    for key in carrosCadastrados.items():
            if key[0]==placa:
                achou=True
#---------------------------------------------------------------
carrosCadastrados={} #nessa etapa. Tokenizei a string e passei todos para o dicionario de
carrosAlugados={}   #carros cadastrados usando modulo 9 para adicioar todos em mesma ordem
continua=True
listaItens=tokenizar("carro Toyota Corolla 2 10.29 2017 PMW-6285 "+
                     "83101851345 9BRGZ1AG7843J6IO4 van Mercedes-Benz "+
                     "Sprinter 10 7.5 2016 OIJ-5046 33829885082 "+
                     "9BM70ZIA2QL5TPNQB carro Honda Civic 4 9.41 2017 "+
                     "PIO-1760 88655507018 93HNXUVUKDM1NDTZG van Mercedes-Benz "+
                     "Sprinter 16 8.98 2016 PDC-0021 75572718509 9BMJIWI92WHVK2674 "+
                     "carro Chevrolet Spin 2 7.73 2016 PLR-3307 23090061575 "+
                     "9BGYG85LX4UD3JY0O carro Ford Ka+ 4 12.66 2017 PRC-8376 "+
                     "45376362546 9BFOCNJFWP3T0SMAR carro Honda Civic 2 9.52 2017 "+
                     "PFT-6721 07442827832 93H1EW4VW9G2WAJBA van Fiat Ducato 12 8.62 "+
                     "2016 PKI-4121 67784657648 9BDHRGL809MG8CT5K van Fiat Ducato "+
                     "11 12.05 2015 PHC-1959 08057942653 9BDUFBEMF030IUCLG"," ")
contador=0
while contador<len(listaItens):
    carrosCadastrados[listaItens[contador+6]]=(listaItens[contador],
                                               listaItens[contador+1],listaItens[contador+2],
                                               listaItens[contador+3],listaItens[contador+4],
                                               listaItens[contador+5],listaItens[contador+7],
                                               listaItens[contador+8])
    contador+=9
#----------------------------------------------------------------------------

while continua:
    entrada=input("--------BEM VINDO-------\n\n"
                  "------------------------\n"+
                  "1.VERIFICAR CATALOGO\n"+
                  "2.CONSULTAR VEICULO\n"+
                  "3.ALUGAR VEICULO\n"+
                  "4.DEVOLVER VEICUL0\n"+
                  "5.SAIR\n"+
                  "------------------------\n")
#---------------------------------------------------------------------------
    if entrada == "1":
        comando=input("Deseja aplicar algum Filtro? s/n")
        if comando == "s":
            quantidadeFiltros=input("Quantos filtros vc deseja aplicar? 1/2")
            if quantidadeFiltros=="1":
                filtro=input("Qual Filtro vc deseja aplicar?\n"+
                             "-----------------------------\n"+
                             " Tipo\n"+
                             " Fabricante\n"+
                             " Modelo\n"+
                             " Portas/Capacidade\n")
                itemDesejado=input("Qual "+filtro+" vc deseja aplicar? ")
                filtro=tipoFiltro(filtro)
                carrosFiltrados=filtragem(filtro,itemDesejado,carrosCadastrados)
                for key in carrosFiltrados.items():
                    print("-------------------\n"+
                    "Placa: "+key[0]+"\n"+
                    "Tipo: "+key[1][0]+"\n"+
                    "Fabricante: "+key[1][1]+"\n"+
                    "Modelo: "+key[1][2]+"\n"+
                    "Portas: "+key[1][3]+"\n"+
                    "Autonomia: "+key[1][4]+"\n"+
                    "Ano: "+key[1][5]+"\n"+
                    "Renavam: "+key[1][6]+"\n"+
                    "Chassi: "+key[1][7]+"\n"+
                    "------------------\n")
                if len(carrosFiltrados)==0:
                    print("Nenhum veiculo encontrado!n")
            elif quantidadeFiltros=="2":
                filtro1=input("Qual Filtro vc deseja aplicar?\n"+
                             "-----------------------------\n"+
                             " Tipo\n"+
                             " Fabricante\n"+
                             " Modelo\n"+
                             " Portas/Capacidade\n")
                itemDesejado1=input("Qual "+filtro1+" vc deseja aplicar? ")
                filtro1=tipoFiltro(filtro1)
                carrosFiltrados=filtragem(filtro1,itemDesejado1,carrosCadastrados)
                filtro2=input("Qual outro Filtro vc deseja aplicar?\n"+
                             "-----------------------------\n"+
                             " Tipo\n"+
                             " Fabricante\n"+
                             " Modelo\n"+
                             " Portas/Capacidade\n")
                itemDesejado2=input("Qual "+filtro2+" vc deseja aplicar? ")
                filtro2=tipoFiltro(filtro2)
                carrosFiltrados2=filtragem(filtro2,itemDesejado2,carrosFiltrados)
                
                for key in carrosFiltrados2.items():
                    print("-------------------\n"+    #nesse caso a filtragem 2 é feita 
                    "Placa: "+key[0]+"\n"+          #em cima da filtragem 1
                    "Tipo: "+key[1][0]+"\n"+
                    "Fabricante: "+key[1][1]+"\n"+
                    "Modelo: "+key[1][2]+"\n"+
                    "Portas: "+key[1][3]+"\n"+
                    "Autonomia: "+key[1][4]+"\n"+
                    "Ano: "+key[1][5]+"\n"+
                    "Renavam: "+key[1][6]+"\n"+
                    "Chassi: "+key[1][7]+"\n"+
                    "------------------\n")
                if len(carrosFiltrados2)==0:
                    print("Nenhum veiculo encontrado!\n")
#----------------------------------------------------------------------------
    elif entrada == "2":
        placa=input("Digite a placa do carro que deseja consultar.\n")
        achou=False
        for key in carrosCadastrados.items():
            if key[0] == placa:
                print("-------------------\n"+
                      "Placa: "+key[0]+"\n"+
                      "Tipo: "+key[1][0]+"\n"+
                      "Fabricante: "+key[1][1]+"\n"+
                      "Modelo: "+key[1][2]+"\n"+
                      "Portas: "+key[1][3]+"\n"+
                      "Autonomia: "+key[1][4]+"\n"+
                      "Ano: "+key[1][5]+"\n"+
                      "Renavam: "+key[1][6]+"\n"+
                      "Chassi: "+key[1][7]+"\n"+
                      "------------------\n")
                achou=True
        if achou==False:
            print("Veiculo nao encontrado!\n")
#---------------------------------------------------------------------------
    elif entrada=="3":
        placa=input("Digite a placa do carro q vc deseja alugar!\n")
        achou=False
        for key in carrosCadastrados.items():
            if key[0]==placa:
                achou=True
                comando=input("Vc deseja alugar:\n"+
                          key[1][0]+"\n"+
                          key[1][1]+"\n"+
                          key[1][2]+" ? (s/n)\n")
                chaveExcluir=key
        if comando=="s":
            carrosCadastrados.pop(chaveExcluir[0])
            carrosAlugados[chaveExcluir[0]]=chaveExcluir[1]
            print("######VEICULO ALUGADO COM SUCESSO#######")
        if achou==False:
            print("Veiculo nao encontrado. \n")
#--------------------------------------------------------------------------
    elif entrada=="4":
        placa=input("Digite a placa do carro q vc deseja devolver.\n")
        for key in carrosAlugados.items():
            if key[0]==placa:
                
            
                
                
                
            
        
        
        
