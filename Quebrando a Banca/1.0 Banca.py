from random import randint


def banca(quant, retirar, num):
    temqter = quant - retirar
    maior = []
    for n in str(num):
        # Verifica se ainda pode retirar algum numero
        # Verfica se ta vazio para fazer a outra comparação (evita o "list index out of range")
        # Verifica se é maior que o ultimo numero adicionado
        if retirar > 0 and maior != [] and n > maior[-1]:

            # Verfica se pode retirar mais de um numero:
                # Caso ainda haja numeros para tirar
                # Caso o numero seja maior que os outros
            for c in range(0, len(maior) - 1):
                if retirar >= (len(maior) - c) and  n > maior[c]:
                    retirar -= len(maior)
                    maior = maior[:c]
                    break

            # Para retirada apenas do ultimo da lista e substitui-lo pelo maior
            else:
                maior.pop()
                retirar -= 1

        maior.append(str(n))

    # Pega apenas os maiores da lista, corrige casos de ordem decrescente como "5432"
    return "".join(maior[:temqter])


for _ in range(10):
    c = randint(1,100000)
    a = len(str(c))
    b = a - 3

    print(f"Numero: {c}")
    print(f"Maior possibilidade: {banca (a, b, c)}")


# Complexidade de :
