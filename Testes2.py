from typing import List


def permutacoes(entrada: List[str], pos: int = 0) -> List[str]:
    # Caso base: quando a posição chega ao final da lista, temos uma permutação completa
    if pos == len(entrada) - 1:
        return ["".join(entrada)]

    resultados = []

    for i in range(pos, len(entrada)):
        # Troca o elemento atual com o elemento da posição `pos`
        entrada[pos], entrada[i] = entrada[i], entrada[pos]

        # Faz a chamada recursiva para a próxima posição
        resultados.extend(permutacoes(entrada, pos + 1))

        # Reverte a troca para restaurar o estado original da lista
        entrada[pos], entrada[i] = entrada[i], entrada[pos]

    return resultados


# Exemplo de uso
simbolos = ["A", "B", "C"]
print(permutacoes(simbolos))