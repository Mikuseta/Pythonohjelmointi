eka = input("Anna ensimäinen luku: ")
toka = input("Anna toinen luku: ")

if eka > toka:  #tarkistetaan onko ensimäinen luku on suurempi
    print("Suurempi luku: ", eka)
elif toka > eka:    #tarkistetaan onko toinen luku suurempi
    print("Suurempi luku: ", toka)
else:
    print("Numerot ovat yhtä suuria.") #tarkistetaan ovatko numerot yhtä suuret