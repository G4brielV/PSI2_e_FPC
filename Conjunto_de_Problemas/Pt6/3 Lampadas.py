def lampada(quant, lista):
    resp = []

    #Lampada 1:
    if len(lista)%2 == 0:
        resp.append(0)
    else:
        resp.append(1)

    #Lampada 2:
    for num in lista:
        if num == 1:
            lista.remove(1)

    if len(lista)%2 == 0:
        resp.append(0)
    else:
        resp.append(1)

    return "".join(str(resp))


print(lampada(3,[1,2,2]))
print(lampada(4,[2,1,2,2]))