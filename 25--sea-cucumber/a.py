import sys


def main():
    f = open(sys.argv[1] if len(sys.argv) > 1 else 'in')
    g = [list(l.rstrip('\n')) for l in f]

    progress = [list('..>.>...>..')]

    step = 1
    while True:
        g, rchanged = rstep(g)
        g, dchanged = dstep(g)
        if not rchanged and not dchanged:
            break
        step += 1

        if step % 50 == 0:
            progress, _ = rstep(progress)
        print(f'\rStep {step-1:3d} of ???   ' + ''.join(progress[0]), end='')
    print('\r' + 'Answer:'.ljust(50))
    print(step)


def rstep(g):
    width = len(g[0])
    moves = []
    for r, row in enumerate(g):
        for c, item in enumerate(row):
            if item == '>':
                nextpos = (r, (c + 1) % width)
                if getindex(g, nextpos) == '.':
                    moves.append(((r, c), nextpos))
    for old, new in moves:
        setindex(g, old, '.')
        setindex(g, new, '>')
    return g, bool(moves)

def dstep(g):
    height = len(g)
    moves = []
    for r, row in enumerate(g):
        for c, item in enumerate(row):
            if item == 'v':
                nextpos = ((r + 1) % height, c)
                if getindex(g, nextpos) == '.':
                    moves.append(((r, c), nextpos))
    for old, new in moves:
        setindex(g, old, '.')
        setindex(g, new, 'v')
    return g, bool(moves)


def getindex(mygrid, vec):
    for x in vec:
        mygrid = mygrid[x]
    return mygrid


def setindex(mygrid, vec, value):
    for x in vec[:-1]:
        mygrid = mygrid[x]
    mygrid[vec[-1]] = value


if __name__ == '__main__':
    main()
