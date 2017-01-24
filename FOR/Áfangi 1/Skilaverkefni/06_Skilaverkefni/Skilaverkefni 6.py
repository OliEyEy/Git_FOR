#Skilaverkefni 6 - Ólafur Eysteinn - 10. Nóvember 2016

on="on"
while on=="on":
    print("1. Kennitala - 2. Búa til nýtt orð - 3. Sneið af streng - 4. Hætta")
    valmynd=int(input("Veldu lið. "))
    if valmynd==1:
        #Liður 1
        #Fá notenda til þess að slá inn kennitölu og staðfesti að kennitalan sé gild.
        print("Liður 1")
        ja=1
        while ja==1:
            kennitala=input("Sláðu inn kennitölu. ")
            dagur=kennitala[:2]
            manudur=kennitala[2:4]
            ar=kennitala[4:6]
            if len(kennitala)==10:
                if int(dagur) <= 31:
                     if int(manudur)<=12:
                        if int(ar)>=26 or int(ar)<=16:
                            print("Vel gert! Þú slóst inn rétta kennitölu.", kennitala)
                            ja = 0
                        else:
                            print("Talan 5-6 getur ekki verið minna en 26 og meira en 16")
                     else:
                        print("Talan 3-4 geta ekki verið meira enn 12.")
                else:
                    print("Fyrstu 2 tölurnar geta ekki verið meira enn 31.")
            else:
                print("Kennitölur eiga að vera með 10 tölustafi.")
    if valmynd==2:
        #Liður 2
        #Fæ notenda til þess að slá inn orð sem er amk 5 stafir og bý til nýtt orð úr fyrstu 2 stöfunum
        # og seinustu 2 stöfunum úr orðinu. Skrifa svo út nýja orðið í há- og lástöfum.
        print("Liður 2")
        ja=1
        while ja==1:
            ord=input("Sláðu inn orð sem er amk 5 stafir. ")
            if len(ord)>4:
                ord2=ord[:2]+ord[-2:]
                print(ord2)
                print(ord2.upper())
                print(ord2.lower())
                ja=0
            else:
                print("Verður að vera amk 5 stafir.")
    if valmynd==3:
        #Liður 3
        #Fæ notenda til þess að slá inn nafn og birti nafnið aftur og aftur og í hvert skipti tek ég fyrsta stafinn úr
        # nafninu þangað til að það er bara einn stafur eftir.
        print("Liður 3")
        nafn=input("Sláðu inn nafn. ")
        for staf in nafn:
            print(nafn)
            nafn=nafn[1:]
    if valmynd==4:
        on="off"