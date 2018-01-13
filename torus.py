#!/usr/bin/python3

import sys

from error import *
import solve

def main(arg):
    if error(arg):
        exit(84)
    if arg[0] is 1:
        solve.bisec(arg[1:6], arg[6], pow(10, -arg[6]))
    elif arg[0] is 2:
        solve.newton(arg[1:6],  arg[6], pow(10, -arg[6]))
    elif arg[0] is 3:
        solve.secant(arg[1:6], arg[6], pow(10, -arg[6]))
    exit(0)

if __name__ == "__main__":
    main(sys.argv[1:])
