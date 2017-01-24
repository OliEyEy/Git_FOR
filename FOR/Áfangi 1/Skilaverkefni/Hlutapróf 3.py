#Hlutapróf 3 - Ólafur Eysteinn Eysteinsson - 22. Nóvember 2016

import random
kveikt=1
while kveikt==1:
    print("1. Skrifa út tölurnar 255-4000 í eina línu.")
    print("2. Vinna með tilviljanakenndar (random) tölur.")
    print("3. Vinna með texta (string).")
    print("4. Hætta.")
    valmynd=int(input("Veldu lið - 1. 2. 3. 3 eða 4. "))
    print(" ")

    if valmynd==1:
        #Liður 1
        #Læt forritið birta allar tölur á bilinu 255 til 4000 í einni línu.
        print("Liður 1")

        for x in range(255,4001):
            print(x, end=" ")
        print(" ")
        print(" ")

    if valmynd==2:
        #Liður 2
        #Læt forritið finna 200 random tölur á bilinu 190 til 999, setja þær í lista og gera eftirfarandi hluti. Birta
        # meðaltal talnanna með tveimur aukastöfum, finna og birta hve oft talan 200 er í listanum, finna allar tölur í
        # listanum sem eru hærri 200, leggja þær allar saman og birta summuna og að lokum finna allar tölur í listanum
        # lægri en 600 og birta þær.
        print("Liður 2")

        randomTolur=[]
        summa=0
        yfir200=0
        undir600=""
        hveOft=0
        for x in range(200):
            randomTala=random.randint(190,999)
            randomTolur.append(randomTala)
            summa=summa+randomTala
            if randomTala==200:
                hveOft=hveOft+1
            if randomTala>200:
                yfir200=yfir200+randomTala
            if randomTala<600:
                undir600=str(undir600)+" "+str(randomTala)
        medaltal=summa/200
        print("Meðaltal talnanna er:",round(medaltal,2))
        print("Talan 200 kom",hveOft,"sinnum upp.")
        print("Summa all talna sem voru yfir 200 er:",yfir200)
        print("Allar tölur sem voru lærri en 600 eru:"+undir600)
        print(" ")

    if valmynd==3:
        #Liður 3
        #Fæ notenda til þess að skrifa inn texta að eigin vali og læt forritið gera eftirfarandi hluti. Finna hversu
        # mörg orð eru í textanum, skrifa út textann nema allt í lágstöfum og að lokum skipta út öllum stöfum og táknum
        # í textanum fyrir (?) nema stafabilum og stafinum e, síðan birta textann.
        print("Liður 3")
        texti=input("Sláðu inn texta að eigin vali. ")
        hveMorgOrd=1
        for stafur in texti:
            if stafur==" ":
                hveMorgOrd=hveMorgOrd+1
        print("Það eru",hveMorgOrd,"orð í textanum.")
        print("Orðið í lágstöfum er:",texti.lower())
        for stafur in texti:
            if stafur != " " and stafur != "e":
                texti = texti.replace(stafur, "?")
        print("Hér er textinn með allt breytt í (?) nema (stafabil) og (e):",texti)
        print(" ")

    if valmynd==4:
        #Liður 4
        #Læt forritið enda.
        print("Liður 4")
        print("Takk fyrir mig ☺")
        kveikt=0