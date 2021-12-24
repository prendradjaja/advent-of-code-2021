import collections, heapq
from dijkstra_gribouillis import Dijkstra

def bfs(node):
    visited.add(node)
    h = [(0, node)]
    heapq.heapify(h)
    while h:
        cumulative_cost, node = heapq.heappop(h)
        print(node)
        if node == 'e':
            print(cumulative_cost)
            return
        for v in g.neighbors[node]:
            if not v in visited:
                # visit(v, h)
                visited.add(v)
                edge_cost = g.edge_weights[(node, v)]
                heapq.heappush(h, (edge_cost + cumulative_cost, v))
        # print(h)

def visit(node, h):
    print('visiting',node)


class Graph:
    def __init__(self):
        self.vertices = set()
        self.neighbors = collections.defaultdict(set)
        self.edge_weights = {}


    def add_vertex(self, v):
        self.vertices.add(v)


    def add_edge(self, v, w, weight):
        self.add_vertex(v)
        self.add_vertex(w)
        self.neighbors[v].add(w)
        self.neighbors[w].add(v)
        self.edge_weights[(v, w)] = weight
        self.edge_weights[(w, v)] = weight

# g = Graph()
# g.add_edge('a', 'b', 2)
# g.add_edge('b', 'c', 30)
# g.add_edge('c', 'd', 3)
# g.add_edge('d', 'e', 50)
# g.add_edge('a', 'f', 2)
# g.add_edge('f', 'g', 30)
# g.add_edge('g', 'h', 30)
# g.add_edge('h', 'e', 3)

g = Graph()
g.add_edge('a', 'd', 35)
g.add_edge('d', 'e', 50)
g.add_edge('a', 'h', 62)
g.add_edge('h', 'e', 3)

# visited = set()
# bfs('a')

node = 'a'
def neighbors(v):
    result = []
    for w in g.neighbors[v]:
        distance = g.edge_weights[(v, w)]
        result.append((distance, w, None))
    return result

target = 'e'
d = Dijkstra(node, neighbors, target=target)
assert d.is_shortest(target)
print(d[target].dist)
# for k in d.rev_path_to(target):
#     print(k, d[k])
