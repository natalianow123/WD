import numpy as np
import pandas as pd

# zad1
# imiona = pd.read_excel('imiona.xlsx')
# print(imiona)

# zad2
# 1
# print(imiona[imiona['Liczba']>1000])
# 2
# print(imiona[imiona.Imie == 'NATALIA'])
# 3
# print(imiona.Liczba.sum())
# 4
# print(imiona[(imiona.Rok >= 2000) & (imiona.Rok <= 2005)].Liczba.sum())
# 5
# print(imiona.groupby('Plec').agg({'Liczba': ['sum']}))
# 6
# print(imiona.sort_values('Liczba').groupby(['Rok', 'Plec']).last())
# 7
# print(imiona[imiona['Plec'] == 'K'].groupby(['Imie']).agg({'Liczba': ['sum']}).sort_values(('Liczba', 'sum'), ascending=False).iloc[-1])
# print(imiona[imiona['Plec'] == 'M'].groupby(['Imie']).agg({'Liczba': ['sum']}).sort_values(('Liczba', 'sum'), ascending=False).iloc[0])

# zad3
zamowienia = pd.read_csv('zamowienia.csv', sep=';', decimal='.')
# print(zamowienia)
# 1
# print(zamowienia['Sprzedawca'].unique())
# 2
# print(zamowienia.sort_values('Utarg', ascending=False).head(5))
# 3
# print(zamowienia.groupby('Sprzedawca').size)
# 4
# print(zamowienia.groupby('Kraj').agg({'Utarg': ['sum']}))
# 5
# print(zamowienia[(zamowienia.Kraj == 'Polska') & (zamowienia['Data zamowienia'] >= '2005-01-01') & (zamowienia['Data zamowienia'] < '2006-01-01')].agg({'Utarg': ['sum']}))
# 6
# print(zamowienia[(zamowienia['Data zamowienia'] >= '2004-01-01') & (zamowienia['Data zamowienia'] < '2005-01-01')].agg({'Utarg': ['mean']}))
# 7
zamowienia_2004 = zamowienia[((zamowienia[ 'Data zamowienia'] >= '2004-01-01') & (zamowienia['Data zamowienia'] < '2005-01-01'))]
zamowienia_2004.to_csv("zamowienia_2004.csv", index=False)
zamowienia_2005 = zamowienia[((zamowienia[ 'Data zamowienia'] >= '2005-01-01') & (zamowienia['Data zamowienia'] < '2006-01-01'))]
zamowienia_2005.to_csv("zamowienia_2005.csv", index=False)