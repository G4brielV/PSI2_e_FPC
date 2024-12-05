def permutacao(n, posi=0):

    resultado = []

    if len(n)-1 == posi:
        return ["".join(n)]

    for p in range(posi, len(n)):

        n[p], n[posi] = n[posi], n[p]

        resultado.extend(permutacao(n, posi+1))

        n[posi], n[p] = n[p], n[posi]

    return resultado


# Exemplo de uso
simbolos = ["A", "B", "C"]
print(permutacao(simbolos))