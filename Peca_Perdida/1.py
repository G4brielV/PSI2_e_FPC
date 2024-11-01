def peca_perdida(quant, lista):
    total = (1 + quant)*quant//2
    total_faltante = 0
    for c in lista:
        total_faltante += c

    return total - total_faltante


a = 10
b = [num for num in range(1,11)]

for i in b:
    lista = b[:]
    lista.remove(i)
    resp = peca_perdida(a,lista)
    print(resp)