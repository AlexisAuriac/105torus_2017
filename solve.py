from math import *

import pol

def bisec(coef, prec, limit):
    max = 100
    iter = 0
    x1 = 0
    x2 = 1
    xm = float()

    while 1:
        xm = (x1 + x2) / 2
        print(("x = %.*f" % (prec, xm)).rstrip('0'))
        if abs(pol.compute(coef, xm)) < limit:
            return 1
        if pol.compute(coef, x1) * pol.compute(coef, xm) < 0:
            x2 = xm
        else:
            x1 = xm
        if iter > max:
            return 0
        iter += 1

def newton(coef, prec, limit):
    max = 20
    iter = 0
    derived = pol.derive(coef)
    xn = 0.5
    xn1 = float()

    print("x = 0.5")
    while 1:
        xn1 = xn - pol.compute(coef, xn) / pol.compute(derived, xn)
        print(("x = %.*f" % (prec, xn1)).rstrip('0'))
        if abs(pol.compute(coef, xn1)) < limit:
            return 1
        if iter > max:
            return 0
        iter += 1
        xn = xn1

def secant(coef, prec, limit):
    max = 100
    iter = 0
    xn_1 = 0
    xn = 1
    xn1 = 0

    while 1:
        xn1 = xn - (pol.compute(coef, xn) * (xn - xn_1)) / (pol.compute(coef, xn) - pol.compute(coef, xn_1))
        print(("x = %.*f" % (prec, xn1)).rstrip('0'))
        if abs(pol.compute(coef, xn1)) < limit:
            return 1
        if iter > max:
            return 0
        iter += 1
        xn_1 = xn
        xn = xn1
    return 0
