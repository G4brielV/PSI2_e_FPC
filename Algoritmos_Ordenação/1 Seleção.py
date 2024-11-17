def selecao_sort(A,n = None):
    if n is None:
        n = len(A)
    for i in range(n-1):
        menor = i
        for j in range(i+1,n):
            if A[j] < A[menor]:
                menor = j

        A[i], A[menor] = A[menor], A[i]


a = [0, 3, 6, 8, 2, 4, 5, 1, 9, 7]
selecao_sort(a)
print(f'Resposta: {a}')