"""Entrega de Caixas"""
def entrega_de_caixas(x,y,z):
    if z > x+y or x<y<z:
        return 1
    elif x == y == z:
        return 3
    else:
        return 2


a = 5
b = 5
c = 8

print(entrega_de_caixas(a,b,c))