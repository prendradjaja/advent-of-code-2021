import sys, collections
from grid import gridsource as grid
from util import findints


Target = collections.namedtuple('Target', 'xmin xmax ymin ymax')


def main():
    f = open(sys.argv[1] if len(sys.argv) > 1 else 'in')
    target = Target(*findints(f.read()))

    result = 0
    for xvel in inclusive_range(0, target.xmax):
        for yvel in inclusive_range(target.ymin, -target.ymin - 1):
            if is_hit((xvel, yvel), target):
                result += 1
    print(result)


def inclusive_range(lo, hi):
    return range(lo, hi + 1)


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


if __name__ == '__main__':
    main()
