from typing import List

def substring_2_lacos(texto: str) -> List[str]:

    lista = []

    for i in range(len(texto)):
        for j in range(i + 1, len(texto) + 1):
            lista.append(texto[i:j])

    return lista


print(substring_2_lacos("ABCD"))
