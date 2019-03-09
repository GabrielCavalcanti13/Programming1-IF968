tamanhoDaLista=int(input("digite a quantidade de palavras que vc digitará"))
lista=[]
while tamanhoDaLista>0:
    palavra=input("digite a palavra")
    lista.append(palavra)
    tamanhoDaLista-=1
for x in lista:
    if x != "segredo":
        print(x)
