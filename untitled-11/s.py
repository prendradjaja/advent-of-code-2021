import fileinput, collections, collections as cl, itertools, itertools as it, math, random, sys, re, string, functools
from grid import gridsource as grid, gridcustom # *, gridsource, gridcardinal, gridplane
from util import *


def main():
    f = open(sys.argv[1] if len(sys.argv) > 1 else 'in')
    lines = [l.rstrip('\n') for l in f]
    energy = {}
    for r, line in enumerate(lines):
        for c, val in enumerate(line):
            val = int(val)
            energy[(r, c)] = val
    flashes = 0
    def step():
        nonlocal flashes
        for pos in energy:
            energy[pos] += 1
        first = True
        shouldcontinue = False
        while first or shouldcontinue:
            shouldcontinue = False
            first = False
            for pos in energy:
                if energy[pos] >= 9:
                    energy[pos] = 0
                    flashes += 1
                    for offset in grid.neivecs:
                        npos = grid.addvec(pos, offset)
                        r, c = npos
                        if 0 <= r < 10 and 0 <= c < 10:
                            energy[(r, c)] += 1
                    shouldcontinue = True
    for _ in range(1000):
        step()
        print(flashes)
    print(flashes)

if __name__ == '__main__':
    main()
