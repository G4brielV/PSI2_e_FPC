def array_invertido(quant, lista):
    if quant == 1:
        return lista[0]

    else:
        return str(lista[-1]) + str(array_invertido(quant-1, lista[0:-1]))


print(array_invertido(7,[1,2,3,4,5,6,7]))