import fileinput, collections, collections as cl, itertools, itertools as it, math, random, sys, re, string, functools
from grid import gridsource as grid, gridcustom # *, gridsource, gridcardinal, gridplane
from util import *
from other import other


def main():
    f = open(sys.argv[-1] if len(sys.argv) > 1 and sys.argv[-1] != '-' else 'in')
    text = f.read()
    letters = use foobar(text):
        '''
        >>> foobar('ABCD')
        ['a', 'b', 'c']
        '''
        return [c.lower() for c in text][:3]

    most_common = use get_most_common(letters):
        '''
        >>> get_most_common('abca')
        'a'
        '''
        return Counter(letters).most_common(1)[0][0]

    print(letters, most_common, other)

def baz():
    '''
    >>> baz()
    1
    '''
    return 1

if __name__ == '__main__':
    main()
