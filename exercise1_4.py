# PALAUTE: HYVÄ

minuutit = input("Anna minuutit: ")
tunti = int(minuutit)//60   #muutetaan annetut minuutit tunneiksi
minuutti = int(minuutit)%60 #tulostetaan loput minuutit minuutteina
print(tunti,"h", minuutti,"min")