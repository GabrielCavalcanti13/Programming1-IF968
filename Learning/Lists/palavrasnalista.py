entrada=input("digite uma frase ")
listaPalavras=[]

palavra=""
for x in entrada:
    if x!=" ":
        palavra+=x
    else:
        if palavra!="":
            listaPalavras.append(palavra)
            palavra=""
if palavra!="":
    listaPalavras.append(palavra)
print(listaPalavras)
