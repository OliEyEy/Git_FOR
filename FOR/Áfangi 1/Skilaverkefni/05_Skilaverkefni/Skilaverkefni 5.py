#Æfingarverkefni 5 - Ólafur Eysteinn Eysteinsson - 1. Nóvember 2016
import random
on="on"
while on=="on":
    print("...")
    print("1. RANDOM TÖLUR - Forritið lætur 50 random tölur á bilinu 5-70 inn í lista og birtir út nokkra hluti úr listanum.")
    print("2. TALNABIL - Forritið finnur allar tölur frá 2000-3200 sem ganga uppí 7 en ganga ekki upp í 5.")
    print("3. STRENGJALISTI - Þú skrifar inn 10 orð inn í lista og forritið birtir nokkra hluti úr listanum.")
    print("4. SAMANBURÐUR - Þú skrifar 7 orð í einn lista og 6 orð í annan lista og forritið ber saman listana og skrifar út orðin sem eru eins í báðum listum.")
    print("5. HÆTTA - Fara úr forritinu.")
    valmynd=int(input("Veldu lið 1, 2, 3, 4 eða 5 "))
    #Liður 1
    #Bý til forrit sem gerir lista úr 50 random tölum á bilinu 5-70 og segi notenda hvað margfeldi talnanna er,
    # hver hæsta og hver læsta talan er og sýni honum talnalistann, raða upp listann og sýni honum aftur.
    if valmynd==1:
        print("Liður 1")

        summa=1
        rTolur=[]
        for x in range(50):
            rTolur.append(random.randint(5,70))
            summa=summa*rTolur[x]
        print("Margfeldi allra talnanna:",summa)
        print("Hæsta talan:",max(rTolur))
        print("Læsta talan:",min(rTolur))
        print("Hér er listinn:                                       ",rTolur)
        rTolur.sort()
        print("Hér er listinn raðaður frá læstu tölunni til hæstu:   ",rTolur)
    #Liður 2
    #Bý til forrit sem finnur allar tölur á bilinu 2000 - 3200 sem ganga upp í sjö en ganga ekki upp í 5 og setur þær
    #  í lista, birtir listann og leggur saman allar tölurnar á listanum og birtir útkomuna.
    if valmynd==2:
        print("Liður 2")

        summa=0
        talnabil=[]
        for x in range(2000,3200):
            if x%7==0 and x%5!=0:
                talnabil.append(x)
                summa=summa+x
        print("Hér eru allar tölur frá 2000-3200 sem ganga upp í 7 en ekki í 5:",talnabil)
        print("Allar tölur samanlagðar:",summa)
    #Liður 3
    #Fæ notenda til þess að slá inn 10 orð inn í lista og forritið finnur öll orðin sem eru bara 4 orð og birtir þau,
    # finnur síðan annað hvert orðið og skrifar það út öfugt, raða listanum og birta hann, fær notendann til þess að
    # velja staf og forritið eyðir öllum orðum sem byrja á þeim staf í listanum og að lokum birtir listann aftur.
    if valmynd==3:
        print("Liður 3")

        fjOrd = 0
        teljari = 0
        strengjalisti = []
        print("Skrifaðu 10 orð.")
        for x in range(10):
            strengjalisti.append(input("Skrifaðu orð hér. "))
        for ord in strengjalisti:
            if len(ord)==4:
                fjOrd=fjOrd+1
                print(ord)
        print("Fjöldi orða með fjóra stafi:",fjOrd)
        strengjalisti.sort()
        for x in range(0,len(strengjalisti),2):
            ord=strengjalisti[x]
            print(ord[::-1])
        print(strengjalisti)
        print("Ég ætla að fjarlægja öll orð sem byrja á ákveðnum staf.")
        fyrstiStafur=input("Hvaða staf á ég að nota? ")
        strengjalisti2=[]
        for ord in strengjalisti:
            if ord[0]!=fyrstiStafur:
                strengjalisti2.append(ord)
            else:
                teljari=teljari+1
            strengjalisti=strengjalisti2
        print(teljari,"orðum var eytt.")
        print(strengjalisti)
    #Liður 4
    #Fæ notendann til þess að búa til 2 lista. Einn með 7 orðum og annan með 6, síðan finnur forritið ef það eru
    # einhver orð eins í báðum listunum og ef svo birtir orðin.
    if valmynd==4:
        print("Liður 4")

        ordSjo=[]
        ordSex=[]
        print("Skrifað sjö orð. ")
        for x in range(7):
            ordSjo.append(input("Skrifaðu orð hér. "))
        print("Skrifaðu sex orð.")
        for x in range(6):
            ordSex.append(input("Skrifaðu orð hér. "))
        print(ordSjo)
        print(ordSex)
        for ord in ordSjo:
            if ord in ordSex:
                print("Þetta orð er í báðum listum.",ord)

    if valmynd==5:
        print("Thank you, come again.")
        on="off"