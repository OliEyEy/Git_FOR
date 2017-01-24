#Ólafur Eysteinn - 2001002980 - 19. Janúar 2017
import random

on=1
while on==1:
    print(" ")
    print("1. Listi fyrir tölur")
    print("2. Random tölur")
    print("3. Strengjalisti")
    print("4. Fjöldi teningakasta ákveðinn af notenda")
    print("5. Skráning í áfanga")
    valmynd=int(input("Sláðu inn 1. 2. 3. 4. eða 5. "))

    if valmynd==1:
        talnalisti=[]
        hveOftListi=[]
        summa=0
        hveOft=0
        for x in range(7):
            tala=float(input("Sláðu inn tölu. "))
            talnalisti.append(tala)
            summa=summa+tala
            if tala<=50.5:
                hveOftListi.append(tala)
                hveOft=hveOft+1
        medaltal=summa/7
        print("Hæsta talan er:",max(talnalisti))
        print("Læsta talan er:",min(talnalisti))
        print("Meðaltala talnanna er:",round(medaltal,2))
        print("Summa talnanna er:",summa)
        talnalisti.sort()
        print("Hér er talnalistinn frá læstu tölu til hæstu:")
        for talan in talnalisti:
            print(round(talan,9), end=" ; ")
        print(" ")
        print("Það komu",hveOft,"sinnum tölur sem voru undir eða jafnar 50,5:")
        print("Það voru þessar tölur:",hveOftListi)

    if valmynd==2:
        randomtolur=[]
        hveOft1=0
        hveOft2=0
        print("Hér eru allar 'random' tölurnar:")
        for x in range(70):
            randomtala=random.randint(1,500)
            randomtolur.append(randomtala)
            if randomtala<=250:
                hveOft1=hveOft1+1
            elif randomtala>=251:
                hveOft2=hveOft2+1
        for x in range(0,len(randomtolur),4):
            print(randomtolur[x:x+4])
        print("Hæsta 'random' talan er",max(randomtolur))
        print("Læsta 'random' talan er",min(randomtolur))
        randomtolur.reverse()
        for x in range(0,len(randomtolur),6):
            print(randomtolur[x:x+6])
        print("Það voru",hveOft1,"tölur á bilinu 1-250.")
        print("Það voru",hveOft2,"tölur á bilinu 251-500.")

    if valmynd==3:
        nafnalisti=[]
        for x in range(5):
            nafn=input("Sláðu inn nafn. ")
            nafnalisti.append(nafn)
        off=0
        nafnalisti2=nafnalisti
        while off==0:
            print(" ")
            print("1. Birta nöfnin óraðað")
            print("2. Raða nöfnunum í stafrófsröð og birta")
            print("3. Raða nöfnunum í öfuga stafrófsröð og birta")
            print("4. Birta eitt nafn eftir því hvaða númer (1-5) var valið")
            print("5. Hætta í verkefni 3")
            valmynd=int(input("1. 2. 3. 4. eða 5. "))
            print(" ")
            if valmynd==1:
                print("Óraðaður nafnalisti:",nafnalisti)
            if valmynd==2:
                nafnalisti2.sort()
                print(nafnalisti2)
            if valmynd==3:
                nafnalisti2.sort()
                nafnalisti2.reverse()
                print(nafnalisti2)
            if valmynd==4:
                nafn=int(input("Númer hvaða nafn viltu sjá? "))
                for x in nafnalisti:
                    if x==nafn:
                        print(x)