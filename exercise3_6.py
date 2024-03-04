def karkausvuosi(vuosi):
    if vuosi % 400 == 0:
        return True
    elif vuosi % 4 == 0:
        if vuosi % 100 != 0:
            return True
        else:
            return False

vuosi = float(input("Anna vuosiluku: \n"))
if (karkausvuosi(vuosi)):
    print("Karkausvuosi: KYLLÄ")
else:
    print("Karkausvuosi: EI")