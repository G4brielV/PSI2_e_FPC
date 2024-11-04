"""Tem q considerar que não está faltando o 1 ou o ultimo elemento e que a lista ta ordenada"""

def peca_perdida(quant, lista):
    i = 0
    f = len(lista)-1
    while True:
        meio = (i + f) // 2

        if lista[meio]+1 not in lista[meio - 1:meio + 2]:
            return lista[meio]+1

        elif lista[meio] == meio + 1: # O faltante da depois
            i = meio

        else:   # O faltante ta antes
            f = meio



a = 10
b = [num for num in range(1,11)]

for i in range(2,10):
    lista = b[:]
    lista.remove(i)
    resp = peca_perdida(a,lista)
    print(resp)
