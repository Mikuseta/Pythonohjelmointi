# PALAUTE: HIENOA

raha = int(input("Anna rahaa: \n")) #pyydetään annettu raha
ostokset = int(input("Ostosten hinta: \n")) #pyydetään ostosten summa

if raha > ostokset:
    tulos = raha - ostokset #lasketaan takaisin annettava summa
    print("Kiitos. Annetaan takaisin", tulos, "€")
   
else:
    lisaa = float(input("Rahat eivät riitä, anna lisää rahaa: \n"))
    tulos = raha + lisaa - ostokset #lasketaan takaisin annettava summa mikäli rahamäärä ylittää ostosten summan
    if raha + lisaa > ostokset:
        print("Kiitos. Annetaan takaisin", tulos, "€")
    else:
        print("Sinulla ei ole tarpeeksi rahaa")
