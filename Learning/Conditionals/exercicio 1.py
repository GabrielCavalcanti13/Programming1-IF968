entrada = input()

if entrada.isdigit()==True:
    entrada=int(entrada)
    if entrada==0:
        print('inteiro\n'+"neutro")
    elif entrada%2 == 0:
        print('Inteiro\n'+'par')
    else:
        print('inteiro\n'+ 'impar')

elif entrada=='True':
    print("Booleano")

elif entrada=='False':
    print("Booleano")

else:
    print("string")
    print(len(entrada))
    






    
