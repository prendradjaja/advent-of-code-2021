import fileinput, collections, collections as cl, itertools, itertools as it, math, random, sys, re, string, functools
from grid import gridsource as grid, gridcustom # *, gridsource, gridcardinal, gridplane
from util import *
import heapq


# type Pos = (r: int, c: int)
# type Alias = '.' | 'a' | ... | 'h' | '0' | ... | '6'
# type State = { [key: Alias]: 'A' | 'B' | 'C' | 'D' }
# type Move = (start: Alias, end: Alias)

width = 13
height = 5

border = [ (0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (0, 9), (0, 10), (0, 11), (0, 12), (1, 0), (1, 12), (2, 0), (2, 1), (2, 2), (2, 4), (2, 6), (2, 8), (2, 10), (2, 11), (2, 12), (3, 2), (3, 4), (3, 6), (3, 8), (3, 10), (4, 2), (4, 3), (4, 4), (4, 5), (4, 6), (4, 7), (4, 8), (4, 9), (4, 10), ]



def main():
    g, state = parse_input()
    show(g, state)

    # # movegen example
    # del state['b']
    # # del state['f']
    # state['3'] = 'C'
    # show(g, state)
    # print(generate_moves(g, state))

    def bfs(state):
        state_hashable = to_hashable(state)
        parents[state_hashable] = None
        visited.add(state_hashable)
        h = [(0, state_hashable)]
        heapq.heapify(h)
        i = 0
        show_every = 1000
        while h:
            cumulative_cost, state_hashable = heapq.heappop(h)
            i += 1
            if i % show_every == 0:
                print('...', i // show_every, cumulative_cost)
            state = from_hashable(state_hashable)
            if is_goal(state):
                print(cumulative_cost, f'({i} states searched)')
                show(g, state)
                # show_steps(state_hashable, parents, g)
                exit()
            for v, move in neighbors(g, state):
                v_hashable = to_hashable(v)
                if v_hashable not in visited:
                    parents[v_hashable] = state_hashable
                    visited.add(v_hashable)
                    heapq.heappush(h, (edge_cost(g, move, state) + cumulative_cost, v_hashable))
    visited = set()
    parents = {}
    bfs(state)


def show_steps(state_hashable, parents, g):
    states = []
    while state_hashable:
        states.append(from_hashable(state_hashable))
        state_hashable = parents[state_hashable]
    states = states[::-1]
    for state in states:
        show(g, state)



def edge_cost(g, move, state):
    '''
    Given STATE, return the cost of making MOVE
    '''
    start_alias, end_alias = move
    start_pos = g.aliases[start_alias]
    end_pos = g.aliases[end_alias]
    r1, c1 = start_pos
    r2, c2 = end_pos

    piece_type = state[start_alias]
    cost_per_move = {'A': 1, 'B': 10, 'C': 100, 'D': 1000}[piece_type]

    # Manhattan distance
    return cost_per_move * (abs(r1 - r2) + abs(c1 - c2))


def neighbors(g, state):
    for move in generate_moves(g, state):
        new_state = dict(state)
        apply_move(g, new_state, move)
        yield new_state, move


def apply_move(g, state, move):
    '''
    Apply MOVE, mutating STATE and returning cost
    '''
    cost = edge_cost(g, move, state)
    start, end = move
    state[end] = state[start]
    del state[start]
    apply_move.total += cost
    return cost
apply_move.total = 0


def to_hashable(state):
    return tuple(sorted(state.items()))


def from_hashable(state_hashable):
    return {k: v for k, v in state_hashable}


def is_goal(state):
    return (
        '0' not in state and
        '1' not in state and
        '2' not in state and
        '3' not in state and
        '4' not in state and
        '5' not in state and
        '6' not in state and
        state['a'] == 'A' and
        state['b'] == 'B' and
        state['c'] == 'C' and
        state['d'] == 'D' and
        state['e'] == 'A' and
        state['f'] == 'B' and
        state['g'] == 'C' and
        state['h'] == 'D'
    )


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


def parse_input(inputstr=None):
    g = parse_layout()
    state = {}
    if not inputstr:
        f = open(sys.argv[1] if len(sys.argv) > 1 else 'in')
        lines = f.readlines()
    else:
        inputstr = inputstr.strip()
        lines = inputstr.split('\n')
    for r, line in enumerate(lines):
        line = line.rstrip('\n')
        for c, ch in enumerate(line):
            if ch in 'ABCD':
                pos = (r, c)
                if pos in g.vertices:
                    alias = g.vertices[pos].alias
                    state[alias] = ch
    return g, state


def show(g, state, *, with_border=False):
    for r in range(height):
        line = ''
        for c in range(width):
            pos = (r, c)
            if pos in g.vertices and g.vertices[pos].alias in state:
                alias = g.vertices[pos].alias
                line += state[alias]
            elif pos in g.vertices:
                line += g.vertices[pos].type
            elif with_border and pos in border:
                line += '#'
            else:
                line += ' '
        line = line.rstrip(' ')
        print(line)


def generate_moves(g, state):
    results = []

    for start_alias, piece in state.items():
        start_pos = g.aliases[start_alias]
        for end_alias in reachable_aliased_positions(g, state, start_pos):
            if square_type(g, start_alias) == square_type(g, end_alias):
                continue

            piece_type = state[start_alias]

            # Moving into a room
            if (
                square_type(g, end_alias) == 'room'
            ):
                # It's the wrong type
                if piece_type != room_name_to_amphipod_type(end_alias):
                    continue

                # It's the right type, but there is a deeper square in the room...
                elif end_alias in 'abcd':
                    my_deeper_square = deeper_square(end_alias) if end_alias in 'abcd' else None

                    # ...which is unoccupied
                    if deeper_square(end_alias) not in state:
                        continue

                    # ...which is occupied by an amphipod of the wrong type
                    elif state[my_deeper_square] != piece_type:
                        continue

                    # ...which is occupied by an amphipod of the right type
                    else:
                        pass

                # It's the right type, and there is no deeper square in the room
                else:
                    pass

            # Moving into a hallway
            else:

                # It's already home...
                if room_name_to_amphipod_type(start_alias) == piece_type:

                    my_deeper_square = deeper_square(start_alias) if start_alias in 'abcd' else None

                    # ...and in the deepest position
                    if start_alias in 'efgh':
                        continue

                    # ...and the deeper position is occupied by an amphipod of the same (right) type
                    elif my_deeper_square in state and state[my_deeper_square] == piece_type:
                        continue

            results.append( (start_alias, end_alias) )
    return results


def room_name_to_amphipod_type(alias):
    '''
    >>> room_name_to_amphipod_type('b')
    'B'
    >>> room_name_to_amphipod_type('f')
    'B'
    '''
    assert alias in 'abcdefgh'
    if alias in 'efgh':
        alias = 'abcd'['efgh'.index(alias)]
    return alias.upper()


def deeper_square(abcd):
    assert abcd in 'abcd'
    return 'efgh'['abcd'.index(abcd)]


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
