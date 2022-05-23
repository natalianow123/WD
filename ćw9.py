import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# zad1
# x = np.arange(1, 21)
# plt.plot(x, 1/x, label='f(x)=1/x')
# plt.legend()
# plt.xlabel('x')
# plt.ylabel('f(x)')
# plt.axis([1, 20, 0, 1])

# zad2
# x = np.arange(1, 21)
# plt.plot(x, 1/x,'g:>' ,label='f(x) = 1/x')
# plt.legend()
# plt.xlabel('x')
# plt.ylabel('f(x)')
# plt.axis([1, 20, 0, 1])
# plt.title('Wykres funkcji f(x) dla x[1,20]')

# zad3
# x = np.arange(0, 30, 0.1)
# plt.plot(x, np.sin(x), label='f(x) = sin(x)')
# plt.plot(x, np.cos(x), label='f(x) = cos(x)')
# plt.xlabel('x')
# plt.ylabel('f(x)')
# plt.legend(loc='upper right')

# zad5
# imiona = pd.read_excel('imiona.xlsx')
#
# plt.subplot(1, 3, 1)
# grupa = imiona.groupby('Plec')['Liczba'].sum()
# plt.bar(grupa.index, grupa, color=['orange', 'green'])
# plt.xlabel('płeć')
# plt.ylabel('suma narodzin w mln')
#
# plt.subplot(1, 3, 2)
# dziewczynki = imiona[imiona['Plec'] == 'K'].groupby('Rok')['Liczba'].sum()
# chlopcy = imiona[imiona['Plec'] == 'M'].groupby('Rok')['Liczba'].sum()
# plt.plot(dziewczynki.index, dziewczynki, 'r', chlopcy.index, chlopcy, 'b')
# plt.xlabel('rok')
# plt.ylabel('suma unarodzin dziewczynek i chłopców')
#
# plt.subplot(1, 3, 3)
# grupa = imiona.groupby('Rok')['Liczba'].sum()
# plt.bar(grupa.index, grupa)
# plt.xlabel('rok')
# plt.ylabel('suma narodzin')
#
# plt.subplots_adjust(wspace=1)

# zad6
zamowienia = pd.read_csv('zamowienia.csv', sep=';', decimal='.')
grupa = zamowienia.groupby('Sprzedawca')['Utarg'].sum()
explode = [0 for n in range(len(grupa.index))]
explode[7] = 0.2
plt.pie(grupa, labels=grupa.index, autopct='%.2f%%', shadow=True, explode=explode)


plt.show()