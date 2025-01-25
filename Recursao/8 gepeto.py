def gols_sucessoes(m, n, sequencia=""):
    # Caso base: Se uma das equipes não tem mais gols restantes, imprimimos o restante dos gols
    if m == 0:
        print(sequencia + "B" * n)
        return
    elif n == 0:
        print(sequencia + "A" * m)
        return

    # Chamada recursiva: Adiciona um gol de A e um gol de B em cada chamada
    gols_sucessoes(m - 1, n, sequencia + "A")
    gols_sucessoes(m, n - 1, sequencia + "B")


# Exemplo de uso para um placar de 2 x 2
gols_sucessoes(2, 2)