import sys
from grid import gridsource as grid
from util import transpose
import heapq


def main():
    def neighbors(pos):
        for r, c in grid.neighbors(pos):
            if 0 <= r < height and 0 <= c < width:
                yield r, c

    def edge_cost(pos):
        return grid.getindex(g, pos)

    def is_goal(pos):
        r, c = pos
        return r == height - 1 and c == width - 1

    def bfs(node):
        visited.add(node)
        h = [(0, node)]
        heapq.heapify(h)
        while h:
            cumulative_cost, node = heapq.heappop(h)
            if is_goal(node):
                print(cumulative_cost)
                exit()
            for v in neighbors(node):
                if not v in visited:
                    visited.add(v)
                    heapq.heappush(h, (edge_cost(v) + cumulative_cost, v))


    # Parse
    f = open(sys.argv[1] if len(sys.argv) > 1 else 'in')
    lines = [l.rstrip('\n') for l in f]
    g = [[int(n) for n in line] for line in lines]

    height = len(g)
    width = len(g[0])

    visited = set()
    bfs((0, 0))


if __name__ == '__main__':
    main()
