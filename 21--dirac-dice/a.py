import sys, functools, collections, itertools
from grid import gridsource as grid


BOARD_SIZE = 10
MAX_SCORE = 1000


def main():
    f = open(sys.argv[-1] if len(sys.argv) > 1 and sys.argv[-1] != '-' else 'in')
    lines = [l.rstrip('\n') for l in f]
    positions = [int(line.split()[-1]) for line in lines]
    player = 0
    scores = [0, 0]
    roll = make_deterministic_die()
    while scores[0] < MAX_SCORE and scores[1] < MAX_SCORE:
        for _ in range(3):
            positions[player] += roll()
            positions[player] %= 10
            if positions[player] == 0:
                positions[player] = 10
        scores[player] += positions[player]
        player = int(not player)
    print(min(scores) * roll.roll_count)


def make_deterministic_die():
    values = itertools.cycle(range(1, 100+1))
    def roll():
        roll.roll_count += 1
        return next(values)
    roll.roll_count = 0
    return roll


if __name__ == '__main__':
    main()
