print("############ while")

# PALAUTE: a-kohdassa piti aloittaa 1:sta

laskin = 0
while laskin <= 50:
    print(laskin)
    laskin = laskin + 1


print("###############for")
for numero in range(1, 51):
    print(numero)

summa = 0
for arvo in range(1, 31):
    summa = summa + arvo
print("Summa:", summa)

for vuosi in range(2005, 2011):
    print(vuosi, end=" ")