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



