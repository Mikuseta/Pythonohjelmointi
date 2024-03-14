import functions

serial = str(input("Anna ISSN: "))

if functions.magazine_serial_check(serial):
    print("Oikea ISSN.")
else:
    print("Väärä ISSN.")