# Área retângular, com linhas e colunas
# Ovelha = k
# Lobo =   v
# Cerca =  #
# Vazio =  .

def lobomal(retangulo):
    ovelha = lobo = 0
    for e1, linha in enumerate(retangulo):
        for e2, elemento in enumerate(linha):
            if elemento in "kv":
                t = (0,0)
                t = arredores(retangulo,e1,e2, [])
                ovelha += t[0]
                lobo += t[1]

    return ovelha, lobo

def arredores(retangulo, e1, e2, lista =[]):
    lista.append(retangulo[e1][e2])
    retangulo[e1][e2] = "#"

    # primeira linha, ultima linha, primeira coluna, ultima coluna --> ovelhas fogem
    if e1 == 0 or e1 == len(retangulo)-1 or e2 == 0 or e2 == len(retangulo[0]) -1:
        return [lista.count("k"), lista.count("v")]

    # linha de cima
    if retangulo[e1-1][e2] not in "#":
        arredores(retangulo, e1 - 1, e2, lista)

    # linha de baixo
    if retangulo[e1+1][e2] not in "#":
        arredores(retangulo, e1+1, e2, lista)

    # direita
    if retangulo[e1][e2+1] not in "#":
        arredores(retangulo, e1, e2+1, lista)

    # esquerda
    if retangulo[e1][e2-1] not in "#":
        arredores(retangulo, e1, e2-1, lista)

    if lista.count("k") > lista.count("v"):
        return [lista.count("k"), 0]

    else:
        return [0, lista.count("v")]



# l = int(input("Numero de linhas: "))
# c = int(input("Numero de colunas: "))
# linhas = []
# for c in range(1,l+1):
#     linha = [c for c in input(f"Digite '.' para água e '#' para parte de navio na linha {c}: ")]
#     linhas.append(linha)



exemplo1 = [['.', '.', '.', '#', '.', '.'], ['.', '#', '#', 'v', '#', '.'], ['#', 'v', '.', '#', '.', '#'],
            ['#', '.', 'k', '#', '.', '#'], ['.', '#', '#', '#', '.', '#'], ['.', '.', '.', '#', '#', '#']]

exemplo2 = [['.', '#', '#', '#', '#', '#', '#', '.'], ['#', '.', '.', 'k', '.', '.', '.', '#'], ['#', '.', '#', '#', '#', '#', '.', '#'],
            ['#', '.', '#', 'v', '.', '#', '.', '#'], ['#', '.', '#', '.', 'k', '#', 'k', '#'], ['#', 'k', '.', '#', '#', '.', '.', '#'],
            ['#', '.', 'v', '.', '.', 'v', '.', '#'], ['.', '#', '#', '#', '#', '#', '#', '.']]

exemplo3 = [['.', '#', '#', '#', '.', '#', '#', '#', '#', '#', '.', '.'], ['#', '.', 'k', 'k', '#', '.', '.', '.', '#', 'v', '#', '.'],
            ['#', '.', '.', 'k', '#', '.', '#', '.', '#', '.', '#', '.'], ['#', '.', '.', '#', '#', 'k', '#', '.', '.', '.', '#', '.'],
            ['#', '.', '#', 'v', '#', 'k', '#', '#', '#', '.', '#', '.'], ['#', '.', '.', '#', 'v', '#', '.', '.', '.', '.', '#', '.'],
            ['#', '.', '.', '.', 'v', '#', 'v', '#', '#', '#', '#', '.'], ['.', '#', '#', '#', '#', '.', '#', 'v', 'v', '.', 'k', '#'],
            ['.', '.', '.', '.', '.', '.', '.', '#', '#', '#', '#', '#']]

print(lobomal(exemplo1))
print(lobomal(exemplo2))
print(lobomal(exemplo3))