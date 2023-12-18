'''
Author: User "Gribouillis" on python-forum.io

https://python-forum.io/thread-34122.html
'''

from collections import namedtuple
import heapq as hq
import itertools as itt

__version__ = '2021.06.30'

Score = namedtuple('Score', 'dist index node prev edge')

class Dijkstra(dict):

    def __init__(
        self, node, neighbors, maxitems=10000, maxdist=None, target=None):
        """Create a Dijkstra instance from an initial node

        Arguments:
            * node: a hashable object representing the starting node
            * neighbors: a function to compute the neighbors of a node
                (more below).
            * maxitems=10000: optional bound to limit the number
                of computation steps in the case of a very large
                or infinite graph.
            * maxdist=None: optionaly a maximal distance from the initial
                node where to stop the computation.
            * target=None: optional target node. The algorithm stops once
                a shortest path to this target has been found.

        The 'neighbors' argument must be a function returning
        or generating a sequence of tuples with 3 elements
            (distance, node, edge)
        'distance' is a nonnegative number to a neigboring 'node', a
        hashable python object. 'edge' is an abitrary object that is
        not used by the algorithm but can be stored as client data
        in the result. This value can be None.

        Instantiating a Dijkstra instance runs immediately Dijkstra's
        algorithm to compute the shortest path from the initial node
        to the nodes discovered by successive calls to the
        neighbors() function.

        The instance itself is a dictionary that maps nodes to
        'Score' objects. These are namedtuples with fields
            * dist: the distance from the initial node to this node
            * index: a number indicating the rank of creation of this
                    Score object
            * node: the node in question
            * prev: the previous node in the shortest discovered path
            * edge: the data provided by the neighbors() function in the
                    transition from the previous node to this one

        Due to the 'maxitems' and 'maxdist' mechanisms used to
        optionally stop the algorithm, it may occur that the shortest
        distance to some nodes of the graph may be shorter than the
        distance actually computed. A method is provided:

            self.is_shortest(node)

        returns True if the found distance is guaranteed to be the
        shortest distance from the initial node. Internally, there
        is a value self.threshold such that the distance is
        guaranteed to be optimal if and only if it is smaller or
        equal to the threshold.

        To retrieve paths from the initial node to a given node,
        a method is provided:

            self.rev_path_to(node)

        this method generates the sequence of nodes leading from
        the initial node to this node in reverse order. The Score
        objects stored in self can be used to obtain details about
        the path.

        Remark: node objects must all be different from None.
        """
        cnt = itt.count()
        self[node] = Score(0, next(cnt), node, None, None)
        seen = self
        heap = [seen[node]]
        visited = set()

        for s in self._elements(heap, visited, maxitems, maxdist, target):
            seen[s.node] = s
            visited.add(s.node)
            for d, m, edge in neighbors(s.node):
                t = seen.get(m, None)
                if t and (t.dist <= d + self.threshold):
                    continue
                seen[m] = Score(
                    d + self.threshold, next(cnt), m, s.node, edge)
                hq.heappush(heap, seen[m])

        self.root = node

    def _heapiter(self, heap):
        while heap:
            s = hq.heappop(heap)
            self.threshold = s.dist
            yield s

    def _elements(self, heap, visited, maxitems, maxdist, target):
        seq = (x for x in self._heapiter(heap) if x.node not in visited)
        if maxitems is not None:
            seq = itt.islice(seq, 0, maxitems)
        if maxdist is not None:
            seq = itt.takewhile((lambda x: x.dist < maxdist), seq)
        if target is not None:
            seq = itt.takewhile((lambda x: x.node != target), seq)
        return seq


    def is_shortest(self, node):
        """Indicates if the shortest distance to the node is known"""
        return self[node].dist <= self.threshold

    def rev_path_to(self, node):
        """Generator of the shortest path found to the node.

        The path is generated in reverse order as a sequence of
        Score objects.
        """
        s = self[node]
        while s:
            yield s.node
            s = self.get(s.prev, None)

if __name__ == '__main__':
    """As an example, we generate a shortest path of transpositions
    leading from one permutation of 7 elements to another one.

    Of course this problem is very simple to solve by other means
    but it is interesting to see Dijkstra's algorithm find the
    solution blindly.
    """
    perm = (0, 1, 2, 3, 4, 5, 6) # a permutation

    def neighs(sigma): # generate neighbors by permuting 2 elements
        s = list(sigma)
        for j in range(1, len(sigma)):
            for i in range(j):
                s[i], s[j] = s[j], s[i]
                yield 1, tuple(s), (i, j)
                s[i], s[j] = s[j], s[i]

    # run the shortest path algorithm
    d = Dijkstra(perm, neighs, maxdist=6)

    target = (3, 5, 1, 2, 6, 4, 0)
    print(
        f"Distance to target {target} is known to be shortest?"
        f" {d.is_shortest(target)}")
    for k in d.rev_path_to(target):
        print(k, d[k].edge)
