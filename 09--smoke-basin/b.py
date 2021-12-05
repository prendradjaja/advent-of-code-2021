import sys
from grid import gridsource as grid


def main():
    f = open(sys.argv[1] if len(sys.argv) > 1 else 'in')
    lines = [l.rstrip('\n') for l in f]
    height = len(lines)
    width = len(lines[0])

    def neighbors(pos):
        for d in grid.directions:
            npos = grid.addvec(pos, d)
            r, c = npos
            if 0 <= r < height and 0 <= c < width:
                yield npos

    def is_low_point(pos):
        r, c = pos
        value = int(lines[r][c])
        for npos in neighbors(pos):
            r, c = npos
            nval = int(lines[r][c])
            if nval <= value:
                return False
        return True

    low_points = []
    for r, line in enumerate(lines):
        for c, value in enumerate(line):
            if is_low_point((r, c)):
                low_points.append((r, c))

    def dfs(pos):
        if pos in visited:
            return
        visited.add(pos)
        for neighbor in neighbors(pos):
            r, c = neighbor
            pos_val = int(grid.index(lines, pos))
            neighbor_val = int(grid.index(lines, neighbor))
            # I wasn't sure if this should be >= or >. Seemed unclear to me
            # from the prompt. Turns out both work.
            if neighbor_val >= pos_val and neighbor_val != 9:
                dfs(neighbor)

    basin_sizes = []
    for pos in low_points:
        visited = set()
        dfs(pos)
        basin_sizes.append(len(visited))
    basin_sizes.sort()

    a, b, c = basin_sizes[-3:]
    print(a * b * c)


if __name__ == '__main__':
    main()
