def peca(quant, list):
    for c in range(1, quant+1):
        if c not in list:
            return c

        
a = int(input("Quant de peça: "))
b = [int(input("Digite o num: ")) for _ in range(a-1)]


resp = peca(a,b)

print(resp)