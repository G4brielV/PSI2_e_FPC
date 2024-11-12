def batalha_naval(linhas, colunas, navios, disparos):
    for disparo in disparos:
        linha, coluna = disparo.split(",")
        linha = int(linha)
        coluna = int(coluna)

        if navios[linha-1][coluna-1][0] == "#": # Quebrou uma parte do navio
            navios[linha-1][coluna-1][0] = "X"






l = int(input("Numero de linhas: "))
c = int(input("Numero de colunas: "))
linhas = []
disparos = []
for c in range(1,l+1):
    linha = [c.split() for c in input(f"Digite '.' para água e '#' para parte de navio na linha {c}: ")]
    linhas.append(linha)

print(linhas[0][2])

k = int(input("Numeros de disparos: "))
for p in range(1,k+1):
    disparo = str(input(f"Digite a cordenada do {p}° disparo (x,y): "))
    disparos.append(disparo)


batalha_naval(5,5, linhas, disparos)