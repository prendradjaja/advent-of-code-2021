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
    # Exponentiation by squaring:
    #
    # m^n can be decomposed into factors of the form m^(2^p).
    #
    # To see this, consider the binary representation of n. For example, if n
    # = 37, then:
    #
    #     37 = 0b100101
    #
    #     m^37 = m^32    * m^4     * m^1
    #     m^37 = m^(2^5) * m^(2^2) * m^(2^0)
    #
    # We can generate these factors sequentially by repeatedly squaring m:
    #
    #     p=0: m         = m^1 = m^(2^0)
    #     p=1: m * m     = m^2 = m^(2^1)
    #     p=2: m^2 * m^2 = m^4 = m^(2^2)
    #     p=3: m^4 * m^4 = m^8 = m^(2^3)
    #     ... (as many as needed)
    binary = bin(n)[2:]
    res = i9
    for i, bit in enumerate(reversed(binary)):
        if bit == '1':
            res = matmul(res, m)
        m = matmul(m, m)
    return res


if __name__ == '__main__':
    main()
