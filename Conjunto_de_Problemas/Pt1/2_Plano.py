"""Plano de Internet"""

v = int(input("Valor da cota mensal: "))
n = int(input("Numero de meses: "))
gastos = [int(input(f"Megabytes gastos no {c} mês: ")) for c in range(1, n+1)]

total = 0

for mes in gastos:
    total = (v+total) - mes

print(f"Ele tem {total+v} de Megabytes para o {n+1} mês")