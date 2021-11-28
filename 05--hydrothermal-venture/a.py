import sys, collections as cl
from grid import gridsource as grid
from util import findints


def main():
    f = open(sys.argv[1] if len(sys.argv) > 1 else 'in')
    lines = [l.rstrip('\n') for l in f]
    counts = cl.Counter()
    for line in lines:
        x1,y1,x2,y2 = findints(line)
        if x1 == x2 or y1 == y2:
            v = grid.subvec((x2,y2),(x1,y1))
            mag = grid.absmanhattan(v)
            v = grid.floordivvec(v, mag)
            curr = (x1,y1)
            while curr != (x2, y2):
                counts[(curr)] += 1
                curr = grid.addvec(curr, v)
            counts[(curr)] += 1
    total = 0
    for point, count in counts.items():
        if count >= 2:
            total += 1
    print(total)


if __name__ == '__main__':
    main()
