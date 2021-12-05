import sys
from util import findints


def main():
    f = open(sys.argv[1] if len(sys.argv) > 1 else 'in')
    xs = findints(f.read())
    def fuel(dest):
        return sum(abs(x - dest) for x in xs)
    candidates = range(min(xs), max(xs)+1)
    print(min(fuel(d) for d in candidates))

if __name__ == '__main__':
    main()
