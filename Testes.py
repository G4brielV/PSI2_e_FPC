lista = [1,2,3]
print(lista[1:])
print(lista[0:-1])

a = 102
print(int(a/10))


b = "1,9"
b1, b2 = b.split(",")

print(b1, b2)

v = []
l = [c.split() for c in input("Digita: ")]
v.append(l)
print(v)