import fileinput, collections, collections as cl, itertools, itertools as it, math, random, sys, re, string, functools
from grid import gridsource as grid, gridcustom # *, gridsource, gridcardinal, gridplane
from util import *

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
    for step in range(10):
        # abcd -> len 4 -> i 3
        # for i in range(len(polymer) - 2, 0 - 1, -1):
        #     polymer[i : i+2]
        polymer = iterate(polymer, rules)
    hi, *_, lo = collections.Counter(polymer).most_common()
    hi_name, hi_count = hi
    lo_name, lo_count = lo
    print(hi_count - lo_count)


def iterate(polymer, rules):
    '''
    >>> f = open('example')
    >>> _, rules = f.read().strip().split('\\n\\n')
    >>> rules = rules.strip().split('\\n')
    >>> rules = dict(rule.split(' -> ') for rule in rules)
    >>> iterate('NNCB', rules)
    'NCNBCHB'
    >>> iterate('NNCB', rules)
    'NCNBCHB'
    >>> iterate('NBCCNBBBCBHCB', rules)
    'NBBBCNCCNBBNBNBBCHBHHBCHB'
    '''
    for left, right in rules.items():
        start, end = left
        polymer = replace(polymer, left, start + right.lower() + end)
        # print(left, right, polymer)
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
