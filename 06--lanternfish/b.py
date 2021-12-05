import sys
from collections import Counter


def main():
    f = open(sys.argv[1] if len(sys.argv) > 1 else 'in')
    counter = Counter(int(n) for n in f.read().split(','))
    counts = [counter[i] for i in range(9)]

    def step():
        nonlocal counts
        births, *rest = counts
        new_counts = [get(rest, i) for i in range(9)]
        new_counts[6] += births
        new_counts[8] += births
        counts = new_counts

    for _ in range(256):
        step()

    print(sum(counts))


def get(lst, idx):
    if idx < len(lst):
        return lst[idx]
    else:
        return 0


if __name__ == '__main__':
    main()
