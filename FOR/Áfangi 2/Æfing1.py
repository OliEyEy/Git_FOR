#Ólafur Eysteinn - 2001002980 - 17. Janúar 2017

print("Liður 1")
tala1=int(input("Sláðu inn tölu 1. "))
tala2=int(input("Sláðu inn tölu 2. "))

print("Tölurnar lagðar saman eru",str(tala1+tala2))
print("Tölurnar margfaldaðar saman eru",str(tala1*tala2))

print(" ")
print("Liður 2")
fornafn=input("Hvað er fornafn þitt? ")
eftirnafn=input("Hvað er eftirnafn þitt? ")
print("Halló",fornafn,eftirnafn)

print(" ")
print("Liður 3")
kilometrar=float(input("Hversu margir kílómetrar?"))
metrar=kilometrar*1000
print(kilometrar,"eru",metrar)

print(" ")
print("Liður 4 - 5")
launKlst=int(input("Hversu mikil laun á klukkustund færðu? "))
fjKlst=int(input("Hversu margar klukkustundir vannstu? "))
heildarLaun=launKlst*fjKlst
skattur=heildarLaun*0.2
print("Heildarlaun verða þá:",heildarLaun,"kr.")
if heildarLaun>30000:
    print("Skattur:",round(skattur),"kr.")

print(" ")
print("Liður 6")
gradur=int(input("Hversu margar gráður? "))
hringir=gradur//360
afgGradur=gradur%360
if afgGradur==0:
    if hringir==1:
        print("Það er",hringir,"hringur.")
    else:
        print("Það eru", hringir, "hringir.")
elif afgGradur!=0:
    if hringir==1:
        print("Það er", hringir, "hringur og",afgGradur,"gráður.")
    else:
        print("Það eru",hringir,"hringir og",afgGradur,"gráður.")