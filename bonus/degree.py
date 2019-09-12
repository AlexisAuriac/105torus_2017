from math import *

from error import *
import solve

def degree1(arg):
    if error(arg, 3):
        return 84
    print(("x = %*f" % (arg[2], (-arg[0]) / arg[1])).rstrip("0"))
    return 0

def degree2(arg):
    if error(arg, 4):
        return 84
    c, b, a = arg[0], arg[1], arg[2]
    delta = b**2 - 4*a*c
    sol = list()

    if delta < 0:
        print("No solution")
    if delta == 0:
        print(("x = %*f" % (arg[3], -b/(2*a))).rstrip("0"))
    elif delta > 0:
        print(("x = %*f" % (arg[3], (-b+sqrt(delta))/(2*a))).rstrip("0"))
        print(("x = %*f" % (arg[3], (-b-sqrt(delta))/(2*a))).rstrip("0"))
    return 0

def degree4(arg):
    if error(arg, 7):
        return 84
    if arg[0] < 1 or arg[0] > 3 or arg[6] < 0:
        return 84
    if arg[0] is 1:
        solve.bisec(arg[1:6], arg[6], pow(10, -arg[6]))
    elif arg[0] is 2:
        solve.newton(arg[1:6],  arg[6], pow(10, -arg[6]))
    elif arg[0] is 3:
        solve.secant(arg[1:6], arg[6], pow(10, -arg[6]))
    return 0

def get(arg):
    arg[0] = int(arg[0])

    if arg[0] < 1 or arg[0] > 4:
        return 84
    elif arg[0] is 1:
        return(degree1(arg[1:]))
    elif arg[0] is 2:
        return(degree2(arg[1:]))
    elif arg[0] is 3:
        return(degree3(arg[1:]))
    elif arg[0] is 4:
        return(degree4(arg[1:]))
