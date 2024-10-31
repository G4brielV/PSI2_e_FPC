"""Idade de Camila"""

# Cibele < Camila < Celeste

lista = []

a = int(input("Digite a 1 idade: "))
lista.append(a)


b = int(input("Digite a 2 idade: "))
if b > lista[0]:
    lista.append(b)
else:
    lista.insert(0,b)


c = int(input("Digite a 3 idade: "))
if c > lista[1]:
    lista.append(c)
elif c > lista[0]:
    lista.insert(1,c)
else:
    lista.insert(0,c)

print(f"A idade de Camila é: {lista[1]}")

