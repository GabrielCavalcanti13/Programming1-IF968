def tokenizar(string,separador):
    lista=[]
    palavra=""
    for x in string:
        if x!=separador or x!="\n":
            palavra+=x
        else:
            lista.append(palavra)
            palavra=""
    if palavra!="":
        lista.append(palavra)
    return lista
