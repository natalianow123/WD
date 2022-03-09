# zad 1
import re

a=2
b=152
c=27.4
d=0.2
e=5+2j
f=92+12j
g='c'
h='Python'
print(a,b,c,d,e,f,g,h)

# zad 2
a=10
b=7.2
print(a,'+',b,'=',a+b)
print(a,'-',b,'=',a-b)
print(a,'*',b,'=',a*b)
print(a,'/',b,'=',a/b)

# zad 3
a=5
a+=1
print(a)

a=5
a-=1
print(a)

a=5
a*=2
print(a)

a=5
a/=2
print(a)

a=5
a**=2
print(a)

a=5
a%=2
print(a)

# zad 4
import math
print(math.e**10)
print((math.log(5)+(math.sin(8)**2))**(1 / 6))
print(math.floor(3.55))
print(math.ceil(4.80))

# zad5
imię="NATALIA"
nazwisko="NOWAKOWSKA"
print(str.capitalize(imię),str.capitalize(nazwisko))

# zad6
refren="la la leyli, la la leyli, la la la la la"
print(refren.count("la"))

# zad7
napis="napis"
print(napis[1], napis[len(napis)-1])

# zad8
print(refren.split())

# zad9
a='napis'
b=49.22
c=0x0a3f2
print('%(z1)s %(z2)f %(z3)x'%{'z1':a, 'z2':b, 'z3':c})