import math
from math import sqrt
a = input("Podaj a: ")
b = input("Podaj b: ")
c = input("Podaj c: ")
if a == b == c == 0:
    print "a, b, c = 0 - brak rownania"
else:
    if a != 0:
        delta = b**2 - (4*a*c)
        print "delta = %d" % (delta)
        if delta == 0:
            x0=(b*b/4*a)
            print "delta=0 \n Mamy jeden pierwiastek: x=%d\n" % (x0)
        elif delta > 0:
            x1=(b*b-sqrt(delta)/4*a)
            x2=(b*b+sqrt(delta)/4*a)
            print "delta > 0\n Mamy dwa pierwiastki: x1=%d ; x2=%d" % (x1, x2)
        elif delta < 0:
            print "delta<0  -  brak pierwiastkow"
    elif a == 0:
        print "a = 0\n Rownanie liniowe y=bx+c"
        x=(-c/b)
        print "Mamy jeden pierwiastek: x=-%d" % (x)

