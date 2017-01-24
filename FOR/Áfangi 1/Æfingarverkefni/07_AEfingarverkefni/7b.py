# Æfingarverkefni 7b

on="on"
while on=="on":
    print("Veldu þér lið hér")
    print("1. Summa - 2. Talnabil UppNiður - 3. Oddatölur ÁkveðiðBil - 4. La La La - 5.Margföldunartöflur 1-10 - 6.Línur og Dálkar - 7. Hætta.")
    valmynd=int(input("1, 2, 3, 4, 5, 6, eða 7 "))
# Liður 1
    if valmynd==1:
        print("Liður 1 ")

        print("Sláðu inn tvær tölur.")
        tala1 = int(input("Tala 1. "))
        tala2 = int(input("Tala 2. "))
        tala2=tala2+1
        summa = 0
        for x in range(tala1, tala2):
            summa = summa + x
        print(summa)
    elif valmynd==2:
        print("Liður 2")

        print("Sláðu inn tvær tölur.")
        tala1 = int(input("Tala 1. "))
        tala2 = int(input("Tala 2. "))
        if tala1==tala2:
            print("Ekkert bil er á milli.")
        elif tala1<tala2:
            tala2=tala2+1
            for x in range(tala1,tala2):
                print(x)
        elif tala2<tala1:
            tala2=tala2-1
            for x in range(tala1,tala2,-1):
                print(x)
        else:
            print("Villa.")
    elif valmynd==3:
        print("Liður 3")

        print("Sláðu inn tvær tölur.")
        tala1 = int(input("Tala 1. "))
        tala2 = int(input("Tala 2. "))
        if tala1<tala2:
            tala2 = tala2 + 1
            for x in range(tala1,tala2):
                if x%2!=0:
                    print(x)
        elif tala1>tala2:
            tala2=tala2-1
            for x in range(tala1, tala2,-1):
                if x % 2 != 0:
                    print(x)
    elif valmynd==4:
        print("Liður 4")

        la="la"
        svar=int(input("Hversu oft á ég að syngja La?"))
        svar=svar-1
        for x in range(svar):
            la=(la+"_la")
        print(la)
    elif valmynd==5:
        print("Liður 5")

        for x in range(1,11,):
            print("Næsta tafla.")
            for i in range(1,11,):
                tala=x*i
                print(tala)
    elif valmynd==6:
        for x in range(1,16):
            print(x,x*2,x*3)
    elif valmynd==7:
        on="off"
print("Takk fyrir og komdu aftur.")