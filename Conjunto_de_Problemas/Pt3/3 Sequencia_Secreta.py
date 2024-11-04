def seq_secreta(quant, lista):
    resp = 1
    for num in range(0,len(lista)):
        if lista[num] == "2" and lista[num+1] != "2":
            resp += 2

    return resp




print(seq_secreta(6, "121222112211"))