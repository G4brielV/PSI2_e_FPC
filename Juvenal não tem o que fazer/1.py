# Juvenal estava sem ter o que fazer durante as férias e resolveu criar uma
# função, porém ele não sabe se ela sempre termina, já que é recursiva. A função é
# a seguinte:
# F(n) = {
# 1, se n = 1
# F(n/2), se n for par
# F(3*n+1), se n for ímpar
# }

# Juvenal definiu outra função:
# G(n) = quantas chamadas recursivas são necessárias para que F(n) atinja o caso
# base.
# Agora, dado dois inteiros A e B, Juvenal quer saber qual o maior valor que a
# função G assume quando n está no intervalo [A,B].


def F(n): # Termina
    if n == 1:
        return 1
    elif n%2 == 0:
        return F(n//2)
    else:
        return F(n*3+1)

def G(n):
    if n == 1:
        return 1
    elif n%2 == 0:
        return 1 + G(n//2)
    else:
        return 1 + G(3 * n + 1)


def main():
    lista = []
    i = int(input("Quantidade de casos: "))
    for _ in range(i):
        interv = int(input("Intervalo_1: "))
        interv2 = int(input("Intervalo_2: "))
        lista.append((interv, interv2))


    for e,tupla in enumerate(lista):
        maior = 0
        for c in range(tupla[0], tupla[1]+1):
            p = G(c)
            if p > maior:
                maior = p

        print(f"Caso {e+1}: {maior}")



if __name__ == "__main__":
    main()