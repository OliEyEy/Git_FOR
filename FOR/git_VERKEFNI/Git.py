#Ólafur Eysteinn - 2001002980 - 24. Janúar 2017

#Læt notenda slá inn tvær tölur, legg þær saman og margfalda þær
print("Liður 1")
tala1=int(input("Sláðu inn tölu 1. "))
tala2=int(input("Sláðu inn tölu 2. "))
print("Tölurnar lagðar saman eru",str(tala1+tala2))
print("Tölurnar margfaldaðar saman eru",str(tala1*tala2))

print(" ")
#Læt notenda skrifa inn nafn sitt og heilsa honum síðan
print("Liður 2")
fornafn=input("Hvað er fornafn þitt? ")
eftirnafn=input("Hvað er eftirnafn þitt? ")
print("Halló",fornafn,eftirnafn)

print(" ")
#Læt notenda slá inn einhvern texta, segi honum hversu mikið af lástöfum, HÁSTÖFUM
# og 'lástöfum á eftir HÁSTÖFUM' hann gerði.
print("Liður 3")
texti=input("Skrifaðu inn texta. ")
lastafur=0
hastafur=0
laHastafur=0
for staf in texti:
    if staf.islower():
        lastafur=lastafur+1
    if staf.isupper():
        hastafur=hastafur+1
for x in range(len(texti)):
    if texti[x].isupper():
        if texti[x+1].islower():
            laHastafur=laHastafur+1
print("Það eru",lastafur,"lástafir.")
print("Það eru",hastafur,"hástafir.")
print("Það eru",laHastafur,"lástafir sem koma strax á eftir hástaf.")