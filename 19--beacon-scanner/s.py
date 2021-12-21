import fileinput, collections, collections as cl, itertools, itertools as it, math, random, sys, re, string, functools
from grid import gridsource as grid, gridcustom # *, gridsource, gridcardinal, gridplane
from util import *
from matmul import matmul
import cProfile
import pstats

PROFILE = False

def trace(f):
    def traced(*args, **kwargs):
        result = f(*args, **kwargs)
        print('args', args)
        print('kwargs', kwargs)
        print('result', result)
        print()
        return result
    return traced

rotations2d = [
    [[1, 0],
     [0, 1]],
    [[0, 1],
     [-1, 0]],
    [[-1, 0],
     [0, -1]],
    [[0, -1],
     [1, 0]],
]

rotations3d = [
[[1, 0, 0], [0, 1, 0], [0, 0, 1]],
[[0, 0, 1], [0, 1, 0], [-1, 0, 0]],
[[-1, 0, 0], [0, 1, 0], [0, 0, -1]],
[[0, 0, -1], [0, 1, 0], [1, 0, 0]],
[[1, 0, 0], [0, 0, 1], [0, -1, 0]],
[[0, 0, 1], [-1, 0, 0], [0, -1, 0]],
[[-1, 0, 0], [0, 0, -1], [0, -1, 0]],
[[0, 0, -1], [1, 0, 0], [0, -1, 0]],
[[0, 1, 0], [0, 0, 1], [1, 0, 0]],
[[0, 1, 0], [-1, 0, 0], [0, 0, 1]],
[[0, 1, 0], [0, 0, -1], [-1, 0, 0]],
[[0, 1, 0], [1, 0, 0], [0, 0, -1]],
[[-1, 0, 0], [0, 0, 1], [0, 1, 0]],
[[0, 0, -1], [-1, 0, 0], [0, 1, 0]],
[[1, 0, 0], [0, 0, -1], [0, 1, 0]],
[[0, 0, 1], [1, 0, 0], [0, 1, 0]],
[[0, -1, 0], [0, 0, 1], [-1, 0, 0]],
[[0, -1, 0], [-1, 0, 0], [0, 0, -1]],
[[0, -1, 0], [0, 0, -1], [1, 0, 0]],
[[0, -1, 0], [1, 0, 0], [0, 0, 1]],
[[0, 0, -1], [0, -1, 0], [-1, 0, 0]],
[[1, 0, 0], [0, -1, 0], [0, 0, -1]],
[[0, 0, 1], [0, -1, 0], [1, 0, 0]],
[[-1, 0, 0], [0, -1, 0], [0, 0, 1]],
]

def main():
    f = open(sys.argv[-1] if len(sys.argv) > 1 and sys.argv[-1] != '-' else 'in')
    # rotations_demo()
    # exit()

    sections = f.read().strip().split('\n\n')
    scanners = [parse_section(s) for s in sections]
    dimensions = len(scanners[0][0])
    if dimensions == 2:
        1/0  # can't do 2dim now
        # config = obj(
        #     overlap_needed = 3,
        #     rotate = rotate2d,
        #     count_rotations = 4,
        # )
    elif dimensions == 3:
        config = obj(
            overlap_needed = 12,
            rotate = rotate3d,
            count_rotations = 24,
        )
    else:
        1/0  # invalid dim

    # print(find_overlap_of_scanners(scanners[0], scanners[1], config))
    # print(find_overlapping_scanner(scanners, 0, [], config))
    # print(find_overlapping_scanner(scanners, 1, [0, 3], config))

    visited = set()
    g = Graph()
    try:
        dfs(0, None, scanners, config, g, visited)
    except SearchDone:
        print('done')


class Graph:
    def __init__(self):
        self.vertices = set()
        self.neighbors = collections.defaultdict(set)


    def add_vertex(self, v):
        self.vertices.add(v)


    def add_edge(self, v, w):
        self.add_vertex(v)
        self.add_vertex(w)
        self.neighbors[v].add(w)
        self.neighbors[w].add(v)


