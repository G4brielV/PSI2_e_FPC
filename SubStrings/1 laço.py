from typing import List

def substring_1_lacos(texto: str, idx: int = 0) -> List[str]:

    lista = []

    if idx == len(texto)-1:
        return texto[idx]

    for i in range(len(texto), 0+idx, -1):
        lista.append(texto[idx:i])

    lista.extend(substring_1_lacos(texto, idx+1))


    return lista


print(substring_1_lacos("ABCD"))