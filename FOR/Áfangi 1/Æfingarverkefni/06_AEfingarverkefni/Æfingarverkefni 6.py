#Ólafur Eysteinn Eysteinsson    Æfingarverkefni 6   11. Október 2016

#Liður 1
print("liður 1")
for x in range(1,6):
    print(x)

#Liður 2
print("liður 2")
for x in range(1,11):
    if x % 2 == 0:
        print(x)

#Liður 3
print("liður 3")
for x in range(30,41):
    print(x)

#Liður 4
print("Liður 4")
teljari = 1
for x in range(10,34):
    if teljari % 6 ==0:
        print(x)
    else:
        print(x,end=" ")
    teljari=teljari+1

#Liður 5
print("Liður 5")
fjA="A"
for x in range(5):
    print(fjA)
    fjA=fjA+"A"

#Liður 6
print("Liður 6")
teljari=1
while teljari<6:
    print(teljari)
    teljari=teljari+1

#Liður 7
print("Liður 7")
teljari=1
while teljari<10:
    if teljari % 2 != 0:
        print(teljari)
    teljari=teljari+1

#Liður 8
print("Liður 8")
teljari=30
while teljari<41:
    print(teljari)
    teljari=teljari+1

#Liður 9
print("Liður 9")
x=10
teljari=1
while x<34:
    if teljari%6==0:
        print(x)
    else:
        print(x, end=" ")
    teljari=teljari+1
    x=x+1

#Liður 10
print("Liður 10")
fjA="A"
teljari=1
while teljari<6:
    print(fjA)
    fjA=fjA+"A"
    teljari=teljari+1