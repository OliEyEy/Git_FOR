#Ólafur Eysteinn - Æfingarverkefni 7 - 18. Október 2016
import random

#Liður 1
print("Liður 1")

tala= random.randint(1,6)
print(tala)

#Liður 2
print("Liður 2")

summa=0
for x in range(5):
    tala=random.randint(1,6)
    print(tala)
    summa=summa+tala
print(summa)

#Liður 3
print("Liður 3")

summa=0
summa2=0
for x in range(25):
    tala=random.randint(1,100)
    summa=summa+tala
    if tala%2!=0:
        print("Hei ég fann oddatölu.",tala)
        summa2=summa2+tala
    else:
        print(tala)
print("Summa allra oddatalnanna",summa2)
print("Summa allra talnanna",summa)

#Liður 4 (eða 5)
print("Liður 4 (eða 5)")
teljari=0
tala2=99
for x in range(250):
    tala=random.randint(25,115)
    print(tala)
    if tala==73:
        print("Fékk 73")
        break
    if tala==99:
        tala2=99
        teljari=teljari+1
print(tala2,"kom upp",teljari,"sinnum.")


#Skæri, Blað, Steinn

nafn = input("Hvað heitiru?")
aldur = int(input("Hvað ertu gamall/gömul?"))
on=1
hveOft=0
sigur = 0
tap = 0
jafntefli = 0
while on==1:
    hveOft=hveOft+1
    print("Skæri, blað, steinn")

    valmynd=int(input("Vilt þú gera 1 = skæri, 2 = blað, 3 = steinn eða 4 = Hætta ?"))

    if valmynd==1:
        tala=random.randint(1,3)
        if tala == 1:
            print("Forritið valdi skæri. Jafntefli!")
            jafntefli = jafntefli + 1
        elif tala == 2:
            print("Forritið valdi blað. Þú vannst!")
            sigur = sigur + 1
        elif tala == 3:
            print("Forritið valdi stein. Þú tapaðir!")
            tap = tap + 1
    elif valmynd==2:
        if tala == 1:
            print("Forritið valdi skæri. Þú tapaðir!")
            tap = tap + 1
        elif tala == 2:
            print("Forritið valdi blað. Jafntefli!")
            jafntefli = jafntefli + 1
        elif tala == 3:
            print("Forritið valdi stein. Þú vannst!")
            sigur = sigur + 1
    elif valmynd==3:
        if tala == 1:
            print("Forritið valdi skæri. Þú vannst!")
            sigur = sigur + 1
        elif tala == 2:
            print("Forritið valdi blað. Þú tapaðir!")
            tap = tap + 1
        elif tala == 3:
            print("Forritið valdi stein. Jafntefli!")
            jafntefli = jafntefli + 1
    elif valmynd==4:
        print("Þú vannst",sigur,"sinnum.")
        print("Þú tapaðir",tap,"sinnum.")
        print("Það var jafntefli",jafntefli,"sinnum.")
        print("Þú spilaðir",hveOft,"sinnum.")
        print("Þú heitir",nafn,"og ert",aldur,"ára gamall.")
        on=0

print("Takk fyrir að spila.")






























