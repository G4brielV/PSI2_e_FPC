# 1) Considere a função Comb(n, k), que representa o número de grupos distintos com k pessoas que podem ser formados a partir de n pessoas.
# Por exemplo, Comb(4, 3) = 4, pois com 4 pessoas (A, B, C, D), é possível formar 4 diferentes grupos: ABC, ABD, ACD e BCD.

#Implemente uma função recursiva para Comb (n, k) e mostre o diagrama de execução para chamada Comb (5, 3).
# Sabendo-se ainda Comb (n, k) = n! / (k! (n-k)!), implemente uma função não recursiva de Comb (n, k).



def Comb_Recursivo(quant_pess, num_pess_for_groups):
    if num_pess_for_groups == 1:
        return quant_pess
    elif num_pess_for_groups == quant_pess:
        return 1

    return Comb_Recursivo(quant_pess - 1, num_pess_for_groups - 1) + Comb_Recursivo(quant_pess - 1, num_pess_for_groups)


def Comb(quant_pess, num_pess_for_groups):

    difereca = quant_pess - num_pess_for_groups

    for i in range(quant_pess-1,0,-1):
        quant_pess *= i

        if i < num_pess_for_groups:
            num_pess_for_groups *= i

        if i < difereca:
            difereca *= i

    return quant_pess/ (num_pess_for_groups*difereca)




def main():
    print(Comb_Recursivo(4, 3))
    print(Comb(4,3))


if __name__ == "__main__":
    main()
