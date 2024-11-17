from random import randint

# Adicionando uma randomização na escolha do pivo

def quick_sort(A, p=0 ,r = None):
    if r is None:
        r = len(A)-1
    if p >= r:
        return
    else:
        q = particionar(A,p,r)
        quick_sort(A, p, q-1)
        quick_sort(A, q+1, r)


def particionar(A, p, r):
    # q --> posição futura do pivo
    q = p

    # Melhorar casos de [1,2,3,4] ou [4,3,2,1], onde a divisão ficaria com [] e [n-1], ajutando a equivalência entre as divisões
    pivo = randint(p, r)
    # pivo = mediana(p,r)

    A[r], A[pivo] = A[pivo], A[r]
    for u in range(p,r):
        if A[u] <= A[r]: # O numero é menor q o pivô? --> se for --> num pega a localização atual do pivô e o pivô anda uma para frente
            A[q], A[u] = A[u], A[q]
            q+=1
    A[q], A[r] = A[r], A[q]
    return q


def mediana(p,r):
    a, b, c = randint(p, r), randint(p, r), randint(p, r)
    if a > b > c or c > b > a:
        pivo = b
    elif b > a > c or c > a > b:
        pivo = a
    else:
        pivo = c
    return pivo



a = [0, 3, 6, 8, 2, 4, 5, 1, 9, 7]
b = [0,3,4,1,2]
quick_sort(b)
print(f'Resposta: {b}')