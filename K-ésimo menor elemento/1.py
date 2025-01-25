def k_esimo_menor(lista, k):
    for _ in range(k):
        m = float("inf")
        tmp = 1
        for e in range(len(lista)):
            if lista[e] < m:
                m = lista[e]
                tmp = e
        lista.pop(tmp)

    return m






lista = [3,1,2,5,4]
k = 3
print(k_esimo_menor(lista, k))