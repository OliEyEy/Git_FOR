# Æfingarverkefni 3    Ólafur Eysteinn Eysteinsson

#Liður 1
#Fá notenda til þess að slá inn t0lu á bilinu 1-20, segja honum hvort talan sé slétte eða ekki og draga tvo frá tölunni.
tala1 = int(input("Sláðu inn tölu á bilinu 1-20. "))
if tala1>=0 and tala1<=20:
    if tala1%2==0:
        print("Þetta er slétt tala.")
        print("Talan þín mínus 2 er "+str(tala1 - 2) + ".")
    else:
        print("Þetta er oddatala.")
        print("Talan þín margfölduð með 3 er "+str(tala1*3)+".")
else:
    print("Þú hefur slegið vitlausa tölu inn.")


#Liður 2
#Fá notenda til að slá inn hversu margir komu á spilakvöldið og segja honum
# hversu mörg fullskipuð borð það eru og hversu margir þurfa að fara.
gestir=int(input("Hversu margir eru mættir á spilakvöldið? "))
fjborda=int(gestir/4)
afgangs=gestir%4
print("Það eru þá "+str(fjborda)+" fullskipuð borð.")
print(str(afgangs)+" verða að fara heim.")

#Liður 3
#Fá notenda til þess að slá inn aldur sinn og segja honum hvort hann sé nógu gamall til þess að taka bílpróf eða kominn
# á eftirlaun, en ef hann er ekki nógu gamall segja honum hvesru mörg ár eru þangað til.
aldur=int(input("Hversu gamall/gömul ertu? "))
if aldur>=17:
    print("Ertu ekki örugglega búinn að taka bílpróf?")
    if aldur>=67:
        print("Og ert kominn á eftirlaun!")
else:
    print("Það eru "+str(17-aldur)+" ár þangað til að þú getur tekið bílpróf og "+str(67-aldur)+" ár þangað til að þú verður kominn á eftirlaun")

#Liður 4
tala_1=int(input("Sláðu inn tölu nr. 1 "))
tala_2=int(input("Sláðu inn tölu nr. 2 "))
tala_3=int(input("Sláðu inn tölu nr. 3 "))
if tala_1==tala_2==tala_3:
    print ("Allar tölur eru jafnstórar.")
else:
    if tala_1>=tala_2>=tala_3:
        print("Tala eitt er stærst.")
    elif tala_2>=tala_3>=tala_1:
        print("Tala tvö er stærst.")
    elif tala_3>=tala_1>=tala_2:
        print("Tala þrjú er stærst.")
       # if tala_1<=tala_2<=tala_3:
      #      print("Tala eitt er minnst.")
        #elif tala_2<=tala_3<=tala_1:
       #     print("Tala tvö er minnst.")
        #else:
       #     print("Tala þrjú er minnst.")
    else:
        print("Slegið vitlaust inn.")