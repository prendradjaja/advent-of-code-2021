import sys, functools
from grid import gridsource as grid


BOARD_SIZE = 10
MAX_SCORE = 21

# qdie[total] = count means: Rolling a qdie three times results in COUNT (out
# of 27) branched universes having a total roll of TOTAL
qdie = {
    3: 1,
    4: 3,
    5: 6,
    6: 7,
    7: 6,
    8: 3,
    9: 1,
}


def main():
    f = open(sys.argv[-1] if len(sys.argv) > 1 and sys.argv[-1] != '-' else 'in')
    lines = [l.rstrip('\n') for l in f]
    positions = tuple(int(line.split()[-1]) for line in lines)
    player = 0
    scores = (0, 0)
    print(max(count_wins(player, scores, positions)))


@functools.cache
def count_wins(player, scores, positions):
    if scores[0] >= MAX_SCORE:
        return [1, 0]
    elif scores[1] >= MAX_SCORE:
        return [0, 1]

    result = [0, 0]
    for rolltotal, rollcount in qdie.items():
        next_state = turn(player, scores, positions, rolltotal)
        sub_result = count_wins(*next_state)
        sub_result = grid.mulvec(sub_result, rollcount)
        result = grid.addvec(result, sub_result)
    return result


def turn(player, scores, positions, rollsum):
    scores = list(scores)
    positions = list(positions)

    # move forward
    positions[player] += rollsum
    positions[player] %= 10
    if positions[player] == 0:
        positions[player] = 10

    scores[player] += positions[player]
    player = int(not player)

    return player, tuple(scores), tuple(positions)


if __name__ == '__main__':
    main()
