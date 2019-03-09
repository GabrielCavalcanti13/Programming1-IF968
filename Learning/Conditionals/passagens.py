print("Destino/","Cidade/","Tarifa")
print("1/","Salvador/", "126.30")
print("2/","Joao Pessoa/","67.00")
print("3/","Fortaleza/","164.87")
print("4/","Sao Paulo/","264.00")
print("5/","Rio de Janeiro/","282.34")
print("6/","Porto Alegre/","365.90")

codigo1 = 126.30 
codigo2 = 67.00
codigo3 = 164.87
codigo4 = 264.00
codigo5 = 282.34
codigo6 = 365.00

valorpassagem = input("Qual o codigo do destino desejado?")
valorpassagem = valorpassagem
dinheiro = float(input("Qual a quantia recebida"))

if valorpassagem > 6 or valorpassagem < 1:
    print("codigo invalido")
elif valorpassagem == 1:
    destino = "Salvador"
elif valorpassagem == 2:
    destino = "Joao Pessoa"
elif valorpassagem == 3:
    destino = "Fortaleza"
elif valorpassagem == 4:
    destino = "São Paulo"
elif valorpassagem == 5:
    destino = "Rio ds Janeiro"
else:
    destino = "Porto  Alegre"


    if dinheiro < valorpassagem:
        print("dinheiro insuficiente")
    else:
        troco = dinheiro - valorpassagem
        print("o destino eh:",destino)
        print("Valor:",valorpassagem)
        print("troco:", troco)
