# zad 1
# plik = open('plik1','w')
# for i in range(0,31):
#     i*=2
#     plik.write(str(i)+' ')
# plik.close()
#
# zad 2
# plik = open('plik1','r')
# linia = plik.readline()
# print(linia)
# plik.close()
#
# zad 3
# with open('plik1','w') as plik:
#     plik.write("Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum\nhas been the industry's standard dummy text ever since the 1500s, when an unknown printer\ntook a galley of type and scrambled it to make a type specimen book. It has survived not\nonly five centuries, but also the leap into electronic typesetting, remaining essentially\nunchanged. It was popularised in the 1960s with the release of Letraset sheets containing\nLorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker\nincluding versions of Lorem Ipsum.")
# with open('plik1', 'r') as plik:
#     linie = plik.read()
# print(linie)

# zad 4
# class NaZakupy:
#     def __init__(self, nazwa_produktu, ilosc, jednostka_miary, cena_jed):
#         self.nazwa_produktu=nazwa_produktu
#         self.ilosc=ilosc
#         self.jednostka_miary= jednostka_miary
#         self.cena_jed=cena_jed
#
#     def wyswietl_produkt(self):
#         print('nazwa produktu: '+self.nazwa_produktu)
#         print('ilość: '+str(self.ilosc))
#         print('jednostka miary: '+self.jednostka_miary)
#         print('cena: '+str(self.cena_jed))
#
#     def ile_produktu(self):
#         print('ilość: '+str(self.ilosc)+" "+self.jednostka_miary)
#
#     def ile_kosztuje(self):
#         print('łączna cena: '+str(self.ilosc*self.cena_jed)+' zł')
#
# banany=NaZakupy('banany',6,'szt',4)
# banany.wyswietl_produkt()
# banany.ile_produktu()
# banany.ile_kosztuje()
#
# zad5
# class ciagi:
#     def __init__(self,a1,r,n):
#         self.a1=a1
#         self.r=r
#         self.n=n
#         self.ciag=[a1+r*x for x in range(0, n)]
#
#     def wyswietl_dane(self):
#         print(self.ciag)
#
#     def pobierz_elementy(self,*elementy):
#         for x in elementy:
#             if x<0 or x>=self.n:
#                 print('w podanym ciagu nie ma elementu a'+str(x))
#             else:
#                 print('a'+str(x)+' = '+str(self.ciag[x]))
#
#     def pobierz_parametry(self, a1, r, n):
#         self.a1 = a1
#         self.r = r
#         self.n = n
#         self.ciag = [a1 + r * x for x in range(0, n)]
#
#     def policz_sume(self):
#         print('suma ciagu = '+str((self.a1+self.ciag[self.n-1])/2*self.n))
#
#     def policz_elementy(self):
#         print(len(self.ciag))
#
# ciag=ciagi(2,4,10)
# ciag.wyswietl_dane()
# ciag.pobierz_elementy(0,5,13,9)
# ciag.pobierz_parametry(2, 3, 10)
# ciag.wyswietl_dane()
# ciag.policz_sume()
# ciag.policz_elementy()
#
# zad6
class Robaczek:
    def __init__(self,x,y,krok):
        self.x=x
        self.y=y
        self.krok=krok

    def idz_w_gore(self,ile_krokow):
        self.y+=ile_krokow*self.krok

    def idz_w_dol(self,ile_krokow):
        self.y-=ile_krokow*self.krok

    def idz_w_lewo(self,ile_krokow):
        self.x-=ile_krokow*self.krok

    def idz_w_prawo(self,ile_krokow):
        self.x+=ile_krokow*self.krok

    def pokaz_gdzie_jestes(self):
        print('x:'+str(self.x)+' y:'+str(self.y))

mrowka=Robaczek(0,0,2)
mrowka.pokaz_gdzie_jestes()
mrowka.idz_w_gore(3)
mrowka.pokaz_gdzie_jestes()
mrowka.idz_w_prawo(12)
mrowka.pokaz_gdzie_jestes()
mrowka.idz_w_dol(8)
mrowka.pokaz_gdzie_jestes()
mrowka.idz_w_lewo(4)
mrowka.pokaz_gdzie_jestes()