#Skilaverkefni 4 - Ólafur Eysteinn - 13. Október

svar="Já"
while svar=="Já":
    print("1. Slærð inn tölu og segir hversu oft ég á að skrifa út töluna.")
    print("2. Slærð inn ártal og ég segi þér hvort það sé hlaupaár eða ekki.")
    print("3. Slærð inn tölu og ég margfalda saman rununa. T.d. ef þú slærð töluna 4 inn þá kemur 4 * 3 * 2 * 1")
    print("4. Slærð inn tölu og ég bý til rétthyrndan þríhyrning úr stjörnum með jafnmargar línur af stjörnum og þú slóst inn.")
    print("5. Enda forritið.")
    valmynd=int(input("Sláðu inn 1, 2, 3, 4 eða 5."))
#Liður 1
#Fæ notenda til þess að slá inn tölu og hversu oft ég á að skrifa töluna á skjáinn og skrifa svo töluna eins oft og hann vill á skjáinn.
    if valmynd==1:
        tala = int(input("Sláðu inn tölu."))
        hveOft=int(input("Hve oft á ég að skrifa töluna"))
        for x in range(hveOft):
            print(tala)
#liður 2
#Fæ notenda til þess að skrifa inn ártal og segja honum svo hvort það sé hlaupaár eða ekki. (Ps. Ekki eins einfalt og það hljómar.)
    elif valmynd==2:
        print("Viltu skrifa inn ártal?")
        svar2 = input("Já eða nei.")
        while svar2=="Já" or svar2=="já":
            arTal= int(input("Sláðu inn ártal."))
            hlaupAr=0
            if arTal%4 == 0:
                hlaupAr=1
                if arTal>400 and arTal%400!=0:
                    hlaupAr=0
            if hlaupAr==1:
                print("Þetta er hlaupaár.")
            else:
                print("Þetta er ekki hlaupaár")

            print("Viltu skrifa inn ártal?")
            svar2 = input("Já eða nei.")
#Liður 3
#Fæ notenda til þess að slá inn tölu og margfalda töluna svo með næstu tölu undir aftur og aftur þangað til að talan er 1.
    elif valmynd==3:
        tala=int(input("Sláðu inn heiltölu."))
        summa=1
        for x in range(tala,0,-1):
            summa=summa*x
        print(summa)

#Liður 4
#Fæ notenda til þess að slá inn tölu á bilinu 1-9 og bý síðan til rétthyrndan þríhyrning með 1 stjörnu í fyrstu línu, tveimur í næstur
# o.s.fv. þangað til að ég er kominn upp að tölunni sem hann valdi.
    elif valmynd==4:
        stjarna="*"
        hveOft=int(input("Sláðu inn hve margar línur stjörnurétthyrningurinn á að vera. Mega bara vera 1-9"))
        if hveOft>=1 and hveOft<=9:
            for x in range(hveOft):
                print(stjarna)
                stjarna=stjarna+"*"
        else:
            print("Þú hefur ekki slegið inn tölu á bilinu 1-9.")

    elif valmynd==5:
        print("Takk fyrir mig")
        svar="Nei"