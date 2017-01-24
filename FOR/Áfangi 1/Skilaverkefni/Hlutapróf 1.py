#Ólafur Eysteinn Eysteinsson - Hlutapróf 1

#DÆMI 1
#Fæ notenda til þess að slá in nafn sitt, skónúmer sitt, uppáhalds skóverslun sína og heilsa honum síðan með þessum upplýsingum.
nafn=input("Hvað heitiru? ")
skoNr=int(input("Hvaða skónúmer notaru? "))
skoVerslun=input("Í hvaða skóverslun verslaru oftast? ")
print("Góðan daginn",nafn,", þú notar skónúmer",skoNr,"og verslar oftast skó í skóbúðinni",skoVerslun,".")

#DÆMI 2
#Fæ notenda til að slá inn stigafjöldan í handbolta og svara honum síðan með viðeigandi svari.
stigaFj=int(input("Hver er stigafjöldinn? "))
if stigaFj>=17 and stigaFj<=35:
    print("Vel gert.")
elif stigaFj>=36:
    print("Voru þeir einir á vellinum?")
else:
    print("Það gengur betur næst.")

#DÆMI 3
#Fæ notenda til að slá inn þrjár mismunandi tölur, legg saman fyrstu tvær, dreg þriðju töluna frá summunni og segji notendanum svarið.
print("Sláðu inn þrjár tölur.")
tala1=int(input("Sláðu inn tölu 1. "))
tala2=int(input("Sláðu inn tölu 2. "))
tala3=int(input("Sláðu inn tölu 3. "))
nidurstada=tala1+tala2-tala3
print("(",tala1,"+",tala2,") -",tala3,"=",nidurstada,)

#DÆMI 4
#Fæ notenda til að slá inn hvort hann vilji að reikna ummál ferhyrnings, rúmmál sívalnings eða
#flatarmál hrings, spyr hann um mælingar og reikna síðan fyrir hann valkostinn sem hann valdi.
svar=input("Viltu reikna ummál ferhyrnings, rúmmál sívalnings eða flatarmál hrings? ")
if svar=="ummál ferhyrnings" or svar=="Ummál ferhyrnings":
    lengdFerhyrnings=int(input("Hver er lengd ferhyrningsins? "))
    breiddFerhyrnings=int(input("Hver er breidd ferhyrningsins? "))
    ummalFerhyrnings=(2*lengdFerhyrnings)+(2*breiddFerhyrnings)
    print("Ummál ferhyrningsins er",ummalFerhyrnings,)
elif svar=="rúmmál sívalnings" or svar=="Rúmmál sívalnings":
    radiusSivalnings=int(input("Hver er radíus sívalningsins? "))
    haedSivalnings=int(input("Hver er hæð sívalningsins? "))
    rummalSivalnings=(radiusSivalnings*radiusSivalnings)*3.14*haedSivalnings
    rummalSivalnings2=round(rummalSivalnings,2)
    print("Rúmmál sívalningsins er",rummalSivalnings,)
elif svar=="flatarmál hrings" or svar=="Flatarmál hrings":
    radiusHrings=int(input("Hver er radíus hringsins? "))
    flatarmalHrings=(radiusHrings*radiusHrings)*3.14
    flatarmalHrings2=round(flatarmalHrings,2)
    print("Flatarmál hringsins er",flatarmalHrings2,)
else:
    print("Rangur innsláttur.")