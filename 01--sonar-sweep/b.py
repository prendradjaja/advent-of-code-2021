import sys
from util import consecutives


def main():
    f = open(sys.argv[1] if len(sys.argv) > 1 else 'in')
    values = [int(l.rstrip('\n')) for l in f]
    res = 0
    windows = consecutives(values, 3)
    for prev, curr in consecutives(windows):
        if sum(curr) > sum(prev):
            res += 1
    print(res)

if __name__ == '__main__':
    main()
