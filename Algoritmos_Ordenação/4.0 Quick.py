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
    # A[r] é o pivô
    for u in range(p,r):
        if A[u] <= A[r]: # O numero é menor q o pivô? --> se for --> num pega a localização atual do pivô e o pivô anda uma para frente
            A[q], A[u] = A[u], A[q]
            q+=1
    A[q], A[r] = A[r], A[q]
    return q





a = [0, 3, 6, 8, 2, 4, 5, 1, 9, 7]
b = [0,3,4,1,2]
quick_sort(b)
print(f'Resposta: {b}')