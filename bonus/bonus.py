#!/usr/bin/python3

import sys

import degree

def main(arg):
    if degree.get(arg):
        exit(84)
    exit(0)
    
if __name__ == "__main__":
    main(sys.argv[1:])
