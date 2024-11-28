from typing import List, Tuple

def permutacao(pontos_entrega: str) -> List[Tuple[str]]:
    tupla = tuple(pontos_entrega)
    n = len(pontos_entrega)

    possiveis_caminhos = [tupla]

    indices = [i for i in range(n)]
    ciclos = [i for i in range(n, 0, -1)]

    while True:
        for i in range(n - 1, -1, -1):
            ciclos[i] -= 1
            if ciclos[i] == 0:
                # Reseta o ciclo/quantidade de trocas que a "casa" fará
                indices[i:] = indices[i + 1:] + indices[i:i + 1]
                ciclos[i] = n - i
            else:
                # Troca de elementos
                j = ciclos[i]
                indices[i], indices[-j] = indices[-j], indices[i]

                # Novo permutado
                p = [tupla[i] for i in indices]
                possiveis_caminhos.append(tuple(p))
                break
        else:
            break

    return possiveis_caminhos


a = permutacao("ABC")
print(a, len(a))