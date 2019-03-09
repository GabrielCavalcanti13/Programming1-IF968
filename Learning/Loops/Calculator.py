continua=True
while continua == True:
    numero1 = int(input("digite o primeiro numero "))
    operador = input("digite o operador ")
    numero2 = input("digite o outro numero ")
    if numero2=="fim":
        continua=False
    else:
        numero2=int(numero2)
        if operador == "+":
            print(numero1+numero2)
        elif operador == "-":
            print(numero1-numero2)
        elif operador == "*":
            cont=0
            soma=0
            while cont < numero2:
                soma+=numero1
                cont+=1
            print(soma)
        elif operador == "//":
            if numero2==0:
                print("erro. divisao por zero")
            else:
                result=0
                while numero1>=numero2:
                    numero1-=numero2
                    result+=1
                print(result)
        elif operador == "^":
            print(numero1**numero2)
        elif operador == "!":
            fat=numero1
            res=fat
            fat-=1
            while fat > 1:
                numX=res
                numY=fat
                cont=0
                resFat=0
                while cont<numX:
                    resFat+=numY
                    cont+=1
                    fat=fat-1
            res=resFat
            print(res)
        elif operador == "%":
            while numero1>=numero2:
                numero1-=numero2
            print(numero1)
        else:
            print("operador invalido")
