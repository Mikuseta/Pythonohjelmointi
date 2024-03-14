pa = 0

# PALAUTE: tässä olisi hyvä käyttää math.pitä
while True:
    sade = float(input("Anna säde: "))
    pa = sade**2*3.14
    print("Keskipisteen pinta-ala on: ", (round(pa, 2)))
    jatko = input("Haluatko jatkaa? (k/e)")
    if jatko == "e":
        break