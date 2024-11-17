def insertion_sort(A):
    for i in range(1, len(A)):
        j = i - 1
        chave = A[i]
        while j >= 0 and A[j] > chave:
            A[j+1] = A[j]
            j -= 1

        A[j+1] = chave

    return A


a = [0, 3, 6, 8, 2, 4, 5, 1, 9, 7]
insertion_sort(a)
print(f'Resposta: {a}')