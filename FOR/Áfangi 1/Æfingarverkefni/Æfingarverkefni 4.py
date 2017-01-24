#Æfingar verkefni 4  -  Ólafur Eysteinn
nafn=input("Sláðu inn nafn þitt. ")
kt=int(input("Sláðu inn kennitöluna þína. "))
vinnutimi=int(input("Sláðu inn hversu marga tíma hefur þú unnið. "))

if vinnutimi<=40:
    dagvinnuFj=vinnutimi
    yfirvinnuFj=0
    extratimaFj=0
elif vinnutimi>40 and vinnutimi<=60:
   dagvinnuFj=40
   yfirvinnuFj=(vinnutimi-40)
   extratimaFj=0
elif vinnutimi>60:
    dagvinnuFj=40
    yfirvinnuFj=20
    extratimaFj=(vinnutimi-60)

dagvinnuLaun= dagvinnuFj*1200
yfirvinnuLaun=yfirvinnuFj*(1800*1.5)
extratimaLaun=extratimaFj*(1200*2)
heildarLaun=dagvinnuLaun+yfirvinnuLaun+extratimaLaun

print(nafn+" kt: "+str(kt))
print("Heildarlaun þín fyrir vikuna eru: ",heildarLaun," kr.")
print("Þú ert með " ,dagvinnuFj, " tíma í dagvinnu sem gera: " ,dagvinnuLaun, "kr.")

if yfirvinnuFj >0:
    print("Þú ert með " ,yfirvinnuFj," tíma í yfirvinnu sem gera " ,yfirvinnuLaun, "kr.")
if extratimaFj >0:
    print("Þú ert með " ,extratimaFj, " tíma í extravinnu sem gera " ,extratimaLaun, "kr.")