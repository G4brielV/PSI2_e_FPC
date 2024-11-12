#2) Implemente recursivamente uma função Max que retorne o maior valor armazenado em um vetor V, contendo n números inteiros.
# Dada a implementação em pseudocódigo da função abaixo, quais são os valores de F(3) e de F(7)?

def max(lista):
    # Caso base:
    if len(lista) == 1:
        return lista[0]

    if lista[0] >= lista[-1]:
        lista.pop()
        return max(lista)

    else:
        return max(lista[1:])


def main():
    print(max([2,3,4,1]))

if __name__ == "__main__":
    main()
