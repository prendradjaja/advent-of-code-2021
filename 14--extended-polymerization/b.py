import sys
from collections import Counter
from util import consecutives


def main():
    f = open(sys.argv[1] if len(sys.argv) > 1 else 'in')
    polymer, rules = f.read().strip().split('\n\n')
    polymer = polymer.strip()
    rules = rules.strip().split('\n')
    rules = dict(rule.split(' -> ') for rule in rules)

    first, *_, last = polymer

    pair_counts = Counter(consecutives(polymer, string=True))
    for step in range(40):
        pair_counts = iterate(pair_counts, rules)

    hi, *_, lo = to_element_counts(pair_counts, first, last).most_common()

    hi_name, hi_count = hi
    lo_name, lo_count = lo
    print(hi_count - lo_count)


def iterate(pair_counts, rules):
    new_pair_counts = Counter()
    for pair, count in pair_counts.items():
        if pair in rules:
            a, c = pair
            b = rules[pair]
            new_pair_counts[a + b] += count
            new_pair_counts[b + c] += count
        else:
            new_pair_counts[pair] += count
    return new_pair_counts


def to_element_counts(pair_counts, first, last):
    counts = Counter()
    for pair, count in pair_counts.items():
        a, b = pair
        counts[a] += count
        counts[b] += count
    counts[first] += 1
    counts[last] += 1

    for pair, count in counts.items():
        new_count = count / 2
        assert new_count.is_integer()
        counts[pair] = int(new_count)

    return counts


if __name__ == '__main__':
    main()
