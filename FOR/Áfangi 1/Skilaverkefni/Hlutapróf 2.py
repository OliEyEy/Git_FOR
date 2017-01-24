#Hlutapróf 1 - Ólafur Eysteinn Eysteinsson - 20.10.2016

#Liður 16
#Fæ notenda til þess að slá inn x mikið af sentimetrum og forritið sýnir til
# baka hversu margir metrar, desimetrar og sentimetrar það er.
#Síðan fær notandinn val um að gera aftur eða halda áfram.
print("Liður 16")

svar="j"
while svar=="j":
    sentimetrar=int(input("Sláðu inn lengd í sentimetrum: "))
    fjMetrar=int(sentimetrar/100)
    afgMetrar=sentimetrar%100
    fjDesimetrar=int(afgMetrar/10)
    afgDesimetrar=afgMetrar%10
    fjSentimetrar=int(afgDesimetrar/1)
    print(fjMetrar,"metrar.")
    print(fjDesimetrar,"desimetrar.")
    print(fjSentimetrar,"sentimetrar.")
    svar=input("Viltu keyra forritið aftur? Sláðu inn j ef já.")

#Liður 17
#Fæ notenda til þess að slá inn tölu og aðra til þess að vera veldisvísir fyrri
# tölunnar og reikna síðan út töluna í x veldi.
#Síðan fær notandinn val um að gera aftur eða halda áfram. 
print("Liður 17")

svar="j"
while svar=="j":
    x=int(input("Sláðu inn tölu: "))
    n=int(input("Sláðu inn aðra veldisvísi: "))
    z=1
    for i in range(n):
        z=z*x
    print(z)
    svar=input("Viltu keyra forritið aftur? Sláðu inn j ef já.")


