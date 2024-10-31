"""Torneio de tênis"""


cont = 1
vitorias = 0
while cont < 7:
    r = str(input(f"Digite o resultado da {cont} partida ( V para venceu e P para perdeu ): ")).upper()
    if r == "V" or r == "P":
        cont += 1
        if r == "V":
            vitorias += 1
        r = ""

if vitorias >= 5:
    print(1)
elif vitorias >= 3:
    print(2)
elif vitorias >=1:
    print(3)
else:
    print(-1)

