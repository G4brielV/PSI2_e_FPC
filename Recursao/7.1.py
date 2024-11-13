def permutar(conjunto):
    # Caso base: se o conjunto tem apenas um símbolo, retorna a permutação única
    if len(conjunto) == 1:
        return [conjunto]

    resultados = []  # Lista para armazenar todas as permutações

    for i in range(len(conjunto)):
        # Símbolo atual
        simbolo = conjunto[i]
        # Conjunto restante excluindo o símbolo atual
        subconjunto = conjunto[:i] + conjunto[i + 1:]

        # Permutações do subconjunto restante
        for perm in permutar(subconjunto):
            resultados.append(simbolo + perm)

    return resultados


# Exemplo de uso
simbolos = "ABC"
print(permutar(simbolos))