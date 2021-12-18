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
