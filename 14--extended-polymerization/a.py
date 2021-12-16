import sys, collections


def main():
    f = open(sys.argv[1] if len(sys.argv) > 1 else 'in')
    polymer, rules = f.read().strip().split('\n\n')
    polymer = polymer.strip()
    rules = rules.strip().split('\n')
    rules = dict(rule.split(' -> ') for rule in rules)

    for step in range(10):
        polymer = iterate(polymer, rules)

    hi, *_, lo = collections.Counter(polymer).most_common()

    hi_name, hi_count = hi
    lo_name, lo_count = lo
    print(hi_count - lo_count)


def iterate(polymer, rules):
    for left, right in rules.items():
        start, end = left
        polymer = replace(polymer, left, start + right.lower() + end)
    return polymer.upper()


def replace(s, old, new):
    '''
    replace(s) acts like the built-in s.replace()...
    >>> replace('a b c', ' ', '_')
    'a_b_c'
    >>> replace('abba', 'bb', 'bnb')
    'abnba'

    ...except it can replace overlapping instances of `old` too (by repeated
    application).
    >>> replace('abbba', 'bb', 'bnb')
    'abnbnba'
    >>> 'abbba'.replace('bb', 'bnb')
    'abnbba'
    '''
    # My implementation supports arbitrarily many repeats, but I think this is
    # actually not needed for this problem (should only need up to 2 repeats)
    while True:
        new_s = s.replace(old, new)
        if new_s == s:
            break
        s = new_s
    return new_s


if __name__ == '__main__':
    main()
