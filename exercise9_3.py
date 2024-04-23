import functions

serial = str(input("Anna ISSN: "))
# palaute: tämä näyttää laskevan väärin
if functions.magazine_serial_check(serial):
    print("Oikea ISSN.")
else:
    print("Väärä ISSN.")