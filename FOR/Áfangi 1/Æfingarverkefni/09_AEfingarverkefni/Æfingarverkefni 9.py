#Æfingarverkfefni 9 - Ólafur Eysteinn - 8. Nóvember 2016

on="on"
while on=="on":
    print("1. Lengsta orðið - 2. Random tölur - 3. Að telja orð - 4. Afturábak - 5. Hætta")
    valmynd=int(input("Veldu lið. 1, 2, 3, 4 eða 5. "))
    if valmynd==1:
        #Liður 1
        print("Liður 1")
        ordalisti=[]
        print("Sláðu 5 orð inn í lista.")
        for x in range(5):
            nafn=input("Slá inn orð hér. ")
            ordalisti.append(nafn)
        print(ordalisti)
        radad=sorted(ordalisti, key=len)
        print("Lengsta orðið er",min(radad))
        print("Það er",len(min(radad)),"stafir.")
    if valmynd==2:
        #Liður 2
        print("Liður 2")
        nafn=input("Sláðu inn nafn þitt. ")
        print("Nafnið þitt í stórum stöfum er",nafn.upper())
        print("Nafnið þitt í litlum stöfum er", nafn.lower())
        stafur=input("Sláðu inn einhvern staf og forritð skiptir honum út fyrir @ ")
        for staf in nafn:
            nafn=nafn.replace(stafur, "@")
        print(nafn)
    if valmynd==3:
        #Liður 3
        print("Liður 3")
        hveMorgOrd=1
        strengur=input("Sláðu inn setningu. ")
        for staf in strengur:
            if staf==" ":
                hveMorgOrd=hveMorgOrd+1
        print("Þú skrifaðir",hveMorgOrd,"orð.")
    if valmynd==4:
        #Liður 4
        print("Liður 4")
        setning=input("Sláðu inn setningu. ")
        print(setning[::-1])
    if valmynd==5:
        print("Takk fyrir mig.")
        on="off"