def k_esimo_menor(lista, k, p=0, q=-1):
    if q == -1:
        q = len(lista)-1
    x = mini_part(lista, p, q)
    if x == k-1:
        return lista[x]
    elif x < k-1:
        return k_esimo_menor(lista, k, x+1, q)
    else: # x > k-1
        return k_esimo_menor(lista, k, p, x-1)

def mini_part(lista, p, q):
    # lista[q] == pivo
    posi = p
    for i in range(p, q):
        if lista[i] <= lista[q]:
            lista[posi], lista[i] = lista[i], lista[posi]
            posi += 1
    lista[posi], lista[q] = lista[q], lista[posi]
    return posi


lista = [30,10,20,50,40,70,60]
k = 4
print(k_esimo_menor(lista, k))