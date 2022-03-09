# zad1
# sporty=["tenis","siatkówka","koszykówka","lekkoatletyka"]
# sporty.reverse()
# sporty.append("piłka nożna")
# sporty.append("rugby")
# print(sporty)

# zad2
# skróty={"np":"na przykład","etc":"et cetera","itp":"i tym podobne","art":"artykuł"}
# print(skróty)

# zad3
# gry={"Lol":"League of legends","GTA":"Grand Theft Auto","MC":"Minecraft","CS":"Counter-Strike"}
# print(gry)
# print(len(gry.keys()))

# zad4
# napis=input("podaj napis: ")
# ile=napis.count("a")
# print("Ilość liter a:",ile)

# zad5
# import sys as system
# system.stdout.write("Podaj 3 liczby: ")
# a=system.stdin.readline()
# b=system.stdin.readline()
# c=system.stdin.readline()
# a,b,c=int(a),int(b),int(c)
# system.stdout.write(str(a**b+c))

# zad6
# a=input("podaj pierwszą liczbę: ")
# b=input("podaj drugą liczbę: ")
# c=input("podaj trzecią liczbę: ")
# a,b,c=int(a),int(b),int(c)
# if a>=b:
#     if a>=c:
#         print(a)
#     else:
#         print(c)
# elif b>=c:
#     print(b)
# else:
#     print(c)

# zad7
# lista=[5,2.2,13,120,6.9,0.01]
# for i in range(0,len(lista),1):
#     lista[i]**=2
# print(lista)

# zad8
# tab=[]
# i=0
# while i!=10:
#     liczba=input("podaj liczbę: ")
#     liczba=int(liczba)
#     if liczba%2==0:
#         tab.append(liczba)
#     i+=1
# print(tab)

# zad9
import math
liczba=input("podaj liczbe: ")
liczba=int(liczba)
try:
    print(math.sqrt(liczba))
except ValueError:
    print("Liczba pod pierwiastkiem nie może być ujemna")
