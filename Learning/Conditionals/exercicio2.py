n1 = input()
n2 = input()
n3 = input()

if n1.isdigit()==False:
    n1 = int(n1)
if n2.isdigit()==False:
    n2 = int(n2)
if n3.isdigit()==False:
    n3 = int(n3)

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
