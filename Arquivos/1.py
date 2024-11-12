# Juvenal tem N arquivos em seu computador, cada um com um tamanho em bytes. Ele
# quer dividir estes arquivos em pastas, porém o sistema do computador é velho e só aceita
# pastas com as duas seguintes limitações:
# - Uma pasta pode ter, no máximo, dois arquivos
# - A soma dos tamanhos dos arquivos na pasta não pode exceder B bytes
# Como ele tem muitos arquivos ele prefere não criar muitas pastas. Dado o tamanho dos
# arquivos, calcule o número mínimo possível de pastas. Vamos supor um exemplo que
# temos os arquivos de tamanho 1, 2 e 3, e que o limite de bytes seja 3. A solução é colocar
# os dois primeiros arquivos juntos, totalizando apenas 2 pastas.

def reverse_bubble_sort(lista):
    for i in range(len(lista)):
        trocou = False
        for j in range(len(lista)-1,i,-1):
            if lista[j] > lista[j-1]:
                lista[j], lista[j-1] = lista[j-1], lista[j]
                trocou = True
        if not trocou:  # caso não tenha ocorrido mais trocas, mesmo antes da lista chegar ao fim, significa que ja está ordenado,
            break       # podendo parar
    return lista



def arquivos(quant, limite, lista):
    lista = reverse_bubble_sort(lista)
    i = 0
    resp = 0
    while i < len(lista):
        if lista[i] + lista[-1] <= limite:
            lista.pop()

        i += 1
        resp += 1

    return resp



print(arquivos(5,4,[4,3,1,2,1]))