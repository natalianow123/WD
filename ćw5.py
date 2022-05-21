import numpy as np
# zad 1
# a = np.arange(4, 21*4, 4)
# print(a)

# zad 2
# b = np.array([2.5, 3.0, 12.1, 40.9])
# print(b)
# c = b.astype('int32')
# print(c)

# zad 3
# def funkcja(n):
#     m = np.ones((n, n), 'int')
#     p = 2
#     for i in range(0,n):
#         for j in range(0, n):
#             m[i][j] = p
#             p = p * 2
#     return m
#
# print(funkcja(5))

# zad 4
# def funkcja2(l, n):
#     tab = np.logspace(1, n, num=n, base=l)
#     return tab
#
# print(funkcja2(2, 4))

# zad 5
# def funkca3(n):
#     md = np.diag([a for a in range(n, 0, -1)], 2)
#     return md
#
# print(funkca3(4))

# zad7
# def funkcja3(n):
#     macierz = np.diag([2 for _ in range(n)])
#     for i in range(1, n):
#         macierz += np.diag([2*(i+1) for j in range(n-i)], k=i)
#         macierz += np.diag([2*(i+1) for j in range(n-i)], k=-i)
#     return macierz
#
# print(funkcja3(3))

# zad8
# def funkcja4(tab, kierunek):
#     if kierunek == 'poziomo':
#         if tab.shape[0] % 2 != 0:
#             print("Tablica posiada nieprzystą liczbę wierszy")
#             return
#         p1 = tab[0:int(tab.shape[0]/2), :]
#         p2 = tab[int(tab.shape[0]/2):, :]
#         print(p1)
#         print()
#         print(p2)
#     elif kierunek == "pionowo":
#         if tab.shape[1] % 2 != 0:
#             print("Tablica posiada nieprzystą liczbę kolumn")
#             return
#         p1 = tab[:, 0:int(tab.shape[1]/2)]
#         p2 = tab[:, int(tab.shape[1] / 2):]
#         print(p1)
#         print()
#         print(p2)
#
# tablica1 = np.arange(16).reshape((4,4))
# tablica2 = np.arange(25).reshape((5,5))
# print(tablica1)
# print()
# funkcja4(tablica1, 'pionowo')
# print()
# funkcja4(tablica1, 'poziomo')
# print()
# print(tablica2)
# print()
# funkcja4(tablica2, 'pionowo')

# zad9
a1 = 1
r = 3
macierz = np.zeros(25)
macierz[0] = a1
for i in range(1, 25, 1):
    macierz[i] = macierz[i-1] + r
macierz = macierz.reshape((5, 5))
print(macierz)