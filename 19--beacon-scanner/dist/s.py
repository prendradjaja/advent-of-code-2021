import fileinput, collections, collections as cl, itertools, itertools as it, math, random, sys, re, string, functools
from grid import gridsource as grid, gridcustom # *, gridsource, gridcardinal, gridplane
from util import *
def main():
    f = open(sys.argv[-1] if len(sys.argv) > 1 and sys.argv[-1] != '-' else 'in')
    sections = f.read().strip().split('\n\n')
    scanners = [parse_section(s) for s in sections]
    dimensions = len(scanners[0][0])
    if dimensions == 2:
        config = obj(
            overlap_needed = 3,
            rotate = rotate2d,
            count_rotations = 4,
        )
    elif dimensions == 3:
        config = obj(
            overlap_needed = 12,
            rotate = rotate3d,  # todo
            count_rotations = 24,
        )
    else:
        1/0  # invalid dim
    # print(find_overlap_of_scanners(scanners[0], scanners[1], config))
    print(find_overlapping_scanner(scanners, 0, config))
def parse_section(section):
    section = section.split('\n')[1:]
    result = []
    for line in section:
        result.append(tuple(int(n) for n in line.split(',')))
    return result
def rotate2d(point, n):
    for _ in range(n):
        point = grid.rotvec(point, 'R')
    return point
def find_overlap_of_scanners(s1, s2, config):
    rotate = config.rotate
    count_rotations = config.count_rotations
    overlap_needed = config.overlap_needed
    for p1 in s1:
        for p2 in s2:
            for r in range(count_rotations):
                # Align p1 and p2
                n1 = center(s1, p1)
                n2 = center(s2, p2)
                # Rotate n2 by r
                n2 = [rotate(beacon, r) for beacon in n2]
                # Check for overlap
                if len(set(n1) & set(n2)) >= overlap_needed:
                    return (True, p1, p2, r)
    return False
def find_overlapping_scanner(scanners, index, config):
    rotate = config.rotate
    count_rotations = config.count_rotations
    overlap_needed = config.overlap_needed
    scanner = scanners[index]
    for i, other_scanner in enumerate(scanners):
        if i == index:
            continue
        has_overlap, *overlap_details = find_overlap_of_scanners(scanner, other_scanner, config)
        if has_overlap:
            return (i, *overlap_details)
    1/0  # Every scanner is guaranteed to have some overlap
def center(scanner, origin_beacon):
    return [grid.subvec(beacon, origin_beacon) for beacon in scanner]
if __name__ == '__main__':
    main()
