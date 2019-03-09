frase=input("digite uma frase: ")
parentese1=0
parentese2=0

for caractere in frase:
    if caractere=="(":
        parentese1+=1
    elif caractere==")":
        parentese2+=1

confirmacao=parentese1-parentese2
if confirmacao==0:
    print("Resultado da analise: Frase bem formada.")
elif confirmacao==1:
    print("Resultado da analise: Frase mal formada. Há",confirmacao,"parentese nao fechado")
else:
    print("Resultado da analise: Frase mal formada. Há",confirmacao,"parenteses nao fechados")

        
