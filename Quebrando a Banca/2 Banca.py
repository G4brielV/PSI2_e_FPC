from random import randint


def banca(quant, retirar, num):
    temqter = quant - retirar
    maior = []

    for n in str(num):
        # Enquanto houver removals disponíveis e o topo da pilha for menor que o dígito atual
        while retirar > 0 and maior and maior[-1] < n:
            maior.pop()
            retirar -= 1
        maior.append(n)

    # Pega apenas os primeiros 'temqter' dígitos para o resultado final
    return "".join(maior[:temqter])


for _ in range(10):
    c = randint(1,100000)
    a = len(str(c))
    b = a - 2

    print(f"Numero: {c}")
    print(f"Maior possibilidade: {banca(a,b,c)}")