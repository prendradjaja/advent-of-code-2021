import sys
from matmul import matmul


_ = 0  # So it's easy to see where the 1s are

step = [
    # See ../06--lanternfish.matmul/b.py notes about this matrix
    [_, _, _, _, _, _, 1, _, 1],
    [1, _, _, _, _, _, _, _, _],
    [_, 1, _, _, _, _, _, _, _],
    [_, _, 1, _, _, _, _, _, _],
    [_, _, _, 1, _, _, _, _, _],
    [_, _, _, _, 1, _, _, _, _],
    [_, _, _, _, _, 1, _, _, _],
    [_, _, _, _, _, _, 1, _, _],
    [_, _, _, _, _, _, _, 1, _],
]


i9 = [
    [1, _, _, _, _, _, _, _, _],
    [_, 1, _, _, _, _, _, _, _],
    [_, _, 1, _, _, _, _, _, _],
    [_, _, _, 1, _, _, _, _, _],
    [_, _, _, _, 1, _, _, _, _],
    [_, _, _, _, _, 1, _, _, _],
    [_, _, _, _, _, _, 1, _, _],
    [_, _, _, _, _, _, _, 1, _],
    [_, _, _, _, _, _, _, _, 1],
]


def main():
    simulation_length = 1000 * 1000

    f = open(sys.argv[1] if len(sys.argv) > 1 else 'in')
    counts = [0] * 9
    for n in f.read().split(','):
        counts[int(n)] += 1
    v = [counts]

    v = matmul(v, matexp(step, simulation_length))

    counts = v[0]
    print('Number of days: ', f'{simulation_length:,}')
    print('Answer mod 1000:', sum(counts) % 1000)


def matexp(m, n):
    binary = bin(n)[2:]
    res = i9
    for i, bit in enumerate(reversed(binary)):
        if bit == '1':
            res = matmul(res, m)
        m = matmul(m, m)

        # mod 1000
        m2 = []
        for row in m:
            row2 = [item % 1000 for item in row]
            m2.append(row2)
        m = m2
    return res


if __name__ == '__main__':
    main()
