tyypi = input("Anna lähetyksen tyyppi: (Kirje tai Paketti) \n")
paino = float(input("Anna lähetyksen paino: (g) \n"))
#Luodaan hintamuuttujat kirjeille ja paketteille
kirjeperus = 0.5
pakettiperus = 2
kirjepieni = round(paino / 100) * 0.04
kirjesuuri = round(paino / 100) * 0.07
pakettipieni = round(paino / 100) * 0.08
pakettisuuri = round(paino / 100) * 0.14

if tyypi == "Kirje":
    if paino < 200:
        print("Lähetyskulut ovat ", kirjeperus, "€")
    elif paino >= 200 and paino < 500:
        print("Lähetyskulut ovat ", kirjeperus+kirjepieni, "€")
    elif paino > 500:
        luukku = input("Mahtuuko kirje postilaatikkoon? (K/E)")
        if luukku == "E":
            print("Lähetyskulut ovat ", kirjeperus+kirjesuuri+2, "€")
        else: print("Lähetyskulut ovat ", kirjeperus+kirjesuuri, "€")
        
if tyypi == "Paketti":
    if paino < 200:
        print("Lähetyskulut ovat ", pakettiperus, "€")
    elif paino >= 200 and paino < 500:
        print("Lähetyskulut ovat ", pakettiperus+pakettipieni, "€")
    elif paino > 500:
        print("Lähetyskulut ovat ", pakettiperus+pakettisuuri, "€")