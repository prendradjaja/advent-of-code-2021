'''
I used this code to generate rotation matrices. None of these functions are
called from my solution program, but I'd be sad deleting them.

(Actual matrices aren't anywhere in the final version of my solution anymore
either -- I optimized to "rotator" functions.)

There is a much simpler way to generate the 3d matrices, actually:

  - Generate 48 matrices ("signed permutations")

  - Half of these matrices are impossible to achieve with only rotations
    (they require reflections). These have determinant -1. The other 24 have
    determinant 1. These are the ones we want.
'''


import itertools


def main():
    m0 = [
        [1, 0],
        [0, 1],
    ]
    m90 = [
        [0, 1],
        [-1, 0],
    ]

    generate_rotations_2d(m0, m90)
    generate_rotations_3d()


# Copied from https://stackoverflow.com/a/48597323/1945088
def matmul(a,b):
    c = []
    for i in range(0,len(a)):
        temp=[]
        for j in range(0,len(b[0])):
            s = 0
            for k in range(0,len(a[0])):
                s += a[i][k]*b[k][j]
            temp.append(s)
        c.append(temp)
    return c


def generate_rotations_2d(m0, m90, *, end='\n'):
    m = m0
    print(m)
    for _ in range(3):
        m = matmul(m, m90)
        print(m)


def generate_rotations_3d():
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

    # I don't know what any of the sign/coordinate conventions are. It doesn't
    # really matter for this purpose (generating all 24 rotations instead of
    # just a specific one / the order they're generated doesn't matter) if I
    # have standard conventions -- just need to pick my own and be consistent
    # in order to make sure I generate all 24.
    #
    # The convention I'll use is below (colors referring to a Rubik's cube
    # with the "Western" color scheme)
    #
    # x = red/orange axis
    # y = white/yellow axis
    # z = blue/green axis

    # white top
    m = m0
    generate_rotations_2d(m, mY, end='')

    # green top
    m = matmul(m, mX)
    generate_rotations_2d(m, mY, end='')

    # red top
    m = matmul(m, mZ)
    generate_rotations_2d(m, mY, end='')

    # blue top
    m = matmul(m, mZ)
    generate_rotations_2d(m, mY, end='')

    # orange top
    m = matmul(m, mZ)
    generate_rotations_2d(m, mY, end='')

    # yellow top
    m = matmul(m, mX)
    generate_rotations_2d(m, mY, end='')


if __name__ == '__main__':
    main()
