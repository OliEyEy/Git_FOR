#Ólafur Eysteinn Eysteinsson - 6.Október - Æfingarverkefni 5

forritunarmal=["C","C++","Pearl","Python","Java"]
for x in forritunarmal:
    print(x)

matur=["Spagetti","Ís","Hamborgari","Fiskur","Subway"]
for x in matur:
    print(x)

#Verkefni 1 - Innslegið talnabil
tala1=int(input("Sláðu inn tölu."))
tala2=int(input("Sláðu inn aðra tölu"))
if tala1<tala2:
    if tala2-tala1==1:
        print(tala1,"er bara einum minni en",tala2)
    else:
        for x in range(tala1,tala2):
            print(x)
elif tala1>tala2:
    print("Fyrri talan (",tala1,") er stærri.")
elif tala1==tala2:
    print(tala1,"og",tala2,"eru  jafnstór.")
else:
    print("Villa.")

#Verkefni 2 - Oddatölur 1-99
for x in range(1,100):
    if x % 2 != 0:
        print(x)
#Verkefni 3 - Summa 1-15
for x in range(1,15):
    summa=0
    summa=summa+x
    print(x)
print("Summa talnanna er",summa)