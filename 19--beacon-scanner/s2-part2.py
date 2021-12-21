import sys
import itertools
import collections
import ast
from s import parse_section, rotators
from grid import gridsource as grid, gridcustom # *, gridsource, gridcardinal, gridplane


def main():
    assert len(sys.argv) == 3
    _, inputfile, step1file = sys.argv
    inputfile = open(inputfile)
    step1file = open(step1file)

    sections = inputfile.read().strip().split('\n\n')
    scanners = [parse_section(s) for s in sections]
    dimensions = len(scanners[0][0])

    print()

    sky = set()

    # (scanner, (x, y, z)) => (x, y, z)
    partials = collections.defaultdict(set)
    for s, scanner in enumerate(scanners):
        for beacon in [(0, 0, 0)]:
            partials[s].add(beacon)

    for line in reversed(step1file.readlines()):
        line = line.rstrip('\n')
        *line, last_word = line.split()
        line = ' '.join(line)
        b, apoint, bpoint, r, _ = ast.literal_eval(line)
        a = int(last_word)

        for beacon in partials[b]:
            # translate
            beacon = grid.addvec(beacon, grid.subvec(apoint, bpoint))
            # rotate
            beacon = rotate_around(beacon, apoint, r)
            partials[a].add(beacon)
        # print(a, b, len(partials[a]))
    scanner_locations = list(partials[0])
    # print(scanner_locations)
    print(max(grid.manhattan(a, b) for a, b in itertools.combinations(scanner_locations, 2)))


        # print('\n' * 10)

        # return

        # adjusted = beacon for beacon in scanners[b]




def rotate_around(point, center, r):
    '''
    >>> rotate_around((1001, 1002, 0), (1000, 1000, 0), 9)
    (1002, 999, 0)
    '''
    move_to_origin = grid.subvec((0, 0, 0), center)
    _ = point
    _ = grid.addvec(_, move_to_origin)
    _ = rotators[r](_)
    _ = grid.subvec(_, move_to_origin)
    return _


if __name__ == '__main__':
    main()
