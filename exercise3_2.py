
# PALAUTE: TÄMÄ EI OTA RANGEN YLÄPÄÄN LUKUJA HUOMIOON
# HUOM! RANGEA KÄYTETÄÄN YLEENSÄ TOISTOLAUSEIDEN EHDOISSA, JOTEN YLÄPÄÄ ON EKSLUSIIVINEN
# JOS LAITAT LÄMPÖTILAKSI 10, SOVELLUS EI TULOSTA MITÄÄN

# TOKI VAIKKA RANGE TOIMII TÄSSÄ TAPAUKSESSA IHAN HYVIN PYTHONILLA, SUOSITTELEN KÄYTTÄÄMÄÄN RANGEN SIJASTA

# if saa >= 10 and .... koska tämä toimii samalla logiikalla useammalla ohjelmointikielellä

# KANNATTAA MUUTTAA MUUTTUJA INTEGERIKSI VAIN KERRAN YLHÄÄLLÄ


saa = input("Syötä päivän lämpötila: ")
if int(saa) in range(0, 10): #luodaan ehtolause, jossa tarkistetaan että onko käyttäjän syöttämä luku 0 ja 10 välissä, ja mikäli ehto toteutuu tulostetaan lämpötila sanallisesti
    print("KYLMÄÄ")
elif int(saa) in range(11, 15): #toistetaan tarkistus mutta seuraavalla lämpöasteikolla
    print("KOLEAA")
elif int(saa) in range(16, 20): #toistetaan tarkistus mutta seuraavalla lämpöasteikolla
    print("NORMAALI LÄMPÖTILA")
elif int(saa) in range(21, 25): #toistetaan tarkistus mutta seuraavalla lämpöasteikolla
    print("LÄMMINTÄ")
elif int(saa) in range(26, 30): #toistetaan tarkistus mutta seuraavalla lämpöasteikolla
    print("HELLETTÄ")