import functions

hours = int(input("Anna tunnit: "))
minutes = int(input("Anna minuutit: "))
seconds = int(input("Anna sekunnit: "))

sekunnit = functions.count_seconds(hours, minutes, seconds) #kutsutaan funktiota lisäten siihen arvot user inputista

print("Yhteensä", sekunnit, "sekuntia")