# (first set every visited flag to false)
def dfs(u, parent, scanners, config, g, visited):
    # if parent:
    #     g.add_edge(u, parent)
    visited.add(u)
    for v in neighbors(u, scanners, config, g):
        if v not in visited:
            dfs(v, u, scanners, config, g, visited)


def neighbors(u, scanners, config, g):
    known_overlaps = list(g.neighbors[u])
    known_no_overlaps = []
    while True:
        has_overlap, *details = find_overlapping_scanner(scanners, u, known_overlaps + known_no_overlaps, config)
        if has_overlap:
            print(details, u)
            neighbor, *details, new_no_overlaps = details
            known_no_overlaps.extend(new_no_overlaps)
            known_overlaps.append(neighbor)
            g.add_edge(u, neighbor)
            if len(g.vertices) == len(scanners):
                raise SearchDone
            yield neighbor
            known_overlaps = list(set(known_overlaps) | set(g.neighbors[u]))
        else:
            break


class SearchDone(Exception):
    pass



def parse_section(section):
    section = section.split('\n')[1:]
    result = []
    for line in section:
        result.append(tuple(int(n) for n in line.split(',')))
    return result


def rotate2d(point, r):
    '''
    r: Which rotation (0 - 3, inclusive)
    >>> tuple(rotate2d((4, 1), 1))
    (-1, 4)
    '''
    return to_tuple(matmul([point], rotations2d[r]))
    # return matmul([point], rotations2d[r])[0]

rotators = {
    0:  lambda point: (point[0], point[1], point[2]),
    1:  lambda point: (point[2], point[1], -point[0]),
    2:  lambda point: (-point[0], point[1], -point[2]),
    3:  lambda point: (-point[2], point[1], point[0]),
    4:  lambda point: (point[0], point[2], -point[1]),
    5:  lambda point: (point[2], -point[0], -point[1]),
    6:  lambda point: (-point[0], -point[2], -point[1]),
    7:  lambda point: (-point[2], point[0], -point[1]),
    8:  lambda point: (point[1], point[2], point[0]),
    9:  lambda point: (point[1], -point[0], point[2]),
    10: lambda point: (point[1], -point[2], -point[0]),
    11: lambda point: (point[1], point[0], -point[2]),
    12: lambda point: (-point[0], point[2], point[1]),
    13: lambda point: (-point[2], -point[0], point[1]),
    14: lambda point: (point[0], -point[2], point[1]),
    15: lambda point: (point[2], point[0], point[1]),
    16: lambda point: (-point[1], point[2], -point[0]),
    17: lambda point: (-point[1], -point[0], -point[2]),
    18: lambda point: (-point[1], -point[2], point[0]),
    19: lambda point: (-point[1], point[0], point[2]),
    20: lambda point: (-point[2], -point[1], -point[0]),
    21: lambda point: (point[0], -point[1], -point[2]),
    22: lambda point: (point[2], -point[1], point[0]),
    23: lambda point: (-point[0], -point[1], point[2]),
}

def rotate3d(point, r):
    '''
    r: Which rotation (0 - 23, inclusive)
    '''
    x, y, z = point
    if r == 0:
        return (x, y, z)
    elif r == 1:
        return (z, y, -x)
    elif r == 2:
        return (-x, y, -z)
    elif r == 3:
        return (-z, y, x)
    elif r == 4:
        return (x, z, -y)
    elif r == 5:
        return (z, -x, -y)
    elif r == 6:
        return (-x, -z, -y)
    elif r == 7:
        return (-z, x, -y)
    elif r == 8:
        return (y, z, x)
    elif r == 9:
        return (y, -x, z)
    elif r == 10:
        return (y, -z, -x)
    elif r == 11:
        return (y, x, -z)
    elif r == 12:
        return (-x, z, y)
    elif r == 13:
        return (-z, -x, y)
    elif r == 14:
        return (x, -z, y)
    elif r == 15:
        return (z, x, y)
    elif r == 16:
        return (-y, z, -x)
    elif r == 17:
        return (-y, -x, -z)
    elif r == 18:
        return (-y, -z, x)
    elif r == 19:
        return (-y, x, z)
    elif r == 20:
        return (-z, -y, -x)
    elif r == 21:
        return (x, -y, -z)
    elif r == 22:
        return (z, -y, x)
    elif r == 23:
        return (-x, -y, z)
    else:
        1/0


