import sys
from types import SimpleNamespace as obj
from graph import Graph
from rotations import rotators2d, rotators3d


def main():
    f = open(sys.argv[1] if len(sys.argv) > 1 else 'in')

    sections = f.read().strip().split('\n\n')
    scanners = [parse_section(s) for s in sections]
    dimensions = len(scanners[0][0])

    if dimensions == 2:
        config = obj(
            overlap_needed = 3,
            rotators = rotators2d,
            count_rotations = 4,
            subvec = subvec2d,
        )
    elif dimensions == 3:
        config = obj(
            overlap_needed = 12,
            rotators = rotators3d,
            count_rotations = 24,
            subvec = subvec3d,
        )
    else:
        print('Dimensions other than 2D and 3D are not supported.')
        exit(1)

    visited = set()
    g = Graph()
    try:
        dfs(0, scanners, config, g, visited)
    except SearchDone:
        print('done')


def dfs(u, scanners, config, g, visited):
    visited.add(u)
    for v in neighbors(u, scanners, config, g):
        if v not in visited:
            dfs(v, scanners, config, g, visited)


def neighbors(u, scanners, config, g):
    known_overlaps = list(g.neighbors[u])
    known_no_overlaps = []
    while True:
        # TODO *details is fragile
        # - replace with explicit variable names?
        # - OR replace with an explicit data type?
        has_overlap, *details = find_overlapping_scanner(scanners, u, known_overlaps + known_no_overlaps, config)
        if has_overlap:
            print(details, u)
            neighbor, *details, new_no_overlaps = details
            known_no_overlaps.extend(new_no_overlaps)
            known_overlaps.append(neighbor)
            g.add_edge(u, neighbor)
            if len(g.vertices) == len(scanners):
                raise SearchDone
            yield neighbor
            known_overlaps = list(set(known_overlaps) | set(g.neighbors[u]))
        else:
            break


class SearchDone(Exception):
    pass


def parse_section(section):
    section = section.split('\n')[1:]
    result = []
    for line in section:
        result.append(tuple(int(n) for n in line.split(',')))
    return result


def find_overlap_of_scanners(s1, s2, config):
    rotators = config.rotators
    count_rotations = config.count_rotations
    overlap_needed = config.overlap_needed
    subvec = config.subvec
    for p1 in s1:
        for p2 in s2:
            for r in range(count_rotations):
                rotate = rotators[r]
                # Align p1 and p2
                n1 = center(s1, p1, subvec)
                n2 = center(s2, p2, subvec)

                # Rotate n2 by r
                n2 = [rotate(beacon) for beacon in n2]

                # Check for overlap
                if len(set(n1) & set(n2)) >= overlap_needed:
                    return( (True, p1, p2, r) )
    return (False,)


def find_overlapping_scanner(scanners, index, skip, config):
    count_rotations = config.count_rotations
    overlap_needed = config.overlap_needed

    scanner = scanners[index]
    no_overlap = []
    for i, other_scanner in enumerate(scanners):
        if i == index or i in skip:
            continue
        has_overlap, *overlap_details = find_overlap_of_scanners(scanner, other_scanner, config)
        if has_overlap:
            return( (True, i, *overlap_details, no_overlap) )
        else:
            no_overlap.append(i)
    return (False,)


def subvec2d(a, b):
    ax, ay = a
    bx, by = b
    return (ax-bx, ay-by)


def subvec3d(a, b):
    ax, ay, az = a
    bx, by, bz = b
    return (ax-bx, ay-by, az-bz)


def center(scanner, origin_beacon, subvec):
    return [subvec(beacon, origin_beacon) for beacon in scanner]


if __name__ == '__main__':
    main()
