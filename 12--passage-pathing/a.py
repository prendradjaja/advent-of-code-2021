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
        if n.isupper() or n not in prefix:
            total += count_paths(g, prefix + [n])
    return total


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
