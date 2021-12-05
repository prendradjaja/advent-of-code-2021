import sys


def main():
    f = open(sys.argv[1] if len(sys.argv) > 1 else 'in')

    counts = [0] * 9
    for n in f.read().split(','):
        counts[int(n)] += 1

    for _ in range(256):
        births, *counts = counts + [0]
        counts[6] += births
        counts[8] += births

    print(sum(counts))


if __name__ == '__main__':
    main()
