import random
import wzory.geo
import wzory.aryt

# zad1
# A=[1-x for x in range(1,11)]
# print(A)
# B=[4**x for x in range(0,8)]
# print(B)
# C=[x for x in B if x%2==0]
# print(C)

# zad2
# lista1=[random.randint(0,100) for x in range(0,10)]
# print(lista1)
# parzyste=[x for x in lista1 if x % 2 == 0]
# print(parzyste)

#zad3
# produkty_spozywcze={"chleb":'szt',"mleko":'l','jajka': 'szt','pomidory': 'kg'}
# print(produkty_spozywcze)
# lista=[key for key, value in produkty_spozywcze.items() if value=='szt']
# print(lista)

#zad4
# def czy_prostokatny(a,b,c):
#     if a**2+b**2==c**2:
#         print('trójkąt jest prostokatny')
#     else:
#         print('trójkąt nie jest prostokatny')
# czy_prostokatny(3,4,5)
# czy_prostokatny(5,9,16)

#zad5
# def pole(h=1,a=1,b=1):
#     print((a+b)*h/2)
# pole()
# pole(5,3,9)
# pole(a=5,b=10)

#zad6
# def iloczyn(a=1,b=4,ile=10):
#     iloczyn=a
#     for i in range(ile):
#         iloczyn*=b
#     return iloczyn
# print(iloczyn())
# print(iloczyn(2,3,6))

#zad7
# def iloczyn2(*liczby):
#     iloczyn=1
#     for i in liczby:
#         iloczyn*=i
#     return iloczyn
# print(iloczyn2(2,3,6,12,7,2,4))

#zad8
# def zliczanie(**produkty):
#     ilosc=0
#     laczna_cena=0
#     for cena in produkty:
#         ilosc+=1
#         laczna_cena+=produkty[cena]
#     print("ilosc produktow: ",ilosc)
#     print("cena: ",laczna_cena)
# zliczanie(chleb=2.50,jajka=6.99,ciastka=9.99,ser=5.89,frytki=17.49)

#zad9
print(wzory.geo.wyraz_ciagu(1,2,4))
print(wzory.geo.suma_wyrazow(1,2,4))
print(wzory.aryt.wyraz_ciagu(1,2,4))
print(wzory.aryt.suma_wyrazow(1,7,4))