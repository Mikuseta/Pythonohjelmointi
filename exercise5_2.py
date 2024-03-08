sade = 0 #määritellään tyhjä muuttuja käytettäväksi loopin sisällä

for i in range(12): #kuukausien määrä
    maara = int(input("Anna kuukauden sademäärä: "))
    sade = sade + maara #lasketaan yhteen sademäärä kuukausilta käyttämällä aiemmin luotua muuttujaa
    keskiarvo = sade / 12 #lasketaan keskiarvo

print("Vuoden keskiarvo on noin",keskiarvo,"mm")