import sys
from util import findints


def main():
    f = open(sys.argv[1] if len(sys.argv) > 1 else 'in')
    xs = findints(f.read())
    def fuel(dest):
        return sum(triangle(abs(x - dest)) for x in xs)
    candidates = range(min(xs), max(xs)+1)
    print(min(fuel(d) for d in candidates))

def triangle(n):
    return n * (n + 1) // 2

# @functools.cache
# def triangle(n):
#     if n == 0:
#         return 0
#     return n + triangle(n - 1)
# sys.setrecursionlimit(3000)

if __name__ == '__main__':
    main()
