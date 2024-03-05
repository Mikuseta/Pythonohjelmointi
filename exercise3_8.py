import math
#luodaan muuttujat käyttäjän antamille tiedoille
summa = int(input("Anna ostosten kokonaissumma: \n"))
opiskelija = input("Oletko opiskelija? (K/E) \n")
kantis = input("Oletko kanta-asiakas? (K/E) \n")
hinta = summa
ale = input("Anna alennuskoodi \n")
#tarkistetaan mahdollinen alennuskoodi ja mikäli koodi on oikein, annetaan ostosten hinnasta alennus
if ale == "FALL23":
    hinta = summa*0.9
if ale == "BK2SCHOOL":
    hinta = summa*0.8
#luodaan kaavaa helpottamaan muuttujat postikuluille ja kanta-asiakaspisteille
kantispisteet = 0
posti = 7.95
#mikäli kanta-asiakkuuden valinta on kyllä, kysytään olemassa olevat pisteet
if kantis == "K":
    pisteet = int(input("Paljonko sinulla on kanta-asiakaspisteitä? \n"))
    kantispisteet = (hinta / 10) * 100 + pisteet #lisätään pisteet alkuperäiseen pistemäärään, mikäli sellainen on
    kantisale = math.floor(kantispisteet/1000) * 5 #lasketaan alennus pyöristämällä kanta-asiakaspisteet tuhannen tarkkuudella alas ja kerrotaan tulos 5:llä jolloin saadaan alennus
    hinta = hinta - kantisale
if hinta < 99: #tarkistetaan onko hinta alle 99€ ja mikäli on, lisätään postikulut
    hinta = hinta + posti
#tulostetaan tilauksen loppusumma
print("Tilauksen loppusumma =", hinta,"€") 