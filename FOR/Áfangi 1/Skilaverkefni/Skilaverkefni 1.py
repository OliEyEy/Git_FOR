#Ólafur Eysteinn Eysteinsson
#30. Ágúst. 2016
#Skilaverkefni 1

#Liður 1
#Fæ nafn frá notenda og læt forritið heilsa honum.
nafn= input("Hvað heitiru?")
print ("Velkominn í áfangann FOR1A3U "+nafn+". Þetta verður skemmtileg önn, ég hlakka til að læra forritun.")

#Liður 2
#Fæ kommutölu frá notendaa og læt forritið stytta kommutöluna í bara einn aukastaf.
kommutala= float(input("Sláðu inn kommutölu með þrem aukastöfum"))
utkoma=round(kommutala, 1)
print("Þú hefur valið töluna "+str(utkoma))

#Liður 3
#Fæ tvær tölur frá notenda, læt forritið margfalda tölurnar og síðan draga fyrri töluna frá annari tölunni.
tala1=int(input("Sláðu inn tölu"))
tala2=int(input("Sláðu inn aðra tölu"))
print(tala1*tala2)
print (tala1-tala2)

#Liður 4
#Fæ hæð, lengd og breidd kassa frá notenda og læt forritið reikna út rúmmál á kassanum.
tala3=int(input("Hver er hæð kassans?(cm)"))
tala4=int(input("Hver er lengd kassans?(cm)"))
tala5=int(input("Hver er breidd kassans?(cm)"))
print ("Rúmmál kassans er "+str(tala3*tala4*tala5)+" cm")

#Liður 5
#Fæ aldut notanda og pabba hans og læt forritið reikna út hvað pabbi hans var gamall þegar notandinn fæddist.
tala6=int(input("Hvað ertu gamall?"))
tala7=int(input("Hvað er pabbi þinn gamall?"))
print ("Pabbi þinn var "+str(tala7-tala6)+" ára þegar þú fæddist")

#Liður 6
#Fæ aldur hjá þremur einstaklingum frá notenda og læt forritið reikna út meðalaldur einstaklingana.
tala8=int(input("Hvað er einstaklingur nr.1 gamall?"))
tala9=int(input("Hvað er einstaklingur nr.2 gamall?"))
tala10=int(input("Hvað er einstaklingur nr.3 gamall?"))
utkoma2=int(tala8+tala9+tala10)
print("Meðalaldur þeirra er "+str(utkoma2/3))
