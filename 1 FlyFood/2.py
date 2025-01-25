import time
from typing import List, Tuple, Dict, Any


def TSP_forca_bruta():


    pontos = {"R": (12, 87),
              "P1": (23,48), "P2": (32,64), "P3": (90,3), "P4":(64,76), "P5":(54,52),
              "P6":(2,34),
              "P7":(26,72),
              "P8":(38,17),
              "P9":(10,90),
              "P10":(41,52),
              "P11":(65,11),
              "P12":(32,97)}

    antes = time.time()
    melhor_caminho(pontos, ["P1", "P2", "P3", "P4", "P5", "P6", "P7", "P8", "P9", "P10", "P11", "P12"])
    depois = time.time()

    return depois - antes




def melhor_caminho(pontos: Dict[str, Tuple[str]], entrada: List[str], pos: int = 0, melhor_preco = float("inf"), caminho = "") -> str:

    # Caso base: quando a posição chega ao final da lista, temos uma permutação completa
    if pos == len(entrada) - 1:
        preco_caminho = calcular_caminho(pontos, entrada)

        if preco_caminho < melhor_preco:
            melhor_preco = preco_caminho
            caminho = " ".join(entrada)

        if pos == 0:
            return caminho

        return melhor_preco, caminho


    for i in range(pos, len(entrada)):
        # Troca o elemento atual com o elemento da posição `pos`
        entrada[pos], entrada[i] = entrada[i], entrada[pos]

        # Faz a chamada recursiva para a próxima posição
        melhor_preco, caminho = melhor_caminho(pontos, entrada, pos + 1, melhor_preco, caminho)

        # Reverte a troca para restaurar o estado original da lista
        entrada[pos], entrada[i] = entrada[i], entrada[pos]

    if pos == 0:
        return caminho

    else:
        return melhor_preco, caminho


def distancia_Manhattan(ponto1: Tuple[str], ponto2: Tuple[str]) -> int:
    distancia = 0
    if ponto1[0] >= ponto2[0]:
        distancia += ponto1[0] - ponto2[0]

    else:
        distancia += ponto2[0] - ponto1[0]

    if ponto1[1] >= ponto2[1]:
        distancia += ponto1[1] - ponto2[1]

    else:
        distancia += ponto2[1] - ponto1[1]

    return int(distancia)


def calcular_caminho(pontos: Dict[str, Tuple[str]], caminho:List[str]) -> int:
    percurso = 0
    for c in range(len(caminho)):
        if c == 0:
            percurso += distancia_Manhattan(pontos["R"], pontos[caminho[c]])  # Restaurante -> 1 ponto
            percurso += distancia_Manhattan(pontos[caminho[c]], pontos[caminho[c + 1]])  # 1 ponto ate o 2

        elif c == len(caminho) - 1:
            percurso += distancia_Manhattan(pontos["R"], pontos[caminho[-1]])  # Último ponto -> restaurante

        else:
            percurso += distancia_Manhattan(pontos[caminho[c]],
                                                  pontos[caminho[c + 1]])  # De um ponto ate o próximo


    return percurso




if __name__ == "__main__":
    print(TSP_forca_bruta())