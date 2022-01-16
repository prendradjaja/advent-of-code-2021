import fileinput, collections, collections as cl, itertools, itertools as it, math, random, sys, re, string, functools
# from grid import gridsource as grid, gridcustom # *, gridsource, gridcardinal, gridplane
from util import *
from day22 import region_overlap


def main():
    f = open(sys.argv[1] if len(sys.argv) > 1 else 'in')
    lines = [l.rstrip('\n') for l in f]
    counts = cl.Counter()
    regions = []
    for line in lines:
        x1,y1,x2,y2 = findints(line)
        if x1 == x2 or y1 == y2:
            region = ((x1, x2), (y1, y2))
            regions.append(region)
    for ra, rb in itertools.combinations(regions, 2):
        overlap = region_overlap(ra, rb)
        if overlap:
            print_overlap(overlap)

def print_overlap(overlap):
    ((x1, x2), (y1, y2)) = overlap
    print(f'on x={x1}..{x2},y={y1}..{y2}')

if __name__ == '__main__':
    main()
