import sys
from util import findints


def main():
    f = open(sys.argv[-1] if len(sys.argv) > 1 and sys.argv[-1] != '-' else 'in')
    lines = [l.rstrip('\n') for l in f]

    on = set()
    for line in lines:
        cmd, *region = parse_line(line)
        xlo, xhi, ylo, yhi, zlo, zhi = region
        if not excludes_initialization_area(region):
            for x in range(xlo, xhi+1):
                for y in range(ylo, yhi+1):
                    for z in range(zlo, zhi+1):
                        pos = x, y, z
                        if cmd == 'on':
                            on.add(pos)
                        elif cmd == 'off':
                            on.discard(pos)
    print(len(on))


def parse_line(line):
    cmd, rest = line.split(' ')
    assert cmd in ['on', 'off']
    return cmd, *findints(rest)


def excludes_initialization_area(region):
    xlo, xhi, ylo, yhi, zlo, zhi = region
    return (
        xlo < xhi < -50 or
        ylo < yhi < -50 or
        zlo < zhi < -50 or
        xhi > xlo > 50 or
        yhi > ylo > 50 or
        zhi > zlo > 50
    )


if __name__ == '__main__':
    main()
