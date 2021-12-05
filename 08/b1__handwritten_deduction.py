import sys
import util


def solve(patterns_seen):
    patterns_seen = [sort_string(p) for p in patterns_seen]
    assignments = {}

    # *** can identify 1478
    one = util.one([p for p in patterns_seen if len(p) == 2])
    four = util.one([p for p in patterns_seen if len(p) == 4])
    seven = util.one([p for p in patterns_seen if len(p) == 3])
    eight = util.one([p for p in patterns_seen if len(p) == 7])

    # *** A (7-1)
    A = util.one(set(seven) - set(one))
    assignments[A] = 'A'

    # *** G (9-(7+4)) -- can identify 9 because it contains 4
    nine = util.one([p for p in patterns_seen if len(p) == 6 and set(p) > set(four)])
    G = util.one(set(nine) - (set(seven) | set(four)))
    assignments[G] = 'G'

    # *** E (8-9)
    E = util.one(set(eight) - set(nine))
    assignments[E] = 'E'

    # *** B (8-3-E) -- can identify 3 because it contains 1
    three = util.one([p for p in patterns_seen if len(p) == 5 and set(p) > set(one)])
    B = util.one(set(eight) - set(three) - {E})
    assignments[B] = 'B'

    # *** D (8-0) -- can identify 0 because it contains 1 and is not 9
    zero = util.one([p for p in patterns_seen if len(p) == 6 and set(p) > set(one) and p != nine])
    D = util.one(set(eight) - set(zero))
    assignments[D] = 'D'

    # *** C (8-6) -- can identify 6 because its not 0 or 9
    six = util.one([p for p in patterns_seen if len(p) == 6 and p != nine and p != zero])
    C = util.one(set(eight) - set(six))
    assignments[C] = 'C'

    # *** F -- it's the last one
    F = util.one(set('abcdefg') - set(assignments))
    assignments[F] = 'F'

    return assignments


def sort_string(s):
    return ''.join(sorted(s))
