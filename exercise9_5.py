import functions

while True:
    numero = int(input("Anna laskutoimituksen numero: (1=laatikko, 2=pallo, 3=putki, 0=lopeta) "))

    if numero == 1: #luodaan muuttujat laatikolle
        leveys = int(input("Anna laatikon leveys: "))
        korkeus = int(input("Anna laatikon korkeus: "))
        syvyys = int(input("Anna laatikon syvyys: "))
        print("Laatikon tilavuus:", functions.box_volume(leveys, korkeus, syvyys),"m3") #kutsutaan funktiota annetuilla parametreillä

    elif numero == 2: #luodaan muuttuja pallalle
        sade = int(input("Anna pallon säde: "))
        print("Pallon tilavuus:", functions.ball_volume(sade),"m3") #kutsutaan funktiota annetuilla parametreillä

    elif numero == 3: #luodaan muuttujat putkelle
        sade = int(input("Anna putken säde: "))
        pituus = int(input("Anna putken pituus: "))
        print("Putkin tilavuus:", functions.pipe_volume(sade, pituus),"m3") #kutsutaan funktiota annetuilla parametreillä
    elif numero == 0: #jos numero on 0 niin lopetetaan looppi
        break
    else:
        print("Virheellinen syöte")