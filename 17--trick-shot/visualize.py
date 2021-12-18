import sys, collections
from grid import gridsource as grid
from types import SimpleNamespace as obj


def show(velocity, target, *, background='.'):
    '''
    >>> Target = collections.namedtuple('Target', 'xmin xmax ymin ymax')
    >>> velocity = (6,2)
    >>> target = Target(20, 30, -4, -2)
    >>> show(velocity, target, background='`')
    ```````````#```#```````````````
    ``````#```````````#````````````
    ```````````````````````````````
    S```````````````````#``````````
    ```````````````````````````````
    ````````````````````TTTTTTTTTTT
    ````````````````````T#TTTTTTTTT
    ````````````````````TTTTTTTTTTT

    Background parameter is optional. I only added it because lines starting
    with '...' break doctest parsing.
    '''
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

    for y in range(window.ymax, window.ymin - 1, -1):
        line = ''
        for x in range(window.xmin, window.xmax + 1):
            line += pixels.get((x, y), background)
        print(line)


def trajectory(velocity, target):
    pos = (0, 0)
    while pos[0] <= target.xmax and pos[1] >= target.ymin:
        yield pos
        pos = grid.addvec(pos, velocity)
        velocity = (
            max(0, velocity[0] - 1),
            velocity[1] - 1
        )
