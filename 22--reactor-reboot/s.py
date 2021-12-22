import fileinput, collections, collections as cl, itertools, itertools as it, math, random, sys, re, string, functools
from grid import gridsource as grid, gridcustom # *, gridsource, gridcardinal, gridplane
from util import *

def main():
    f = open(sys.argv[-1] if len(sys.argv) > 1 and sys.argv[-1] != '-' else 'in')
    lines = [l.rstrip('\n') for l in f]
    on = set()
    for line in lines:
        cmd, *region = parse_line(line)
        xlo, xhi, ylo, yhi, zlo, zhi = region
        if not excludes_initialization_area(region):
            for x in range(xlo, xhi+1):
                for y in range(ylo, yhi+1):
                    for z in range(zlo, zhi+1):
                        pos = x,y,z
                        if cmd == 'on':
                            on.add(pos)
                        elif cmd == 'off':
                            on.discard(pos)
                        else:
                            1/0
    print(len(on))


def parse_line(line):
    cmd, rest = line.split(' ')
    return cmd, *findints(rest)


def excludes_initialization_area(region):
    xlo, xhi, ylo, yhi, zlo, zhi = region
    return (
        xlo < xhi < -50 or
        ylo < yhi < -50 or
        zlo < zhi < -50 or
        xhi > xlo > 50 or
        yhi > ylo > 50 or
        zhi > zlo > 50
    )


def unused_just_for_line_completion():
    xlo, xhi, ylo, yhi, zlo, zhi = region



if __name__ == '__main__':
    main()
