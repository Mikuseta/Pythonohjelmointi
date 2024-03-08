def salaa_sana(sana): #luodaan funktio jossa salataan sana
    tulos = ""

    for i in range(len(sana)): 
        salaus = sana[i]

        if salaus == " ": #tarkistetaan onko sanassa välilyönti ja jos on niin lisätään salaukseenkin se
            tulos += " "
        elif (salaus.isupper()): #tarkistetaan onko kirjain iso ja jos on niin pidetään se salatussakin isona
            tulos += chr((ord(salaus) + 3 - 65) % 26 + 65)
        else: #jos kirjain ei ole iso niin pidetään se pienenä
            tulos += chr((ord(salaus) + 3 - 97) % 26 + 97)
    return tulos

sana = input("Anna salattava sana: ")

print(salaa_sana(sana)) #kutsutaan funktiota