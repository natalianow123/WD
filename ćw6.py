import numpy as np
# zad1
# a = np.arange(3)
# b = np.array([2, 4, 8])
# print(a * b)

# zad2
# a = np.array([[6,1,3], [4,9,1], [5,3,0]])
# b = np.array([[7,4,2,3], [7,3,7,4], [9,8,0,2], [1,0,4,8]])
# print(a)
# print()
# print(a.min(axis=0))
# print()
# print(a.min(axis=1))
# print()
# print(b)
# print()
# print(b.min(axis=0))
# print()
# print(b.min(axis=1))

# zad3
# print(np.dot(a, b))

# zad4
# a = np.array([2, 3, 4])
# b = np.array([5.5, 6.2, 7.9])
# print(a*b)

# zad5
# m = np.array([[2, 3, 4], [5, 6, 7]])
# a = np.sin(m)
# print(a)

# zad6
# n = np.array([[11, 12, 13], [14, 15, 16]])
# b = np.cos(n)
# print(b)

# zad7
# def dodawanie(a, b):
#     return a+b
#
# print(dodawanie(a, b))

# zad8
# a = np.array([[2, 3, 4], [5, 6, 7], [8, 9, 10]])
# for i in a:
#     print(i)
#     print()

# zad9
# a = np.array([[2, 3, 4], [5, 6, 7], [8, 9, 10]])
# for i in a.flat:
#     print(i)

# zad10
# a = np.arange(81).reshape((9, 9))
# print(a)
# print()
# a1 = a.reshape(1, 81)
# print(a1)
# print()
# a2 = a.reshape(81, 1)
# print(a2)
# print()
# a3 = a.reshape(3, 27)
# print(a3)
# print()
# a4 = a.reshape(27, 3)
# print(a4)

# zad11
a = np.arange(12)
print(a)
print()
a1 = a.reshape(3, 4)
print(a1)
print()
a2 = a.reshape(4, 3)
print(a2)
print()
a3 = a.reshape(2, 6)
print(a3)
print()
print(a1.ravel())
print(a2.ravel())
print(a3.ravel())