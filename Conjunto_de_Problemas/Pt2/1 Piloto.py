"""Piloto Automático"""
def piloto_automatico(atras, voce, frente):
    if voce - atras < frente - voce:
        return 1
    elif voce - atras == frente - voce:
        return 0
    else:
        return -1




a = 80
b = 120
c = 132

print(piloto_automatico(a,b,c))