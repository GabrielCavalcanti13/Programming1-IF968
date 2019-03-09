print("1=domingo\n""2=segunda\n""3=terça\n""4=quarta\n""5=quinta\n""6=sexta\n""7=domingo")
dia = int(input('Qual o dia da semana que vc deseja fazer o tranporte?'))

if dia > 7 or dia < 1:
    print("codigo invalido")
else:
    if dia == 1 or dia == 2 or dia == 3:
        taxa = 25.00
    elif dia == 5 or dia == 6:
        taxa = 30.00
    else:
        taxa = 40.00

    numerodecaixas = int(input('quantas caixas vc quer transportar?'))

    preço = taxa*(.7*.8*.6)*numerodecaixas
    preço = int(preço)
    caminhoes = (.7*.8*.6*numerodecaixas)//20
    if (.7*.8*.6*numerodecaixas)%20!=0:
        caminhoes = caminhoes + 1
    caminhoes = int(caminhoes) 
    print("o custo total eh", preço)
    print("vc vai prescisar de", caminhoes, "caminhoes")
    





