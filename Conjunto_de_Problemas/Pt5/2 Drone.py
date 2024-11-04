def drone(a,b,c,h,l):
    caixa = [a,b,c]
    janela = []
    # Ordaenando as dimensões da janela
    if h < l:
        janela = [h,l]
    else:
        janela = [l,h]

    # Ordenando as dimensões da caixa
    for i in range(len(caixa)-1):
        if caixa[i] <= caixa[i+1]:
            pass

        else:
            cont = 0
            while i-cont >= 0 and caixa[i+1-cont] < caixa[i-cont]:
                caixa[i-cont], caixa[i+1-cont] = caixa[i+1-cont], caixa[i-cont]
                cont += 1

    if janela[0] >= caixa[0] and janela[1] >= caixa[1]:
        return "S"

    else:
        return "N"


print(drone(30,50,80,80,60))
print(drone(75,100,50,100,30))
print(drone(20,22,5,20,10))
