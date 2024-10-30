"""NÃO CONSEGUE ENCONTRAR SE FOR O '1' QUE TA FALTANDO"""

def peca(quant, list, list_natural = []):
    posi_meio = len(list)//2

    if list[posi_meio]+1 not in list and list[posi_meio]+1 not in list_natural: # Verificando se ja achou o faltante
        return list[posi_meio]+1

    if posi_meio+list[0] == list[posi_meio]: # O faltante ta apos o meio
        resp = peca(quant//2, list[posi_meio:], list)
        # print("Depois ")

    else:
        resp = peca(quant//2, list[:posi_meio], list)
        # print("Antes")

    return resp


# a = int(input("Quant de peça: "))
# b = [int(input("Digite o num: ")) for _ in range(a - 1)]

a = 60
b = [num for num in range(1,61)]


for num in b:
    lista = b[:]
    lista.remove(num)
    resp = peca(a, lista)
    print(resp)