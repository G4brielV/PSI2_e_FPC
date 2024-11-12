def soma_array(lista):
    if len(lista) == 1:
        return lista[0]

    else:
        lista_aux = lista[:]
        lista_aux.pop()
        return lista[-1] + soma_array(lista_aux)

print(soma_array([10.2, 10.8, 20.5]))