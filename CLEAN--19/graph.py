import collections


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
