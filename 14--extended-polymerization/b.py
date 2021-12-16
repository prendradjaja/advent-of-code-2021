import sys
from collections import Counter
from util import consecutives

# NBCCNBBBCBHCB
# NBBBCNCCNBBNBBBCHBHHBCHB
# NBBBCNCCNBBNBNBBCHBHHBCHB


# linked list
# array
# counts??


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

    element_counts = to_element_counts(pair_counts, first, last).values()

    answer = max(element_counts) - min(element_counts)
    answer = int(answer)
    print(answer)


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
    double_counts = Counter()
    for pair, count in pair_counts.items():
        a, b = pair
        double_counts[a] += count
        double_counts[b] += count
    double_counts[first] += 1
    double_counts[last] += 1
    return { key: value / 2 for key, value in double_counts.items() }


if __name__ == '__main__':
    main()
