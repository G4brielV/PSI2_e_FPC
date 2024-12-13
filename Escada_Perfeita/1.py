def escada(n, lista):
    pa = (n * (n+1))/2
    soma = sum(lista)
    i = soma - pa

    # Testando se há escada
    # if soma < pa or i % n != 0: --> precisa?
    #     return -1

    if i % n != 0:
        return -1

    inicio = int(i/n) + 1
    final = [c+inicio for c in range(n)]

    resp = 0

    for j in range(len(lista)):
        if lista[j] - final[j] > 0:
            resp += lista[j] - final[j]


    return resp



print(escada(5, [5,4,5,4,2]))
print(escada(6,[9,8,7,6,5,4]))
print(escada(2,[1,5]))