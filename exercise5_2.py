sade = 0 #määritellään tyhjä muuttuja käytettäväksi loopin sisällä

# PALAUTE: tehtävässä annetaan vihe, että keskiarvo kannattaa laskea vasta luupin jälkeen pyöristysvirheiden välttämiseksi
# vaikka silmukka toimii teknisesti oikein, en anna tästä pisteitä

for i in range(12): #kuukausien määrä
    maara = int(input("Anna kuukauden sademäärä: "))
    sade = sade + maara #lasketaan yhteen sademäärä kuukausilta käyttämällä aiemmin luotua muuttujaa
    keskiarvo = sade / 12 #lasketaan keskiarvo

print("Vuoden keskiarvo on noin",keskiarvo,"mm")