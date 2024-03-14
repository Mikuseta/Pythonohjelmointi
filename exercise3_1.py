#PALAUTE: TÄMÄ OHJELMA KYLLÄ TEKEE VERTAILUN, MUTTA EI TOIMI NIIN KUIN PITÄISI

# TÄMÄ OHJLEMA VERTAA MERKKIJONOJA TOISIINSA: LUE LISÄÄ TÄÄLTÄ: https://www.digitalocean.com/community/tutorials/python-string-comparison

# JOS ANNAT EKAN ARVOKSI a ja TOISEN ARVOKSI B, ANTAA SOFTA TULOKSEKSI: Suurempi luku: a

eka = input("Anna ensimäinen luku: ")
toka = input("Anna toinen luku: ")

if eka > toka:  #tarkistetaan onko ensimäinen luku on suurempi
    print("Suurempi luku: ", eka)
elif toka > eka:    #tarkistetaan onko toinen luku suurempi
    print("Suurempi luku: ", toka)
else:
    print("Numerot ovat yhtä suuria.") #tarkistetaan ovatko numerot yhtä suuret