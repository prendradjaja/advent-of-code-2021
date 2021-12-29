import sys, math, itertools
from util import findints


# Data types:
#
# Interval: (lo: int, hi: int)
# - These are not intervals on real numbers, but intervals on integers.
# - Endpoints are inclusive.
# - Example: (1, 4) represents the interval containing 1, 2, 3, and 4.
#
# Region: (xinterval: Interval, yinterval: Interval, ...)
# - An n-dimensional cuboid.


def main():
    f = open(sys.argv[1] if len(sys.argv) > 1 else 'in')
    lines = [l.rstrip('\n') for l in f]

    on_regions = []
    for i, line in enumerate(lines):
        cmd, region = parse_line(line)

        if cmd == 'on':
            to_add = [region]
            for existing in on_regions:
                to_add = flatten([region_subtract(r, existing) for r in to_add])
            on_regions.extend(to_add)

        elif cmd == 'off':
            on_regions = flatten(
                [region_subtract(existing, region) for existing in on_regions]
            )

        print(f'\rStep {i+1} of {len(lines)} (# of regions: {len(on_regions)})', end='')
    print('\r' + 'Answer:'.ljust(50))

    answer = sum(region_size(r) for r in on_regions)
    print(answer)


def parse_line(line):
    cmd, rest = line.split(' ')
    assert cmd in ['on', 'off']
    xlo, xhi, ylo, yhi, zlo, zhi = findints(rest)
    region = ((xlo, xhi), (ylo, yhi), (zlo, zhi))
    return cmd, region


def interval_overlap(a, b):
    '''
    Given two intervals, return their overlap (or None if no overlap).

    As described above, these are not intervals on real numbers, but intervals
    on integers.

        a 1----6
        b     5--8
        >>> interval_overlap((1, 6), (5, 8))
        (5, 6)

    More tests in test_interval_overlap.txt
    '''
    a, b = sorted([a, b])
    alo, ahi = a
    blo, bhi = b
    if blo > ahi:
        return None
    elif blo == ahi:
        return (blo, blo)
    else:
        hi = min(ahi, bhi)
        return (blo, hi)


def region_subtract(ra, rb):
    '''
    Subtract region B from region A, returning the parts of A that do not
    overlap with B.

    The result is a list of regions (which can be empty: specifically, if A
    overlaps entirely with B, then the result is an empty list).

        Example: A - B results in a list of three smaller regions C, D, E

        aaaaa        cceee
        aaaaa        cceee
        aa***bb  ->  dd.....
        aa***bb      dd.....
          bbbbb        .....

        * = overlap of A and B
        . = where B was (Included just for clarity. This is not present in the
            return value.)

        >>> a = ((1, 5), (1, 4))
        >>> b = ((3, 7), (3, 5))
        >>> c = ((1, 2), (1, 2))
        >>> d = ((1, 2), (3, 4))
        >>> e = ((3, 5), (1, 2))
        >>> region_subtract(a, b) == [c, d, e]
        True

    It would be possible to return an equivalent list with a smaller number of
    regions e.g. by fusing C and D or fusing C and E! This is not implemented.

    More tests in test_region_subtract.txt
    '''
    # ra, rb: region a, region b
    # ia, ib: interval a, interval b

    dimensions = len(ra)
    overlaps = tuple(interval_overlap(ia, ib) for ia, ib in zip(ra, rb))
    if any(overlap == None for overlap in overlaps):
        return [ra]

    subintervals_by_dimension = []
    for d in range(dimensions):
        ia = ra[d]
        ib = rb[d]
        split1 = ib[0] - 0.5
        split2 = ib[1] + 0.5

        if in_interval(ia, split1):
            subintervals = interval_split(ia, split1)
        else:
            subintervals = [ia]

        if in_interval(subintervals[-1], split2):
            subintervals[-1:] = interval_split(subintervals[-1], split2)
        subintervals_by_dimension.append(subintervals)

    subregions = [
        region for region in itertools.product(*subintervals_by_dimension)
        if not in_region(rb, arbitrary_point(region))
    ]
    return subregions


def interval_split(interval, split):
    lo, hi = interval
    assert lo < split < hi
    return [(lo, math.floor(split)), (math.ceil(split), hi)]


def in_interval(interval, point_1d):
    lo, hi = interval
    return lo <= point_1d <= hi


def in_region(region, point):
    '''
    >>> a = ((82, 83), (5, 8))
    >>> in_region(a, (82, 5))
    True
    >>> in_region(a, (81, 5))
    False
    '''
    return all(in_interval(interval, point_1d) for interval, point_1d in zip(region, point))


def arbitrary_point(region):
    return tuple((lo + hi) / 2 for lo, hi in region)


def region_size(region):
    '''
    >>> region_size( ((1, 3), (1, 3), (1, 3)) )
    27
    '''
    result = 1
    for lo, hi in region:
        result *= (hi - lo + 1)
    return result


def flatten(t):
    return [item for sublist in t for item in sublist]


if __name__ == '__main__':
    main()