# Maybe not needed -- a list probably
def to_tuple(row_matrix):
    return tuple(row_matrix[0])


# @trace
def find_overlap_of_scanners(s1, s2, config):
    # rotate = config.rotate
    count_rotations = config.count_rotations
    overlap_needed = config.overlap_needed
    for p1 in s1:
        for p2 in s2:
            for r in range(count_rotations):
                rotate = rotators[r]
                # Align p1 and p2
                n1 = center(s1, p1)
                n2 = center(s2, p2)

                # Rotate n2 by r
                n2 = [rotate(beacon) for beacon in n2]

                # Check for overlap
                if len(set(n1) & set(n2)) >= overlap_needed:
                    return( (True, p1, p2, r) )
    return (False,)


def find_overlapping_scanner(scanners, index, skip, config):
    rotate = config.rotate
    count_rotations = config.count_rotations
    overlap_needed = config.overlap_needed

    scanner = scanners[index]
    no_overlap = []
    for i, other_scanner in enumerate(scanners):
        if i == index or i in skip:
            continue
        has_overlap, *overlap_details = find_overlap_of_scanners(scanner, other_scanner, config)
        if has_overlap:
            return( (True, i, *overlap_details, no_overlap) )
        else:
            no_overlap.append(i)
    return (False,)


def subvec3d(a, b):
    ax, ay, az = a
    bx, by, bz = b
    return (ax-bx, ay-by, az-bz)

def center(scanner, origin_beacon):
    return [subvec3d(beacon, origin_beacon) for beacon in scanner]







def showmat(m, *, trailing_comma='', end='\n'):
    '''
    >>> m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    >>> showmat(m)
    [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
    '''
    print('[', m[0], ',', sep='', end=end)
    for row in m[1:-1]:
        print(' ', row, ',', sep='', end=end)
    print(' ', m[-1], ']', trailing_comma, sep='')

def rotations_demo():
    m0 = [
        [1, 0],
        [0, 1],
    ]
    m90 = [
        [0, 1],
        [-1, 0],
    ]
    generate_rotations2d(m0, m90)
    generate_rotations3d()

def generate_rotations2d(m0, m90, *, end='\n'):
    m = m0
    showmat(m, trailing_comma=',', end=end)
    for _ in range(3):
        m = matmul(m, m90)
        showmat(m, trailing_comma=',', end=end)

def generate_rotations3d():
    m0 = [
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1],
    ]
    mX = [
        [1, 0, 0],
        [0, 0, 1],
        [0, -1, 0],
    ]
    mY = [
        [0, 0, 1],
        [0, 1, 0],
        [-1, 0, 0],
    ]
    mZ = [
        [0, 1, 0],
        [-1, 0, 0],
        [0, 0, 1],
    ]

    # x = red
    # y = white
    # z = blue

    # white top
    m = m0
    generate_rotations2d(m, mY, end='')

    # green top
    m = matmul(m, mX)
    generate_rotations2d(m, mY, end='')

    # red top
    m = matmul(m, mZ)
    generate_rotations2d(m, mY, end='')

    # blue top
    m = matmul(m, mZ)
    generate_rotations2d(m, mY, end='')

    # orange top
    m = matmul(m, mZ)
    generate_rotations2d(m, mY, end='')

    # yellow top
    m = matmul(m, mX)
    generate_rotations2d(m, mY, end='')




if __name__ == '__main__':
    if PROFILE:
        with cProfile.Profile() as pr:
            main()
        stats = pstats.Stats(pr)
        stats.sort_stats(pstats.SortKey.TIME)
        stats.print_stats()
        stats.dump_stats(filename='myprof.prof')
    else:
        main()
