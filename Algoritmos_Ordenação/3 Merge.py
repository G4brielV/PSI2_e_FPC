def merge_sort(lista, p, r):
    # condição de parada
    if p >= r:
        return
    else:
        q = (p + r) // 2 #posição do elemento do meio

        merge_sort(lista, p, q) # dividindo a lista em 2, vai do inicio ao meio
        merge_sort(lista, q + 1, r) # dividindo a lista em 2, vai do meio+1 ate o fim

        intercalar(lista, p, q, r) # comparar os numeros


def intercalar(lista, p, q, r):
    Left = lista[p:q+1]
    Left.append(float("inf"))
    Right = lista[q + 1:r+1]
    Right.append(float("inf"))
    i = j = 0

    for k in range(p, r + 1):
        if Left[i] <= Right[j]:
            # entra quando não tiver elementos na primeira metade
            lista[k] = Left[i]
            i += 1

        else: # temp[j] > temp[i]
            # retirar elemento da segunda metade
            lista[k] = Right[j]
            j += 1




a = [0, 3, 6, 8, 2, 4, 5, 1, 9, 7]
merge_sort(a, 0, len(a)-1)
print(f'Resposta: {a}')