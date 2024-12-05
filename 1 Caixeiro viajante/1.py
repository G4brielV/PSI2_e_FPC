from typing import List, Tuple, Dict


def TSP_forca_bruta():

    restaurante = input(f"Digite as coordenadas x, y separadas por vírgula (ex: 1,2) do restaurante: ")
    x, y = map(int, restaurante.split(","))
    pontos = {"100": (x,y)}
    quant_pontos = int(input("Quantidade de Pontos de entrega: "))

    for i in range(quant_pontos):
        entrada = str(input(f"Digite as coordenadas x, y separadas por vírgula (ex: 1,2) do ponto de entrega {i+1}: "))
        x, y = map(int, entrada.split(","))
        pontos[f"{i+1}"] = (x,y)

    permutacoes = permutacao([""+str(c+1) for c in range(quant_pontos)])


    return melhor_caminho(pontos, permutacoes)




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


def distancia_Manhattan(ponto1: Tuple[str], ponto2: Tuple[str]):
    distancia = 0
    if ponto1[0] >= ponto2[0]:
        distancia += ponto1[0] - ponto2[0]

    else:
        distancia += ponto2[0] - ponto1[0]

    if ponto1[1] >= ponto2[1]:
        distancia += ponto1[1] - ponto2[1]

    else:
        distancia += ponto2[1] - ponto1[1]

    return distancia

def melhor_caminho(pontos: Dict[str:Tuple[str]], lista: List[str]):
    total = float("inf")
    resp = ""
    for caminho in lista:
        percurso_atual = 0
        for c in range(len(caminho)):

            if c == 0:
                percurso_atual  += distancia_Manhattan(pontos["100"], pontos[caminho[0]]) # Restaurante -> 1 ponto
                percurso_atual += distancia_Manhattan(pontos[caminho[c]], pontos[caminho[c + 1]]) # 1 ponto ate o 2

            elif c == len(caminho)-1:
                percurso_atual  += distancia_Manhattan(pontos["100"], pontos[caminho[-1]]) # Último ponto -> restaurante

            else:
                percurso_atual  += distancia_Manhattan(pontos[caminho[c]], pontos[caminho[c+1]]) # De um ponto ate o próximo


        if percurso_atual < total:
            total = percurso_atual
            resp = " ".join(caminho)

    return resp


if __name__ == "__main__":
    print(TSP_forca_bruta())