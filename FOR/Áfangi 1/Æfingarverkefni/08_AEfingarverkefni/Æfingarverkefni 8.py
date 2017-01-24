#Ólafur Eysteinn - Æfingarverkefni 8 - 27. Október 2016

import random
on="on"
while on=="on":
    print("Veldu verkefni.")
    valmynd=int(input("1. Innkaupalisti 2. Random tölur 3. Fyrsta og síðasta 4. Nemendur 5. Hætta "))
#Liður 1
    if valmynd==1:
        print("Liður 1")
        svar="j"
        innkaupalisti=[]
        while svar=="j":
            innkaupalisti.append(input("Hvað viltu á innkaupalistann?"))
            svar=input("Viltu bæta einhverju öðru á listann? j fyrir Já")
        innkaupalisti.sort()
        print(innkaupalisti)
#Liður 2
    if valmynd==2:
        print("Liður 2")
        tolur=[]
        summa=0
        for x in range(15):
            tolur.append(random.randint(5,25))
            summa=summa+tolur[x]
        tolur.sort()
        print("Listinn =",tolur)
        print("Hæsta talan er",max(tolur))
        print("Minnsta talan er",min(tolur))
        print("Summa talnanna er",summa)
        print("Listinn er með",len(tolur),"tölur")
#Liður 3
    if valmynd==3:
        print("Liður 3")
        tolur=[]
        for x in range(20):
            tolur.append(random.randint(1,20))
        print("Listi númer 1",tolur)
        tolur2=[(tolur[0]),(tolur[19])]
        print("Listi númer 2",tolur2)
#Liður 4
    if valmynd==4:
        nemendalisti=[]
        print("Liður 4")
        for x in range(10):
            nafn=input("Sláðu inn nafn. ")
            if nafn not in nemendalisti:
                nemendalisti.append(nafn)
            else:
                print("Bannað að slá inn sama nafn tvisvar.")
        nemendalisti.reverse()
        print(nemendalisti)



    if valmynd==5:
        print("Takk fyrir.")
        on="off"