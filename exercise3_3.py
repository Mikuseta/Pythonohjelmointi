tunnit = float(input("Syötä viikon työtunnit: "))
palkka = float(input("Syötä tuntipalkkasi: "))

if float(tunnit) > 40:
    ylityo = (tunnit-40)*1.5*palkka
    tulot = (40*palkka)
    raha = tulot + ylityo
else:
    raha = (tunnit*palkka)
    ylityo = 0

print("Viikon ansiosi ovat: ", raha)