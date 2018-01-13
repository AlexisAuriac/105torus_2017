from math import *

import pol

def bisec(coef, prec, limit):
    max = 100
    iter = 0
    x1 = 0
    x2 = 1
    xm = float()

    while (1):
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
    val = 0.5
    val_next = float()

    print("x = 0.5")
    while 1:
        val_next = val - pol.compute(coef, val) / pol.compute(derived, val)
        print(("x = %.*f" % (prec, val_next)).rstrip('0'))
        if abs(pol.compute(coef, val_next)) < limit:
            return 1
        if iter > max:
            return 0
        iter += 1
        val = val_next

def secant(coef, prec):
    return 0
