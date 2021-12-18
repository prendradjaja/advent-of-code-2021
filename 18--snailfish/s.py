import fileinput, collections, collections as cl, itertools, itertools as it, math, random, sys, re, string, functools
from grid import gridsource as grid, gridcustom # *, gridsource, gridcardinal, gridplane
from util import *


def main():
    f = open(sys.argv[1] if len(sys.argv) > 1 else 'in')
    snlist = f.read().strip()
    my_sum = sum(snlist)
    print(magnitude(my_sum))


def magnitude(sn):
    if isinstance(sn, int):
        return sn
    elif isinstance(sn, list):
        left, right = sn
        return 3 * magnitude(left) + 2 * magnitude(right)
    else:
        1/0


def safer_eval(s):
    if set(s) <= set('[]0123456789 ,-'):
        return eval(s)
    else:
        1/0  # unsafe


def sum(snlist):
    sns = [safer_eval(line.strip()) for line in snlist.split('\n')]
    return functools.reduce(add, sns)


def add(sn1, sn2):
    unreduced = [sn1, sn2]
    return reduce(unreduced)


def reduce(sn):
    '''
    >>> reduce([[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]])
    [[[[0, 7], 4], [[7, 8], [6, 0]]], [8, 1]]
    '''
    while True:
        exploded, sn = maybe_explode(sn)
        if not exploded:
            splitted, sn = maybe_split(sn)
            if not splitted:
                break
    return sn


def maybe_explode(sn):
    '''
    >>> maybe_explode([[[[[9,8],1],2],3],4])
    (True, [[[[0, 9], 2], 3], 4])
    >>> maybe_explode([7,[6,[5,[4,[3,2]]]]])
    (True, [7, [6, [5, [7, 0]]]])
    >>> maybe_explode([[6,[5,[4,[3,2]]]],1])
    (True, [[6, [5, [7, 0]]], 3])
    >>> maybe_explode([[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]])
    (True, [[3, [2, [8, 0]]], [9, [5, [4, [3, 2]]]]])
    >>> maybe_explode([[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]])
    (True, [[3, [2, [8, 0]]], [9, [5, [7, 0]]]])

    >>> maybe_explode( [7,[6,[5,[4,0]]]] )
    (False, [7, [6, [5, [4, 0]]]])
    >>> maybe_explode( [[6,[5,[4,0]]],1] )
    (False, [[6, [5, [4, 0]]], 1])
    >>> maybe_explode( [[3,[2,[1,0]]],[6,[5,[4,0]]]] )
    (False, [[3, [2, [1, 0]]], [6, [5, [4, 0]]]])
    '''
    exploding_pair = find_4x_nested(sn)
    if not exploding_pair:
        return False, sn

    explode_add(True, exploding_pair, sn)
    explode_add(False, exploding_pair, sn)

    parent, index = find_parent_and_index(exploding_pair, sn)
    parent[index] = 0

    return True, sn


def explode_add(is_left, exploding_pair, sn):
    find_neighbor = find_leftward_neighbor if is_left else find_rightward_neighbor
    index_in_exploding = 0 if is_left else 1

    neighbor = find_neighbor(exploding_pair, sn)
    if neighbor:
        value, parent, index_in_parent = neighbor
        parent[index_in_parent] = value + exploding_pair[index_in_exploding]


def maybe_split(sn):
    '''
    >>> maybe_split([[[[0,7],4],[15,[0,13]]],[1,1]])
    (True, [[[[0, 7], 4], [[7, 8], [0, 13]]], [1, 1]])
    >>> maybe_split([[[[0,7],4],[[7,8],[0,13]]],[1,1]])
    (True, [[[[0, 7], 4], [[7, 8], [0, [6, 7]]]], [1, 1]])
    >>> maybe_split([[[[0,7],4],[[7,8],[6,0]]],[8,1]])
    (False, [[[[0, 7], 4], [[7, 8], [6, 0]]], [8, 1]])
    '''
    for item, parent, index in inorder_traversal(sn, None, None):
        if isinstance(item, int) and item >= 10:
            break
    else:  # not found
        return False, sn

    parent[index] = split(item)

    return True, sn


def split(n):
    '''
    >>> split(10)
    [5, 5]
    >>> split(11)
    [5, 6]
    '''
    return [math.floor(n / 2), math.ceil(n / 2)]


# i think this can be either preorder or inorder (this is preorder)
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


def find_parent_and_index(needle, haystack):
    '''
    Find NEEDLE in HAYSTACK (both snailfish numbers NOT regular numbers).
    Return NEEDLE's parent and index in that parent.

    >>> needle = [3, 4]
    >>> find_parent_and_index(needle, [needle, [5, 6]])
    ([[3, 4], [5, 6]], 0)
    >>> find_parent_and_index(needle, [[2, needle], [5, 6]])
    ([2, [3, 4]], 1)
    '''
    assert isinstance(needle, list)
    for item, parent, index in inorder_traversal(haystack, None, None):
        if needle is item:
            return parent, index
    1/0  # not found


def inorder_traversal(sn, parent, index):
    '''
    >>> for item, parent, index in inorder_traversal([1, 2], None, None):
    ...     print(item)
    1
    [1, 2]
    2
    '''
    if isinstance(sn, list):
        yield from inorder_traversal(sn[0], sn, 0)
    yield sn, parent, index
    if isinstance(sn, list):
        yield from inorder_traversal(sn[1], sn, 1)


def right_to_left_traversal(sn, parent, index):
    '''
    This is just the reverse of an inorder traversal.

    >>> for item, parent, index in right_to_left_traversal([1, 2], None, None):
    ...     print(item)
    2
    [1, 2]
    1
    '''
    if isinstance(sn, list):
        yield from right_to_left_traversal(sn[1], sn, 1)
    yield sn, parent, index
    if isinstance(sn, list):
        yield from right_to_left_traversal(sn[0], sn, 0)


def find_rightward_neighbor(pair, sn):
    '''
    Find the first regular number (and its parent & index in that parent) to
    the right of PAIR inside SN, if any. Else, return None.

    >>> pair = [1, 2]
    >>> find_rightward_neighbor(pair, [pair, [3, 4]])
    (3, [3, 4], 0)
    >>> find_rightward_neighbor(pair, [pair, 3])
    (3, [[1, 2], 3], 1)
    >>> find_rightward_neighbor(pair, [[9, 9], pair])
    '''
    assert isinstance(pair, list)
    found = False
    for item, parent, index in inorder_traversal(sn, None, None):
        if pair is item:
            found = True
        elif found and isinstance(item, int) and parent is not pair:
            return item, parent, index
    return None


def find_leftward_neighbor(pair, sn):
    '''
    Find the first regular number (and its parent & index in that parent) to
    the right of PAIR inside SN, if any. Else, return None.

    >>> pair = [8, 9]
    >>> find_leftward_neighbor(pair, [[6, 7], pair])
    (7, [6, 7], 1)
    >>> find_leftward_neighbor(pair, [7, pair])
    (7, [7, [8, 9]], 0)
    >>> find_leftward_neighbor(pair, [pair, [1, 1]])
    '''
    assert isinstance(pair, list)
    found = False
    for item, parent, index in right_to_left_traversal(sn, None, None):
        if pair is item:
            found = True
        elif found and isinstance(item, int) and parent is not pair:
            return item, parent, index
    return None


if __name__ == '__main__':
    main()
