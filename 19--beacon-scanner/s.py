import fileinput, collections, collections as cl, itertools, itertools as it, math, random, sys, re, string, functools
from grid import gridsource as grid, gridcustom # *, gridsource, gridcardinal, gridplane
from util import *
from matmul import matmul

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
        config = obj(
            overlap_needed = 3,
            rotate = rotate2d,
            count_rotations = 4,
        )
    elif dimensions == 3:
        config = obj(
            overlap_needed = 12,
            rotate = rotate3d,
            count_rotations = 24,
        )
    else:
        1/0  # invalid dim

    # print(find_overlap_of_scanners(scanners[0], scanners[1], config))
    print(find_overlapping_scanner(scanners, 0, [], config))
    print(find_overlapping_scanner(scanners, 1, [0, 3], config))


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

def rotate3d(point, r):
    '''
    r: Which rotation (0 - 23, inclusive)
    '''
    return to_tuple(matmul([point], rotations3d[r]))


# Maybe not needed -- a list probably
def to_tuple(row_matrix):
    return tuple(row_matrix[0])


# @trace
def find_overlap_of_scanners(s1, s2, config):
    rotate = config.rotate
    count_rotations = config.count_rotations
    overlap_needed = config.overlap_needed
    results = []
    for p1 in s1:
        for p2 in s2:
            for r in range(count_rotations):
                # Align p1 and p2
                n1 = center(s1, p1)
                n2 = center(s2, p2)

                # Rotate n2 by r
                n2 = [rotate(beacon, r) for beacon in n2]

                # Check for overlap
                if len(set(n1) & set(n2)) >= overlap_needed:
                    results.append( (True, p1, p2, r) )
    if results:
        return results[0]
    return (False,)


def find_overlapping_scanner(scanners, index, known_overlaps, config):
    rotate = config.rotate
    count_rotations = config.count_rotations
    overlap_needed = config.overlap_needed

    scanner = scanners[index]
    results = []
    for i, other_scanner in enumerate(scanners):
        if i == index or i in known_overlaps:
            continue
        has_overlap, *overlap_details = find_overlap_of_scanners(scanner, other_scanner, config)
        if has_overlap:
            results.append( (i, *overlap_details) )
    return results[0]
    1/0  # Every scanner is guaranteed to have some overlap


def center(scanner, origin_beacon):
    return [grid.subvec(beacon, origin_beacon) for beacon in scanner]







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
    main()
