from typing import List
def maior(lista:List[int], num:int = 0) -> int:
    #Base
    if num == len(lista)-1:
        return lista[num]

    maior_atual = lista[num]
    maior_do_resto = maior(lista, num+1)

    if maior_atual < maior_do_resto:
        maior_atual = maior_do_resto

    return maior_atual


print(maior([1,3,2]))