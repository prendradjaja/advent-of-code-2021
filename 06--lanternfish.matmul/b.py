import sys
from matmul import matmul


# TODO Try this with NumPy


_ = 0  # So it's easy to see where the 1s are

step = [
    # If you multiply a 1x9 vector (v) with this 9x9 matrix, you get a new 1x9
    # vector (w)
    #
    # Each column represents a new value (= column) in the new vector. Do some
    # example matrix multiplication to get an intuition for this.
    #
    #*-- This column means w[1] = v[0]
    #|  *-- means w[2] = v[1]
    #|  |              *-- means w[6] = v[0] + v[7]
    #v  v              v
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


def main():
    f = open(sys.argv[1] if len(sys.argv) > 1 else 'in')

    counts = [0] * 9
    for n in f.read().split(','):
        counts[int(n)] += 1

    v = [counts]
    for _ in range(256):
        v = matmul(v, step)

    counts = v[0]
    print(sum(counts))


if __name__ == '__main__':
    main()
