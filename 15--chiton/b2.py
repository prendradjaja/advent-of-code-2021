'''
An alternate solution using Dijkstra's algorithm from a library.
'''

import sys
from grid import gridsource as grid
from util import transpose
import heapq

from dijkstra_gribouillis import Dijkstra


def main():
    def neighbors(pos):
        for r, c in grid.neighbors(pos):
            if 0 <= r < height and 0 <= c < width:
                distance = g[r][c]
                node = r, c
                edge = None
                yield (distance, node, edge)

    # Parse
    f = open(sys.argv[1] if len(sys.argv) > 1 else 'in')
    lines = [l.rstrip('\n') for l in f]
    g = [[int(n) for n in line] for line in lines]

    g = embiggen(g)

    height = len(g)
    width = len(g[0])

    target = (height - 1, width - 1)
    start = (0, 0)

    d = Dijkstra(
        start,
        neighbors,
        maxitems=None,
        maxdist=None,
        target=target
    )
    assert d.is_shortest(target)
    print(d[target].dist)


def embiggen(g, factor=5):
    _ = g
    _ = [embiggen_horizontally(row, factor) for row in _]
    _ = transpose(_)
    _ = [embiggen_horizontally(row, factor) for row in _]
    _ = transpose(_)
    return _


def embiggen_horizontally(row, factor):
    result = []
    for i in range(factor):
        result.extend([multi_increment(x, i) for x in row])
    return result


def increment(n):
    return n + 1 if n < 9 else 1


def multi_increment(n, x):
    for _ in range(x):
        n = increment(n)
    return n


if __name__ == '__main__':
    main()
