"""quebrando a banca"""
def maior(lista_saldo, inicio, fim):
    if inicio == fim:
        return inicio
    maior_idx, maior_numero = inicio, lista_saldo[inicio]
    for i in range(inicio+1, fim+1):
        if lista_saldo[i] > maior_numero:
            maior_numero = lista_saldo[i]
            maior_idx = i
    return maior_idx

def principal():
    # leitura da entrada
    n_digitos, n_removidos = [int(i) for i in input().split()]
    lista_saldo = [int(i) for i in input()]

    # compute
    maior_idx = -1
    n_saldo = n_digitos - n_removidos
    for i in range(n_saldo):
        inicio = maior_idx + 1
        fim = n_digitos - (n_saldo - i)
        maior_idx = maior(lista_saldo, inicio, fim)
        print(lista_saldo[maior_idx], end="")
    print()
if __name__ == "__main__":
    principal()