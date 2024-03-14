# PALAUTE: hyvä, tämähän toimii oikein kokonaisluvuilla
# mutta itse tekisin useamapaa returnia varten
# yhden muuttujan, jonka arvoa vaihdan vuoden modulon mukaan ja palauttaisin (return) muuttujan vasta lopussa
# näin koodin kulkua on ehkä hieman helpompi seurata
# toki tämä ei ole pakollista, mutta suotavaa


def karkausvuosi(vuosi):
    if vuosi % 400 == 0:
        return True
    elif vuosi % 4 == 0:
        if vuosi % 100 != 0:
            return True
        else:
            return False


# miksi teet vuosiluvusta liukuluvun?
vuosi = float(input("Anna vuosiluku: \n"))
if (karkausvuosi(vuosi)):
    print("Karkausvuosi: KYLLÄ")
else:
    print("Karkausvuosi: EI")