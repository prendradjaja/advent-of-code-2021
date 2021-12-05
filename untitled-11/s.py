import fileinput, collections, collections as cl, itertools, itertools as it, math, random, sys, re, string, functools
from grid import gridsource as grid, gridcustom # *, gridsource, gridcardinal, gridplane
from util import *
from termcolor import colored, cprint


def main():
    f = open(sys.argv[1] if len(sys.argv) > 1 else 'in')
    lines = [l.rstrip('\n') for l in f]
    energy = {}
    for r, line in enumerate(lines):
        for c, val in enumerate(line):
            val = int(val)
            energy[(r, c)] = val
    flashes = 0
    last_flashes = []
    def step():
        nonlocal flashes, last_flashes
        last_flashes = []
        for pos in energy:
            energy[pos] += 1
        first = True
        shouldcontinue = False

        # emulating a do {} while(shouldcontinue)
        while first or shouldcontinue:
            shouldcontinue = False
            first = False
            for pos in energy:
                if energy[pos] >= 9:
                    energy[pos] = float('-inf')
                    last_flashes.append(pos)
                    flashes += 1
                    for offset in grid.neivecs:
                        npos = grid.addvec(pos, offset)
                        r, c = npos
                        if 0 <= r < 10 and 0 <= c < 10:
                            energy[(r, c)] += 1
                    shouldcontinue = True
        for pos in last_flashes:
            energy[pos] = 0
    def show():
        pass
    # print('Before any steps:')
    show()
    for i in range(1000):
        step()
        # print(f'After step {i+1}:')
        show()
    print(flashes)

if __name__ == '__main__':
    main()
