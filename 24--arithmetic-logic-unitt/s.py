import fileinput, collections, collections as cl, itertools, itertools as it, math, random, sys, re, string, functools
from grid import gridsource as grid, gridcustom # *, gridsource, gridcardinal, gridplane
from util import *


def main():
    f = open(sys.argv[1] if len(sys.argv) > 1 else 'in')
    lines = [l.rstrip('\n') for l in f]

    # valid = False
    # counting = get_counting()
    # while not valid:
    #     # n = 13579246899999
    #     n = get_random()
    #     # print(n)
    #     variables = execute_program(lines, n, verbose=False)
    #     valid = variables['z'] == 0
    #     # print('Valid?', valid)
    # print(n)

    # for n in itertools.product([1,2,3,4,5,6,7,8,9], repeat=4):
    #     lines = lines[:18*len(n)]
    #     variables = execute_program(lines, n, verbose=False)
    #     print(','.join(str(x) for x in n), variables['z'], sep='|')

    # 167893
    # 314125

    # # from the top
    # n = [9, 9, 9, 9]
    # # n = [1, 1, 1, 1]
    # lines = lines[:18*len(n)]
    # variables = execute_program(lines, n, verbose=True)

    # from the bottom
    # n = [5, 9, 9, 9, 8, 4, 2, 6, 9, 9, 7, 9, 7, 9]
# 13621111481315

# 59998426997979
    # n = [9, 8, 1, 2, 6, 9, 9, 7, 9, 9, 9]
    lines = lines[-18*len(n):]
    variables = execute_program(lines, n, verbose=True, initial_variables={
        'w': 0, 'x': 0, 'y': 0,
        'z': 0
    })




# def chunks(lst, size):
#     '''
#     The last chunk might be incomplete, depending on len(lst) and size.
#     >>> [*chunks([*'abcdef'], 2)]
#     [['a', 'b'], ['c', 'd'], ['e', 'f']]
#     >>> [*chunks([*'abcdef'], 4)]
#     [['a', 'b', 'c', 'd'], ['e', 'f']]
#     '''
#     i = 0
#     while i < len(lst):
#         yield lst[i:i+size]
#         i += size


def get_random():
    result = ''
    for _ in range(14):
        result += random.choice('123456789')
    return int(result)


def get_counting():
    n = 11111111111111
    n = 13579246899999
    while True:
        n += 1
        if '0' not in str(n):
            yield n



def execute_program(lines, inputnum, *, verbose=False, initial_variables=None):
    wxyz = 'wxyz'
    # digits = to_digits(inputnum)
    digits = iter(inputnum)
    if not initial_variables:
        variables = { v: 0 for v in wxyz }
    else:
        variables = initial_variables
    ops = {
        'add': lambda a, b: a + b,
        'mul': lambda a, b: a * b,
        'div': my_div,
        'mod': lambda a, b: a % b,
        'eql': lambda a, b: int(a == b),
    }
    for i, line in enumerate(lines,start=1):
        if verbose and (i - 1) % 18 == 0:
            print()
        opname, *rest = line.split()
        if opname == 'inp':
            [a] = rest
            assert a in wxyz
            result = next(digits)
            variables[a] = result
            aval = None
            b = None
            bval = None
        else:
            a, b = rest
            assert a in wxyz
            b = maybeint(b)
            aval = dereference(a, variables)
            bval = dereference(b, variables)
            op = ops[opname]
            result = op(aval, bval)
            variables[a] = result
        if verbose:
            # print(opname, '\t|', a, aval, '\t|', b, bval, '\t|', result)
            print(f'{i} {opname}'.ljust(8), f'{a} {aval}'.ljust(11), f'{b} {bval if bval != b else ""}'.ljust(11), str(result).ljust(9), [*variables.values()], sep=' | ')
    return variables


def my_div(a, b):
    '''
    >>> my_div(17, 3)
    5
    >>> my_div(15, 3)
    5
    '''
    result = a / b
    sign = get_sign(result)
    result = sign * math.floor(abs(result))
    assert result == a // b
    return result


def get_sign(n):
    if n == 0:
        return 0
    elif n > 0:
        return 1
    else:
        return -1


def dereference(x, variables):
    if isinstance(x, int):
        return x
    else:
        return variables[x]


def to_digits(n):
    if n is None:
        return
    for digit in str(n):
        yield int(digit)


if __name__ == '__main__':
    main()
