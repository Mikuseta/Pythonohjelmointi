tunnit = float(input("Syötä viikon työtunnit: "))
palkka = float(input("Syötä tuntipalkkasi: "))

# PALAUTE: float-tyyppimuunnos on tässä ifissä turha, koska teet sen ylhäällä jo ennen ifiä

if float(tunnit) > 40:
    ylityo = (tunnit-40)*1.5*palkka
    tulot = (40*palkka)
    raha = tulot + ylityo
else:
    raha = (tunnit*palkka)
    # PALAUTE: ylityo-muuttuja on tässä turha, koska tunnit eivät ylity
    ylityo = 0

print("Viikon ansiosi ovat: ", raha)