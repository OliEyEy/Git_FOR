#Ólafur Eysteinn - 2001002980 - 17. Janúar 2017

print("Liður 1")
nafn1=input("Fyrra nafn: ")
haed1=int(input("Hæð í sentimetrum: "))
nafn2=input("Seinna nafn: ")
haed2=int(input("Hæð í sentimetrum: "))
if haed1==haed2:
    print(nafn1,"og",nafn2,"eru jafnhá/ir.")
elif haed1!=haed2:
    if haed1<haed2:
        print(nafn2,"er hærri en",nafn1,".")
    elif haed1>haed2:
        print(nafn1,"er hærri en",nafn2,".")

print(" ")
print("Liður 2")
lengd=float(input("Lengd í metrum: "))
breidd=int(input("Breidd í metrum: "))
ekrur=(lengd*breidd)/4046
print("Þessi reitur er",round(ekrur,3),"ekrur.")

print(" ")
print("Liður 3")
breidd=int(input("Breidd fernings í metrum: "))
for x in range(0,201,10):
    print("Stærð"," ","Lengd í ekrum")
    ekrur=(x*breidd)/4046
    print(x," "," ",round(ekrur,6))

print(" ")
print("Liður 4")
afangi=input("Hvað er skammstöfun áfanga þíns? ")
for staf in afangi:
    if staf