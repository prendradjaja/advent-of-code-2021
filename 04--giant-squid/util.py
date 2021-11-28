import re
import inspect
import types
import itertools

def tee_disableable(*args, **kwargs):
    print(*args, **kwargs) ############### can disable me by commenting out this line
    if args:
        return args[0]
p2 = tee_disableable

def tee(*args, **kwargs):
    print(*args, **kwargs)
    if args:
        return args[0]
p = tee

# TODO shouldn't consider full stack, just lineno of function call
def pfirst(*args, **kwargs):
    """
    For each occurrence of this function in source code, print only on the first call. e.g.

    >>> for n in [1, 2]:
    ...     _ = pfirst(n * 10)
    ...     _ = pfirst(n * 100)
    10
    100
    """
    stack = _getstack()
    if not stack in pfirst.seen_stacktraces:
        pfirst.seen_stacktraces.add(stack)
        print(*args, **kwargs)
    if args:
        return args[0]
pfirst.seen_stacktraces = set()
pf = pfirst

def _getstack():
    frame = inspect.currentframe()
    stack = ''
    while frame:
        stack += f'{frame.f_lineno}-{frame.f_code.co_name}/'
        frame = frame.f_back
    return stack

def ints(strings, mixedstring='error'):
    """
    Parses a sequence of strings, some of which are ints. Usually, each should be either exactly
    a number or contain no digits at all. In these cases, just return the string or int.

    If a "mixed string" (contains digits and nondigits) is
    encountered, then the `mixedstring` param determines the behavior:

    - 'error' (default)
    - 'str': keep it as a string
    - 'int': take just the int part

    Example:
    >>> s = "red 1 2"
    >>> color, x, y = ints(s.split())
    >>> color, x, y
    ('red', 1, 2)
    """
    return [maybeint(s, mixedstring) for s in strings]

def maybeint(s, mixedstring='error'):
    """ See ints(...) """
    if re.search('[0-9]', s):
        try:
            return int(s)
        except ValueError:
            if mixedstring == 'error':
                raise
            elif mixedstring == 'str':
                return s
            elif mixedstring == 'int':
                return int(re.search('-?\d+', s).group(0))
            else:
                raise ValueError('Invalid value for mixedstring: ' + mixedstring)
    else:
        return s

def findint(s):
    return maybeint(s, 'int')

def findints(s):
    """
    >>> findints('1_-2__3.45')
    [1, -2, 3, 45]
    """
    return ints(re.findall('-?\d+', s))

def consecutives(seq, n=2, string=False):
    """
    >>> list(consecutives('abcd'))
    [('a', 'b'), ('b', 'c'), ('c', 'd')]
    >>> list(consecutives('abcd', string=True))
    ['ab', 'bc', 'cd']
    >>> list(consecutives('abcd', 3, string=True))
    ['abc', 'bcd']
    >>> list(consecutives('abcd', 5, string=True))
    []
    """
    prevs = []
    for item in seq:
        prevs.append(item)
        if len(prevs) == n:
            if not string:
                yield tuple(prevs)
            else:
                yield ''.join(prevs)
            prevs.pop(0)

def transpose(m):
    """
    >>> transpose([[1, 2, 3], [4, 5, 6]])
    [[1, 4], [2, 5], [3, 6]]
    """
    return [list(i) for i in zip(*m)]

def flipvert(m):
    """
    >>> flipvert([[1, 2], [3, 4]])
    [[3, 4], [1, 2]]
    """
    return m[::-1]

def fliphorz(m):
    """
    >>> fliphorz([[1, 2], [3, 4]])
    [[2, 1], [4, 3]]
    """
    return transpose(flipvert(transpose(m)))

def rotmat(original):
    """
    Rotate clockwise

    >>> rotmat([[1, 2], [3, 4]])
    [(3, 1), (4, 2)]
    """
    return list(zip(*original[::-1]))

def one(seq, only=True):
    """
    Return the only element of a one-item sequence.

    >>> one([2])
    2
    >>> one({2})
    2
    >>> one('2')
    '2'
    >>> one('22')
    Traceback (most recent call last):
    AssertionError: Not length 1: 22

    This can also be used to return an arbitrary item from a multi-item
    sequence. The main use case for this is taking an arbitrary item from a
    set. The same can be accomplished with next(iter(my_set))

    >>> one([2, 3], only=False)
    2
    """
    if only:
        assert len(seq) == 1, f'Not length 1: {seq}'
    for item in seq:
        return item

def ilen_exhaustive(seq):
    """
    Given a finite iterator, return the number of items. As a necessary side
    effect, this also exhausts the iterator.

    >>> iterator = iter('abc')
    >>> ilen_exhaustive(iterator)
    3
    >>> ilen_exhaustive(iterator)
    0
    """
    count = 0
    for _ in seq:
        count += 1
    return count

# SimpleNamespace can be used similarly to objects in JavaScript: Set
# attribute names and values on the fly, and fetch values later with dot
# notation. This seems to perform somewhat slower than using a Python dict.
#
# Example usage:
#     point = obj(x=1, y=2)
#     point.x  # -> 1
obj = types.SimpleNamespace

def Record(arg1, arg2=None):
    """
    Record(field_names) -> constructor
    Record(typename, field_names) -> constructor

    Creates a record type. Similar to namedtuple, but with mutability and
    WITHOUT ordering.

    TODO: Add destructuring support? Requires ordering.

    typename parameter can be omitted. It does nothing, and is only included
    so Record is closer to a drop-in replacement for namedtuple.

    >>> Point = Record('x y')
    >>> a = Point(1, 2)
    >>> a.x
    1
    >>> a.x += 10
    >>> a.x
    11

    >>> Point2 = Record('Point2', 'x y')
    >>> b = Point2(3, 4)
    >>> b.x
    3
    >>> b.x += 10
    >>> b.x
    13
    """

    if arg2:
        field_names = arg2
    else:
        field_names = arg1
    field_names = field_names.split()

    def constructor(*values):
        obj = types.SimpleNamespace()
        for name, value in zip(field_names, values):
            setattr(obj, name, value)
        return obj

    return constructor

def nth(iterable, n):
    '''
    >>> nth(range(10), 3)
    3
    '''
    return next(itertools.islice(iterable, n, n+1))

def strjoin(items, delimiter=' '):
    '''
    >>> strjoin([3,4])
    '3 4'
    >>> strjoin(range(3))
    '0 1 2'
    >>> strjoin(['ab', 'cd'])
    'ab cd'
    '''
    return delimiter.join(str(item) for item in items)


# enumerate
# ascii_lowercase ascii_lowercase
# defaultdict namedtuple Counter _replace
# combinations permutations product combinations_with_replacement
# lru_cache maxsize
