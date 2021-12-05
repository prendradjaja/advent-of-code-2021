import sys, collections


def main():
    f = open(sys.argv[1] if len(sys.argv) > 1 else 'in')
    lines = [l.rstrip('\n') for l in f]

    g = Graph()
    for line in lines:
        v, w = line.split('-')
        g.add_edge(v, w)

    print(count_paths(g, ['start']))


def count_paths(g, prefix):
    if prefix[-1] == 'end':
        return 1

    total = 0
    for n in g.neighbors[prefix[-1]]:
        if (
            n != 'start'
            and (n.isupper() or can_visit_small_cave(prefix, n))
        ):
            total += count_paths(g, prefix + [n])
    return total


def can_visit_small_cave(prefix, n):
    small_caves = [c for c in prefix if c.islower()]
    return (
        # never visited this small cave, or
        n not in prefix

        # never revisited any small cave (Once you revisit a small cave, it
        # equally rules out revisiting this cave and revisiting any cave: So
        # the "a single small cave can be visited at most twice" constraint
        # can be expressed in this way)
        or len(small_caves) == len(set(small_caves))
    )


class Graph:
    def __init__(self):
        self.vertices = set()
        self.neighbors = collections.defaultdict(set)


    def add_vertex(self, v):
        self.vertices.add(v)


    def add_edge(self, v, w):
        self.add_vertex(v)
        self.add_vertex(w)
        self.neighbors[v].add(w)
        self.neighbors[w].add(v)


if __name__ == '__main__':
    main()
