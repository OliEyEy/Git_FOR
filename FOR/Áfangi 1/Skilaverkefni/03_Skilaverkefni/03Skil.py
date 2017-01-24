#Skilaverkefni 3 - Ólafur Eysteinn

#Liður 1
#Fæ notenda til þess að slá tölu, segja honum hvaða tölu hann valdi og spyr hann hvort hann vilji slá inn tölu oftar,
#ef svo þá gerir forritið það eins oft og hann vill.
tala1=int(input("Sláðu inn tölu."))
print("Þú hefur valið töluna:",tala1,)
svar=(input("Viltu slá inn aðra tölu? Já eða Nei."))
while(svar=="Já"):
    tala1=int(input("Sláðu inn aðra tölu."))
    print("Þú hefur valið töluna:",tala1,)
    svar = (input("Viltu slá inn aðra tölu? Já eða Nei."))
print("Takk fyrir og bless.")

#Liður 2
#Fæ notenda til þess að slá inn lengd og breidd ferhyrnings og reikna flatarmál ferhyrningsins fyrir hann.
#Spyr hann síðan hvort hann vilji reikna flatarmál oftar, ef svo þá gerir forritið það eins oft og hann vill.
print("Ég ætla að reikna flatarmál ferhyrnings fyrir þig.")
lengd=int(input("Sláðu inn lengd ferhyrningsins."))
breidd=int(input("Sláðu inn breidd ferhyrningsins."))
flatarmal=lengd*breidd
print("Flatarmál ferhyrningsins er",flatarmal)
svar2=input("Á ég að reikna flatarmál ferhyrnings aftur? Já eða Nei. ")
while(svar2=="Já"):
    lengd = int(input("Sláðu inn lengd ferhyrningsins."))
    breidd = int(input("Sláðu inn breidd ferhyrningsins."))
    flatarmal = lengd * breidd
    print("Flatarmál ferhyrningsins er", flatarmal)
    svar2 = input("Á ég að reikna flatarmál ferhyrnings aftur? Já eða Nei. ")
print("Takk fyrir og bless.")

#Liður 3
#Fæ notenda til að slá inn leyniorðið en ef notendandinn giskar vitlaust, þarf hann að giska aftur og aftur þangað til
#hann giskar rétt
leyniord="Leyniorðið"
gisk=input("Sláðu inn leyniorðið. ")
while(leyniord!=gisk):
    print("Vitlaust.")
    gisk=input("Giskaðu aftur. ")
print("Rétt! Þú mátt halda áfram.")

#liður 4
#Fæ notendan til að slá inn hversu mikinn pening hann á og segi honum hversu marga 5000 kalla, 1000 kalla o.s.fv hann á
peningar=int(input("Hvað áttu mikinn pening? "))
fj5000=int(peningar/5000)
afg5000=peningar%5000
fj1000=int(afg5000/1000)
afg1000=afg5000%1000
fj500=int(afg1000/500)
afg500=afg1000%500
fj100=int(afg500/100)
afg100=afg500%100
fj50=int(afg100/50)
afg50=afg100%50
fj10=int(afg50/10)
afg10=(afg50%10)
fj5=int(afg10/5)
afg5=afg10%5
fj1=int(afg5/1)
print("Þú átt",fj5000,"fimmþúsund kalla,",fj1000,"þúsund kalla,",fj500,"fimmhundruð kalla,",fj100,"hundrað kalla,",fj50,
"fimmtíu kalla,",fj10,"tíkalla,",fj5,"fimmkalla og",fj1,"eina krónur.")

#Liður 5
#Fæ notenda til þess að velja notkun forritsins sem er annaðhvort 1.sláðu inn 10 tölur og ég finn summu og meðaltal þeirra.
# 2. slá inn tölu og ég segi hvort hún sé slétt- eða oddatala. Ég geri þetta fyrir hann eins oft og hann vill þangað til
# að hann velur valmöguleika 3. Þá monnta ég mig, segi honum hversu oft hann notaði forritið og forritið endar.
svar3="Já"
hveOft=0
while svar3=="Já":
    hveOft=hveOft+1
    print("1. Sláðu inn 10 tölur og ég finn summu og meðaltal þeirra.")
    print("2. Sláðu inn tölu og ég segi þér hvort hún er slétt eða oddatala.")
    print("3. Hætta í forritinu.")
    valmynd=int(input("Veluru 1, 2 eða 3? "))
    if valmynd==1:
        summa=0
        teljari=0
        while (teljari<10):
            teljari=teljari+1
            tala=int(input("Sláðu inn tölu."))
            summa=summa+tala
        medaltal=summa/10
        print("Meðaltala talnanna þína er",medaltal)
        print("Summa talnanna þína er",summa)
    elif valmynd==2:
        tala2=int(input("Sláðu inn tölu."))
        if tala2%2==0:
            print("Talan þín er slétt tala.")
        else:
            print("Talan þín er oddatala")
    elif valmynd==3:
        teljari2=0
        while teljari2<10:
            print("Ég er frábær forritari.")
            teljari2=teljari2+1
        print("Þú hefur notað forritið",hveOft,"sinnum.")
        svar3="Neibb"
    else:
        print("Þú hefur ekki valið rétt.")

#Verkefni F
#Fyrra kóðabrotið virkar þannig að hann enturtekur það sem er inn í while-inu 10 sinnum og getur þess vegna verið notað
# til þess að gera eitthvað 10 sinnum (eða minna eða oftar ef þú breytir kóðanum aðeins.
#Seinna kóðabrotið virkar þannig að "i" verður aldrei 10 svo að það mun halda áfram endalaust svo það er hægt að nota
# það ef maður vill að eitthvað inn í while-inu heldur endalaust áfram