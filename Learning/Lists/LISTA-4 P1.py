continua=True
listaDados=[]

while continua:
    entrada=input("1.ADICIONAR(add)\n2.READ(ler)\n3.UPDATE(atualizar)\n4.DELETE(deletar)\n5.FINALIZAR(finalizar)\nO que vc deseja fazer?(digite oq esta entre parenteses) ")

    if entrada=="add":
        email=input("Qual o email? ")
        idade=int(input("Qual a idade? "))
        nome=input("Qual o nome? ")
        sexo=input("Qual o sexo? M/F")
        estadoCivil=input("Qual o estado Civil? S-solteiro C-Casado N-Namorando D-Divorciado")
        numeroAmigos=int(input("Qual a quantidade de amigos? "))
        numeroFotos=int(input("Qual a quantidade de fotos? "))
        achou=False
        for pessoa in listaDados:
            if pessoa[0]==email:
                achou=True
        if achou==False:
            listaDados.append((email,idade,nome,sexo,estadoCivil,numeroAmigos,numeroFotos))
            print("\nUsuario salvo com sucesso!")
        else:
            print("email ja cadastrado! ")

    elif entrada=="ler":
        emailBuscar=input("digite o email da pessoa desejada ")
        achou=False
        for pessoa in listaDados:
            if pessoa[0]==emailBuscar:
                achou=True
        if achou==True:
            print("Email:",pessoa[0])
            print("Idade:",pessoa[1])
            print("nome:",pessoa[2])
            print("sexo:",pessoa[3])
            print("Estado Civil:",pessoa[4])
            print("Quantidade de amigos:",pessoa[5])
            print("Quantidade de fotos:",pessoa[6])
        else:
            print("email não encontrado!")
            
            
    elif entrada=="atualizar":
        email=input("Qual o email? ")
        idade=int(input("Qual a idade? "))
        nome=input("Qual o nome? ")
        sexo=input("Qual o sexo? M/F")
        estadoCivil=input("Qual o estado Civil? S-solteiro C-Casado N-Namorando D-Divorciado")
        numeroAmigos=int(input("Qual a quantidade de amigos? "))
        numeroFotos=int(input("Qual a quantidade de fotos? "))
        atualizacao=(email,idade,nome,sexo,estadoCivil,numeroAmigos,numeroFotos)
        achou=False
        contadorLista=0
        for pessoa in listaDados:
            if pessoa[0]==email:
                listaDados[contadorLista]=atualizacao
                achou=True
                print("Cadastro atualizado!\n----------------")
            contadorLista+=1
        if achou==False:
            print("Usuario nao existente!")
        
            
        
        
     
