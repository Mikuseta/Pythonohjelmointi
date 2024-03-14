import functions

maara = int(input("Anna rahasumma: "))
mista = input("Mistä valuutasta haluat vaihtaa?: (€, £, $, kr) ")
mihin = input("Miksi valuutaksi haluat vaihtaa?: (€, £, $, kr) ")
kurssit = {"€": 1.09, "£": 0.85, "$": 1.24, "kr": 11.24}

print(functions.convert_money(maara, mista, mihin, kurssit))