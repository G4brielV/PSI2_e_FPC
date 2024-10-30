'''Verifica se o alvo existe na lista'''
def peca_faltanate(lista):
    i = 0 #posição inicial
    f = len(lista)-1 #posição final

    while i<=f:
        m=(i+f)//2
        print(f'm: {m}')
        if lista[m]+1 not in lista:
            return f'Resposta {lista[m]+1}'
        elif m + 1 == lista[m]:  # O faltante ta apos o meio
            # print("Maior")
            i = m+1
        else:
            # print("Menor")
            f = m-1
    return 1



a = 60
b = [num for num in range(1,61)]


for num in b:
    lista = b[:]
    lista.remove(num)
    resp = peca_faltanate(lista)
    print(resp)
