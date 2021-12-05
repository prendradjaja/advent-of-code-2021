import fileinput, collections, collections as cl, itertools, itertools as it, math, random, sys, re, string, functools
from grid import gridsource as grid, gridcustom # *, gridsource, gridcardinal, gridplane
from util import *


def main():
    f = open(sys.argv[1] if len(sys.argv) > 1 else 'in')
    lines = [l.rstrip('\n') for l in f]
    result = 0
    for line in lines:
        output = line.split('|')[1].strip()
        for digit in output.split():
            if len(digit) in [2, 3, 4, 7]:
                result += 1
    print(result)

if __name__ == '__main__':
    main()
