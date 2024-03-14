
# PALAUTE: SUOSITTELEN OPETTELEMAAN SELKEÄN NIMEÄMISKÄYTÄNNÖN HETI ALUSTA LÄHTIEN,
# JOTTA SE TULEE MYÖHEMMIN SELKÄRANGASTA
# TÄMÄ SOFTA ON TOKI NIIN PIENI, ETTÄ MUUTTUJIEN ARVOT SELVIÄVÄT HELPOSTI
# MUTTA JOS TEET MUUTTUJAN NIMELTÄ 'kuudes', JOTA KÄYTÄT 200 RIVIÄ ALEMPANA, ET TIEDÄ, MITÄ MUUTTUJAN ON TARKOITUS TEHDÄ

# LISÄKSI: sentit KANNATTAA MUUTTAA INTEGERIKSI KERRAN JA KÄYTTÄÄ SITÄ LOPUISSA LASKUTOIMITUKSISSA
# TÄSSÄ ON MELKO MONTA YLIMÄÄRÄISTÄ TYYPPIMUUNNOSTA

sentit = input("Anna 1-100 senttiä: ") #otetaan käyttäjä antamat sentit
eka = int(sentit)//50   #muutetaan annetut sentit kolikoiden määräksi
tase = int(sentit)%50   #muodostetaan muuttuja joka ottaa huomioon aikaisemmin otetut senttimäärät käyttäjän antamasta määrästä ja jatketaan samalla tavalla kunnes määrä on jaettu kokonaisuudessaan kolikoiksi
toka = int(tase)//20
tase = int(tase)%20
kolmas = int(tase)//10
tase = int(tase)%10
neljas = int(tase)//5
tase = int(tase)%5
viides = int(tase)//2
tase = int(tase)%2
kuudes = int(tase)//1
print("50 snt kolikoita", eka, "kpl"), print("20 snt kolikoita", toka, "kpl"), print("10 snt kolikoita", kolmas, "kpl"), print("5 snt kolikoita", neljas, "kpl"), print("2 snt kolikoita", viides, "kpl"), print("1 snt kolikoita", kuudes, "kpl")