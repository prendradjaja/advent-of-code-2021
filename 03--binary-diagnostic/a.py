import sys
import collections as cl
from util import transpose


def main():
    f = open(sys.argv[1] if len(sys.argv) > 1 else 'in')
    lines = [l.rstrip('\n') for l in f]
    m = transpose(lines)
    g = ''
    e = ''
    for row in m:
        gbit = cl.Counter(row).most_common(1)[0][0]
        ebit = other(gbit)
        g += gbit
        e += ebit
    gamma = int(g, 2)
    epsilon = int(e, 2)
    print(gamma * epsilon)

def other(s):
    return '0' if s == '1' else '1'

if __name__ == '__main__':
    main()
