def album(tot, comprou, lista):
    aux = ""
    cont=0
    while aux == "":
        if int(lista[cont]) <= tot:
            aux = f'{lista[cont]}'
        cont += 1
    for num in lista:
        for i in range(len(aux)):
            if num != aux[i] and int(num) < tot:
                pass
            else:
                break
        else:
            aux += num

    return tot - len(aux)



print(album(4, 4, "42133"))