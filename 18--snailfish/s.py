import fileinput, collections, collections as cl, itertools, itertools as it, math, random, sys, re, string, functools
from grid import gridsource as grid, gridcustom # *, gridsource, gridcardinal, gridplane
from util import *


def main():
    f = open(sys.argv[1] if len(sys.argv) > 1 else 'in')
    f.read().strip()


def safer_eval(s):
    if set(s) <= set('[]0123456789 ,-'):
        return eval(s)
    else:
        1/0  # unsafe


def add(sn1, sn2):
    unreduced = [sn1, sn2]
    return reduce(unreduced)


def reduce(sn):
    while True:
        exploded, sn = maybe_explode(sn)
        if exploded:
            continue
        splitted, sn = maybe_split(sn)
        if not splitted:
            break
    return sn


def maybe_explode(sn):
    1/0  # not implemented


def maybe_split(sn):
    1/0  # not implemented


# TODO this should be inorder traversal
def find_4x_nested(sn, depth=0, *, target=4):
    '''
    Find the leftmost 4x-nested pair inside SN, if any. Else, return None.

    >>> find_4x_nested( [[[[[9,8],1],2],3],4] )
    [9, 8]
    >>> find_4x_nested( [[[[0,1],2],3],4] )
    '''
    if depth == target and isinstance(sn, list):
        return sn
    elif isinstance(sn, list):
        left, right = sn
        return (
            find_4x_nested(
                left,
                depth=depth+1,
                target=target
            )
            or find_4x_nested(
                right,
                depth=depth+1,
                target=target
            )
            or None
        )
    else:
        return None


def inorder_traversal(sn, parent):
    '''
    >>> for item, parent in inorder_traversal([1, 2], None):
    ...     print(item)
    1
    [1, 2]
    2
    '''
    if isinstance(sn, list):
        yield from inorder_traversal(sn[0], sn)
    yield sn, parent
    if isinstance(sn, list):
        yield from inorder_traversal(sn[1], sn)


def right_to_left_traversal(sn, parent):
    '''
    This is just the reverse of an inorder traversal.

    >>> for item, parent in right_to_left_traversal([1, 2], None):
    ...     print(item)
    2
    [1, 2]
    1
    '''
    if isinstance(sn, list):
        yield from right_to_left_traversal(sn[1], sn)
    yield sn, parent
    if isinstance(sn, list):
        yield from right_to_left_traversal(sn[0], sn)


def find_rightward_neighbor(pair, sn):
    '''
    Find the first regular number to the right of PAIR inside SN, if any.
    Else, return None.

    >>> pair = [1, 2]
    >>> find_rightward_neighbor(pair, [pair, [3, 4]])
    (3, [3, 4])
    >>> find_rightward_neighbor(pair, [pair, 3])
    (3, [[1, 2], 3])
    >>> find_rightward_neighbor(pair, [[9, 9], pair])
    '''
    assert isinstance(pair, list)
    found = False
    for item, parent in inorder_traversal(sn, None):
        if pair is item:
            found = True
        elif found and isinstance(item, int) and parent is not pair:
            return item, parent
    return None


def find_leftward_neighbor(pair, sn):
    '''
    Find the first regular number to the right of PAIR inside SN, if any.
    Else, return None.

    >>> pair = [8, 9]
    >>> find_leftward_neighbor(pair, [[6, 7], pair])
    (7, [6, 7])
    >>> find_leftward_neighbor(pair, [7, pair])
    (7, [7, [8, 9]])
    >>> find_leftward_neighbor(pair, [pair, [1, 1]])
    '''
    assert isinstance(pair, list)
    found = False
    for item, parent in right_to_left_traversal(sn, None):
        if pair is item:
            found = True
        elif found and isinstance(item, int) and parent is not pair:
            return item, parent
    return None


if __name__ == '__main__':
    main()
