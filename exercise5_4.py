kaupungit = ['Rooma', 'Ateena', 'Tukholma', 'Lontoo', 'Dublin', 'Pariisi']
jarjestetty = sorted(kaupungit) #järjestetään kaupungit aakkosjärjestykseen

for (i, jarj) in enumerate(jarjestetty, start=1): #luodaan looppi jossa tulostetaan järjestetyt kaupungit
    print(i, jarj)