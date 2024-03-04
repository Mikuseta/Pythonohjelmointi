pisteet = float(input("Anna pisteet: \n"))

if pisteet >= 0 and pisteet <=50:
    print("Arvosana: 0")
elif pisteet >= 51 and pisteet <= 60:
    print("Arvosana: 1")
elif pisteet >= 61 and pisteet <= 70:
    print("Arvosana: 2")
elif pisteet >= 71 and pisteet <= 80:
    print("Arvosana: 3")
elif pisteet >= 81 and pisteet <= 90:
    print("Arvosana: 4")
elif pisteet >= 91 and pisteet <= 100:
    print("Arvosana: 5")
else:
    print("Pistemäärä ei ole mahdollinen")