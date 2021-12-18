'''
Various functions I didn't end up needing that I might still want (e.g. if I
want to solve again with a different approach)
'''


def find_rightward_neighbor(pair, sn, *, _pair_found=False):
    '''
    Find the first regular number to the right of PAIR inside SN, if any.
    Else, return None.
    '''
    if sn == pair:
        _pair_found = True
    if isinstance(sn, int) and _pair_found:
        return sn

    left, right = sn
    return (
        find_rightward_neighbor(pair, left, _pair_found=_pair_found)
        or find_rightward_neighbor(pair, right, _pair_found=_pair_found)
        or None
    )


def to_variables(snlist):
    '''
    >>> snlist = """
    ... [3, [1, 4]]
    ... [1, 5]
    ... """.strip()
    >>> to_variables(snlist)
    {-1: 3, -2: 1, -3: 4, -4: 1, -5: 5}
    '''
    variables = {}
    for line in snlist.split('\n'):
        line = line.strip()
        sn = safer_eval(line)
        to_variables_from_sn(sn, variables)
    return variables


def to_variables_from_sn(sn, variables):
    if isinstance(sn, int):
        name = next_variable(variables)
        variables[name] = sn
    elif isinstance(sn, list):
        left, right = sn
        to_variables_from_sn(left, variables)
        to_variables_from_sn(right, variables)
    else:
        1/0  # invalid


def next_variable(variables):
    '''
    >>> next_variable({})
    -1
    >>> next_variable({-1: 3})
    -2
    '''
    return -len(variables) - 1
