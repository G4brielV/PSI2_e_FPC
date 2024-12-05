from typing import List, Tuple


def TSP_forca_bruta():

    restaurante = input(f"Digite as coordenadas x, y separadas por vírgula (ex: 1,2) do restaurante: ")
    x, y = map(int, restaurante.split(","))
    pontos_entrega = {"1": (x,y)}
    quant_pontos = int(input("Quantidade de Pontos de entrega: "))

    for i in range(quant_pontos):
        entrada = str(input(f"Digite as coordenadas x, y separadas por vírgula (ex: 1,2) do ponto de entrega {i+1}: "))
        x, y = map(int, entrada.split(","))
        pontos_entrega[f"{i+2}"] = (x,y)

    permutacoes = permutacao([""+str(c+2) for c in range(quant_pontos)])

    print(permutacoes)
    print(pontos_entrega)



def permutacao(entrada: List[str], pos: int = 0) -> List[str]:
    # Caso base: quando a posição chega ao final da lista, temos uma permutação completa
    if pos == len(entrada) - 1:
        return ["".join(entrada)]

    resultados = []

    for i in range(pos, len(entrada)):
        # Troca o elemento atual com o elemento da posição `pos`
        entrada[pos], entrada[i] = entrada[i], entrada[pos]

        # Faz a chamada recursiva para a próxima posição
        resultados.extend(permutacao(entrada, pos + 1))

        # Reverte a troca para restaurar o estado original da lista
        entrada[pos], entrada[i] = entrada[i], entrada[pos]

    return resultados



if __name__ == "__main__":
    TSP_forca_bruta()