import fileinput, collections, collections as cl, itertools, itertools as it, math, random, sys, re, string, functools
from grid import gridsource as grid, gridcustom # *, gridsource, gridcardinal, gridplane
from util import *
from interval_overlap import interval_overlap


# interval = e.g. (1,3) represents 1 to 3 inclusive
# region = (xinterval, yinterval, ...)  (n-dimensional)


def main():
    f = open(sys.argv[-1] if len(sys.argv) > 1 and sys.argv[-1] != '-' else 'in')
    lines = [l.rstrip('\n') for l in f]
    on_regions = []
    for i, line in enumerate(lines):
        print('processing line', i)
        cmd, *region = parse_line(line)
        xlo, xhi, ylo, yhi, zlo, zhi = region
        if True:
        # if not excludes_initialization_area(region):
            region = ((xlo, xhi), (ylo, yhi), (zlo, zhi))
            if cmd == 'on':
                to_add = [region]
                # to_add = flatten([region_subtract(r, existing) for r in to_add for existing in on_regions])
                for existing in on_regions:
                    to_add = flatten([region_subtract(r, existing) for r in to_add])
                on_regions.extend(to_add)
            elif cmd == 'off':
                on_regions = flatten([region_subtract(existing, region) for existing in on_regions])
            else:
                1/0  # unreachable
        print('  count regions', len(on_regions))
    # answer = len(on)
    answer = sum(region_size(r) for r in on_regions)
    print(answer)
    # print(answer == 2758514936282235)


def parse_line(line):
    cmd, rest = line.split(' ')
    return cmd, *findints(rest)


def excludes_initialization_area(region):
    xlo, xhi, ylo, yhi, zlo, zhi = region
    return (
        xlo < xhi < -50 or
        ylo < yhi < -50 or
        zlo < zhi < -50 or
        xhi > xlo > 50 or
        yhi > ylo > 50 or
        zhi > zlo > 50
    )



def unused_just_for_line_completion():
    xlo, xhi, ylo, yhi, zlo, zhi = region



# TODO I only checked the length is right, not the actual subregions
def region_subtract(ra, rb):
    '''
    aaaaa
    aaaaa
    aa***bb
    aa***bb
      bbbbb
    >>> a = ((57, 60), (5, 9))
    >>> b = ((59, 61), (7, 11))
    >>> len(region_subtract(a, b))
    3

    aaaa
    aaaa  bbb
    >>> a = ((66, 67), (5, 8))
    >>> b = ((67, 67), (11, 13))
    >>> region_subtract(a, b)
    [((66, 67), (5, 8))]

    aaaaaaa
    aaaaaaa
    aa***aa  (b is entirely inside a)
    aa***aa
    aaaaaaa
    >>> a = ((73, 77), (5, 11))
    >>> b = ((75, 76), (7, 9))
    >>> len(region_subtract(a, b))
    8

    ****  (b == a)
    ****
    >>> a = ((82, 83), (5, 8))
    >>> b = a
    >>> len(region_subtract(a, b))
    0
    '''
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



if __name__ == '__main__':
    main()
