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

    result = 0
    for r, line in enumerate(lines):
        for c, value in enumerate(line):
            if is_low_point((r, c)):
                value = int(lines[r][c])
                result += 1 + value
    print(result)


if __name__ == '__main__':
    main()
