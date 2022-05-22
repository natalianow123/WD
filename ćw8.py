import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

imiona = pd.read_excel('imiona.xlsx')

# zad1
grupa = imiona.groupby(['Rok']).sum()
wykres = grupa.plot()
wykres.set_title('Liczba urodzonych dzieci każdego roku')
wykres.set_ylabel('Liczba urodzonych dzieci')
plt.subplots_adjust(left=0.2, right=0.9, bottom=0.2, top=0.9)
roczniki = imiona['Rok'].unique()
wykres.set_xticks(roczniki)
wykres.tick_params(axis='x', labelrotation=50)

# zad2
# grupa = imiona.groupby(['Plec']).agg({'Liczba':['sum']})
# wykres = grupa.plot.bar()
# wykres.set_title("Liczba urodzonych dziewczynek i chłopców")
# wykres.set_ylabel('Liczba dzieci')
# wykres.legend(['dzieci'])
# wykres.tick_params(rotation=0)

#zad3
# grupa = imiona[imiona['Rok'] >= 2013].groupby(['Plec']).agg({'Liczba':['sum']})
# wykres = grupa.plot(kind='pie', subplots=True, autopct='%.2f%%', fontsize=20, figsize=(6,6), title='Procet urodzonych dziewczynek i chłopców od 2012 do 2017')

#zad4
# zamowienia = pd.read_csv('zamowienia.csv', sep=';', decimal='.')
# grupa = zamowienia.groupby('Sprzedawca').agg({'idZamowienia':['count']})
# wykres = grupa.plot.bar(title='Ilość zamówień sprzedawców', ylabel='Ilość zamówień')
# wykres.legend(['Zamóweinia'])
# wykres.tick_params(axis='x', labelrotation=20)
# plt.subplots_adjust(left=0.15, right=0.9, bottom=0.2, top=0.9)

plt.show()
