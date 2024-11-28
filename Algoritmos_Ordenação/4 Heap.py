from random import randint


def heapSort(A):
    build_max_heap(A) # --> Log(n)//2
    for i in range(len(A)-1, 0, -1): # --> n
        A[0], A[i] = A[i], A[0]
        max_heapify(A,0, i) # log(n) --> provar com a arvore



def build_max_heap(A):
    for i in range((len(A)//2)-1, -1, -1):
        max_heapify(A,i,len(A)-1)


def max_heapify(A,i, tamanho):
    maior = i
    left = (2 * i)+1
    right = (2 * i)+2
    if left < tamanho and A[left] > A[maior]:
        maior = left

    if right < tamanho and A[right] > A[maior]:
        maior = right

    if maior != i:
        A[i], A[maior] = A[maior], A[i]
        max_heapify(A, maior, tamanho)

#    1   2   3   4  5  6  7  8  9, 10
a = [16, 4, 10, 14, 7, 9, 3, 2, 8, 1]
lista = []
for _ in range(10):
    lista.append(randint(1,1000))

# heapSort(lista)
heapSort(a)
print(a)