#Liður 1
#Fæ notenda til að slá inn tvær tölur og segja nemandanum hvor er stærri
tala1=int(input("Sláðu inn tölu"))
tala2=int(input("Sláðu inn aðra tölu"))
if tala1 < tala2:
    print("Seinni talan er stærri")
elif tala2 < tala1:
    print("Fyrri talan er stærri")
else:
    print("Tölurnar eru jafnstórar")

#Liður 2
#Spyr notenda hvaða mánuður er og segji honum númer hvaða mánuður það er
man=input("Hvaða mánuður er núna?")
if man=="Janúar":
    print("Mánuður nr.1")
elif man=="Febrúar":
    print("Mánuður nr.2")
elif man=="Mars":
    print("Mánuður nr.3")
elif man=="Apríl":
    print("Mánuður nr.4")
elif man=="Maí":
    print("Mánuður nr.5")
elif man=="Júní":
    print("Mánuður nr.6")
elif man=="Júlí":
    print("Mánuður nr.7")
elif man=="Ágúst":
    print("Mánuður nr.8")
elif man=="September":
    print("Mánuður nr.9")
elif man=="Október":
    print("Mánuður nr.10")
elif man=="Nóvember":
    print("Mánuður nr.11")
elif man=="Desember":
    print("Mánuður nr.12")
else:
    print("Ég þekki ekki þennan mánuð")
    
#Liður 3
#Spyr notenda hvað hann er gamall og svara eins og hentar
aldur=int(input("Hvað ertu gömul/gamall?"))
if aldur>=0 and aldur<=6:
    print("Nú, svo þú ferð að byrja í skóla")
elif aldur>=7 and aldur<=15:
    svar=input("Ætlar þú í menntaskóla?")
    if svar=="Já":
        print("Gott fyrir þig")
    elif svar=="Nei":
        print("Jæja, gangi þér vel")
    else:
        print("Þú svaraðir vitlaust")
elif aldur>=16 and aldur<=105:
    print ("Gangi þér vel í framtíðinni")
else:
    print("Þú svaraðir spurningunni vitlaust")

#Liður 4
#Fæ notenda til að slá inn tölu á milli 0-25 og margfalda hana með 1,7
tala3=int(input("Sláðu inn tölu á milli 0-25"))
if tala3>=0 and tala3<=25:
    print(tala3*1.7)
else:
    print("Rangur innsláttur")

#Liður 5
#5Spyr notenda hvort hann vill heyra brandara, ef hann segir já þá segi ég honum brandara
svar2=input("Viltu heyra brandara?")
if svar2=="Já":
    print("Það var maður sem fór til læknis og sagðist eiga við vandamál að stríða, nú sagði læknirinn, hvað er vandamálið. Jú sjáðu til ég þarf alltaf að kúka kl 9 á morgnana. Er það eitthvað vandamál, sagði læknirinn. Já sagði maðurinn ég vakna aldrei fyrr en 10.")
elif svar2=="Nei":
    print("Allt í lagi, kannski seinna")
