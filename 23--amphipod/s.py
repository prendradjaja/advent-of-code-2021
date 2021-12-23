import fileinput, collections, collections as cl, itertools, itertools as it, math, random, sys, re, string, functools
from grid import gridsource as grid, gridcustom # *, gridsource, gridcardinal, gridplane
from util import *


# type Pos = (r: int, c: int)
# type Alias = '.' | 'a' | ... | 'h' | '0' | ... | '6'
# type State = { [key: Alias]: 'A' | 'B' | 'C' | 'D' }
# type Move = (start: Alias, end: Alias)

width = 13
height = 5


def main():
    g = parse_layout()
    state = parse_input(g)

    # movegen example
    del state['b']
    state['3'] = 'C'
    show(g, state)
    print(generate_moves(g, state))


def parse_layout():
    f = open('layout.txt')
    g = Graph()
    for r, line in enumerate(f.readlines()):
        line = line.rstrip('\n')
        for c, ch in enumerate(line):
            pos = (r, c)
            if ch == ' ':
                continue
            elif ch == '#':
                continue
                # type = '#'
                # alias = None
            elif ch in '.abcdefgh0123456':
                type = '.'
                alias = None if ch == '.' else ch
            else:
                1/0
            g.add_vertex(pos, type, alias)
            left = (r, c-1)
            up = (r-1, c)
            for neighbor in (left, up):
                if (
                    type == '.'
                    and neighbor in g.vertices
                    and g.vertices[neighbor].type == '.'
                ):
                    g.add_edge(pos, neighbor)
    return g


def parse_input(g):
    f = open(sys.argv[1] if len(sys.argv) > 1 else 'in')
    state = {}
    for r, line in enumerate(f.readlines()):
        line = line.rstrip('\n')
        for c, ch in enumerate(line):
            if ch in 'ABCD':
                pos = (r, c)
                if pos in g.vertices:
                    alias = g.vertices[pos].alias
                    state[alias] = ch
    return state


def show(g, state):
    for r in range(height):
        line = ''
        for c in range(width):
            pos = (r, c)
            if pos in g.vertices and g.vertices[pos].alias in state:
                alias = g.vertices[pos].alias
                line += state[alias]
            elif pos in g.vertices:
                line += g.vertices[pos].type
            else:
                line += ' '
        print(line)


def generate_moves(g, state):
    results = []
    for start_alias, piece in state.items():
        start_pos = g.aliases[start_alias]
        for end_alias in reachable_aliased_positions(g, state, start_pos):
            if square_type(g, start_alias) != square_type(g, end_alias):
                results.append( (start_alias, end_alias) )
    return results


def square_type(g, alias):
    if alias in '0123456':
        return 'hallway'
    elif alias in 'abcdefgh':
        return 'room'
    else:
        1/0


def reachable_aliased_positions(g, state, pos):
    visited = set()
    def dfs(g, state, pos):
        if g.vertices[pos].alias:
            yield g.vertices[pos].alias
        visited.add(pos)
        for v in g.neighbors[pos]:
            alias = g.vertices[v].alias
            occupant = state.get(alias) if alias else None
            if not occupant and v not in visited:
                yield from dfs(g, state, v)
    yield from dfs(g, state, pos)


class Graph:
    def __init__(self):
        self.vertices = {}
        self.neighbors = collections.defaultdict(set)
        self.aliases = {}


    def add_vertex(self, v, type, alias):
        assert v not in self.vertices
        assert alias not in self.aliases
        self.vertices[v] = obj(type=type, alias=alias)
        if alias is not None:
            self.aliases[alias] = v


    def add_edge(self, v, w):
        assert v in self.vertices
        assert w in self.vertices
        self.neighbors[v].add(w)
        self.neighbors[w].add(v)



if __name__ == '__main__':
    main()
