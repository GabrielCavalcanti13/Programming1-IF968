n1 = int(input())
n2 = int(input())
n3 = int(input())

if n1==n3 or n1==n2 or n2==n3:
    print("vc deve colocar numeros diferentes")
    n1 = int(input())
    n2 = int(input())
    n3 = int(input())

if n1 < n2 and n1 > n3:
    print('Maior:' + str(n2))
    print("Menor:" + str(n3))
    
elif n2 < n1 and n2 > n3:
    print('Maior:' + str(n1))
    print("Menor:" + str(n3))
    
elif n3 < n1 and n3 > n2:
    print('Maior:' + str(n1))
    print("Menor:" + str(n2))
    
elif n1 < n3 and n1 > n2:
    print('Maior:' + str(n3))
    print("Menor:" + str(n2))
    
elif n2 < n3 and n2 > n1:
    print('Maior:' + str(n3))
    print("Menor:" + str(n1))

elif n3 < n2 and n3 > n1:
    print('Maior:' + str(n2))
    print('Menor:' + str(n1))
