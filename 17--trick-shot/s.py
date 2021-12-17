import fileinput, collections, collections as cl, itertools, itertools as it, math, random, sys, re, string, functools
from grid import gridsource as grid, gridcustom # *, gridsource, gridcardinal, gridplane
from util import *


Target = collections.namedtuple('Target', 'xmin xmax ymin ymax')
# Velocity and Position are both (x, y)

# 17, 113 is a hit


def main():
    f = open(sys.argv[1] if len(sys.argv) > 1 else 'in')
    t = Target(*findints(f.read()))
    for xv in range(t.xmax + 3):
        for yv in range(t.ymin - 3, -t.ymin + 3):
            v = (xv, yv)
            if is_hit(v, t):
                print(v)

def show(velocity, target):
    pixels = {}
    window = obj(xmin=0, xmax=target.xmax, ymin=target.ymin, ymax=0)
    for x in range(target.xmin, target.xmax + 1):
        for y in range(target.ymin, target.ymax + 1):
            pixels[(x, y)] = 'T'
    for pos in trajectory(velocity, target):
        x, y = pos
        pixels[pos] = '#'
        window.ymax = max(window.ymax, y)

    pixels[(0, 0)] = 'S'

    # window.ymin = target.ymin
    # window.ymax = target.ymax + 10
    # window.xmin = target.xmin - 30
    # window.xmax = target.xmax

    window.ymax = 20

    for y in range(window.ymax, window.ymin - 1, -1):
        line = ''
        for x in range(window.xmin, window.xmax + 1):
            line += pixels.get((x, y), '.')
        print(line)



def is_hit(velocity, target):
    for pos in trajectory(velocity, target):
        if (
            target.xmin <= pos[0] <= target.xmax and
            target.ymin <= pos[1] <= target.ymax
        ):
            return True
    return False


def trajectory(velocity, target):
    pos = (0, 0)
    while pos[0] <= target.xmax and pos[1] >= target.ymin:
        yield pos
        pos = grid.addvec(pos, velocity)
        velocity = (
            max(0, velocity[0] - 1),
            velocity[1] - 1
        )


def min_xvel(target_xmin):
    '''
    In order to reach 7, an initial velocity of 3 is insufficient: the
    farthest distance that can be reached is 3 + 2 + 1 = 6. But 4 works: 4 + 3
    + 2 + 1 = 10 >= 7.
    >>> min_xvel(7)
    4
    >>> min_xvel(6)
    3

    More test cases
    >>> min_xvel(1)
    1
    >>> min_xvel(2)
    2
    >>> min_xvel(3)
    2
    >>> min_xvel(4)
    3
    '''
    for i, n in enumerate(triangulars):
        if n >= target_xmin:
            return i


triangulars = [0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153, 171, 190, 210, 231, 253, 276, 300, 325, 351, 378, 406, 435, 465, 496]

if __name__ == '__main__':
    main()
