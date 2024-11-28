from typing import List

def substring_0_lacos(texto: str, idx1: int = 0, idx2: int = 1) -> str | list[str]:

    lista = []

    lista.append(texto[idx1:idx2])

    # Base
    if idx1 == len(texto) - 1:
        return texto[-1]

    if idx2 == len(texto) + 1:
        return substring_0_lacos(texto, idx1+1, idx1+2)

    lista.extend(substring_0_lacos(texto, idx1, idx2+1))


    return lista


print(substring_0_lacos("ABC"))