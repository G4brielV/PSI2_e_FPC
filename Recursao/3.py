def raiz_quadrada(x,aproX, erro):
    if 0 < aproX**2 - x <= erro:
        return aproX

    else:
        aproX = (aproX**2 + x)/(2*aproX)
        return raiz_quadrada(x,aproX,erro)



print(raiz_quadrada(13,3.2,0.001))