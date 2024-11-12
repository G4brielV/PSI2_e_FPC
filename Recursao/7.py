def permutacao_recursiva(lista):
    if len(lista) == 2:
        return 2

    else:
        return len(lista) * permutacao_recursiva(lista[1:])


print(permutacao_recursiva([1,2,3,4,5,6]))