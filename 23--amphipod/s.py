import fileinput, collections, collections as cl, itertools, itertools as it, math, random, sys, re, string, functools
from grid import gridsource as grid, gridcustom # *, gridsource, gridcardinal, gridplane
from util import *
import heapq
from dijkstra_gribouillis import Dijkstra


# type Pos = (r: int, c: int)
# type Alias = '.' | 'a' | ... | 'h' | '0' | ... | '6'
# type State = { [key: Alias]: 'A' | 'B' | 'C' | 'D' }
# type Move = (start: Alias, end: Alias)

width = 13
height = 5
abcdefghijklmnop = 'abcdefghijklmnop'

border = [ (0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (0, 9), (0, 10), (0, 11), (0, 12), (1, 0), (1, 12), (2, 0), (2, 1), (2, 2), (2, 4), (2, 6), (2, 8), (2, 10), (2, 11), (2, 12), (3, 2), (3, 4), (3, 6), (3, 8), (3, 10), (4, 2), (4, 3), (4, 4), (4, 5), (4, 6), (4, 7), (4, 8), (4, 9), (4, 10), ]

solved = tuple(zip(abcdefghijklmnop, itertools.cycle('ABCD')))
# solved = (('a', 'A'), ('b', 'B'), ('c', 'C'), ('d', 'D'), ('e', 'A'), ('f', 'B'), ('g', 'C'), ('h', 'D'))
# solved_mini = (('e', 'A'), ('f', 'B'))


def main():
    g, state=parse_input()
    target = solved

#     g, state=parse_input('''
# #############
# #AA.D.....AD#
# ###.#B#C#.###
#   #.#B#C#.#
#   #.#B#C#D#
#   #A#B#C#D#
#   #########
#     ''')

#     g, state=parse_input('''
# #############
# #A..D.....AD#
# ###.#B#C#.###
#   #.#B#C#.#
#   #A#B#C#D#
#   #A#B#C#D#
#   #########
#     ''')

    # print(generate_moves(g, state))
    # print(deepest_unoccupied_square('A', state))
    # return

#     g, state = parse_input('''
# #############
# #...........#
# ###A#.#.#.###
#   #B#.#.#.#
#   #########
#     ''')
#     target = solved_mini

    # show(g, state)

    start = to_hashable(state)
    def neighs(state):
        state = from_hashable(state)
        result = []
        for new_state, move in neighbors(g, state):
            cost = edge_cost(g, move, state)
            result.append( (cost, to_hashable(new_state), move) )
        return result
    d = Dijkstra(start, neighs, target=target, maxitems=None)
    assert d.is_shortest(target)
    print(d[target].dist)

    # for k in d.rev_path_to(target):
    #     print(k, d[k].edge)

    # for item in d:
    #     show(g, from_hashable(item))

    # print(d[start])
    # for dist, n, edge in neighs(start):
    #     print(d[n])



    # # movegen example
    # del state['b']
    # # del state['f']
    # state['3'] = 'C'
    # show(g, state)
    # print(generate_moves(g, state))

    # def bfs(state):
    #     state_hashable = to_hashable(state)
    #     parents[state_hashable] = None
    #     visited.add(state_hashable)
    #     h = [(0, state_hashable)]
    #     heapq.heapify(h)
    #     i = 0
    #     show_every = 1000
    #     while h:
    #         cumulative_cost, state_hashable = heapq.heappop(h)
    #         i += 1
    #         if i % show_every == 0:
    #             print('...', i // show_every, cumulative_cost)
    #         state = from_hashable(state_hashable)
    #         my_other_interesting = (('e', 'A'), ('f', 'B'))
    #         if state_hashable == my_other_interesting:
    #             pass
    #             # show_steps(state_hashable, parents, g)
    #             # # print(cumulative_cost)
    #             # exit()
    #
    #         # my_interesting = (('1', 'A'), ('e', 'B'))
    #         # my_interesting = (('1', 'A'), ('2', 'B'))
    #         # my_interesting = (('1', 'A'), ('f', 'B'))
    #         my_interesting = 'x'
    #         if state_hashable == my_interesting:
    #             interesting = True
    #             print('cumulcost', cumulative_cost)
    #         else:
    #             interesting = False
    #         if is_goal(state):
    #             print(cumulative_cost, f'({i} states searched)')
    #             show(g, state)
    #             show_steps(state_hashable, parents, g)
    #             exit()
    #         # if interesting:
    #         #     print(list(neighbors(g, state)))
    #         for v, move in neighbors(g, state):
    #             v_hashable = to_hashable(v)
    #             if interesting:
    #                 print('possible move', move, v_hashable)
    #             if v_hashable not in visited:
    #                 if interesting:
    #                     print(move, end=' ')
    #                 parents[v_hashable] = state_hashable
    #                 visited.add(v_hashable)
    #                 heapq.heappush(h, (edge_cost(g, move, state) + cumulative_cost, v_hashable))
    #                 # print(edge_cost(g, move, state) + cumulative_cost, move, state_hashable)
    #         if interesting:
    #             print()
    # visited = set()
    # parents = {}
    # bfs(state)


def show_steps(state_hashable, parents, g):
    print('Steps:')
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
        state.get('a', '-') in 'A-' and
        state.get('b', '-') in 'B-' and
        state.get('c', '-') in 'C-' and
        state.get('d', '-') in 'D-' and
        state.get('e', '-') in 'A-' and
        state.get('f', '-') in 'B-' and
        state.get('g', '-') in 'C-' and
        state.get('h', '-') in 'D-'
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
            elif ch in '.abcdefghijklmnop0123456':
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
    # print('generate_moves:')
    results = []

    for start_alias, piece in state.items():
        start_pos = g.aliases[start_alias]
        reachable = reachable_aliased_positions(g, state, start_pos)
        for end_alias in reachable:
            # print('reachable', start_alias, end_alias)

            # # *************************************************
            # # this didn't seem to be necessary, but i wonder if it would be if i implemented my own dijkstra
            # if start_alias == end_alias:
            #     continue
            # # *************************************************

            if square_type(g, start_alias) == square_type(g, end_alias):
                continue

            piece_type = state[start_alias]

            # if start_alias == '1' and end_alias == 'i':
            #     print(deepest_unoccupied_square(piece_type, state))

            # Moving into a room
            if (
                square_type(g, end_alias) == 'room'
            ):
                # It's the wrong type
                if piece_type != room_name_to_amphipod_type(end_alias):
                    continue


# success condition:
# is filled only with things of the right type AND
# is deepest unoccupied

                elif not (
                    only_correct_type(piece_type, state) and
                    end_alias == deepest_unoccupied_square(piece_type, state)
                ):
                    continue

            # Moving into a hallway
            else:

                # It's already home...
                if room_name_to_amphipod_type(start_alias) == piece_type:

                    # ...and everything here is the correct type
                    if only_correct_type(piece_type, state):
                        continue

            # results.append( start_alias + end_alias )
            results.append( (start_alias , end_alias) )
    return results


def room_squares(mytype):
    assert mytype in 'ABCD'
    return reversed(['aeim', 'bfjn', 'cgko', 'dhlp']['ABCD'.index(mytype)])
    # return reversed(['ae', 'bf', 'cg', 'dh']['ABCD'.index(mytype)])


def only_correct_type(mytype, state):
    for alias in room_squares(mytype):
        if alias in state:
            if state[alias] != mytype:
                return False
    return True


def deepest_unoccupied_square(mytype, state):
    for alias in room_squares(mytype):
        if alias not in state:
            return alias
    assert False  # i think this should be unreachable


def room_name_to_amphipod_type(alias):
    '''
    >>> room_name_to_amphipod_type('b')
    'B'
    >>> room_name_to_amphipod_type('k')
    'C'
    '''
    assert alias in abcdefghijklmnop
    alias = 'abcd'[abcdefghijklmnop.index(alias) % 4]
    return alias.upper()


# def deeper_square(abcd):
#     assert abcd in 'abcd'
#     return 'efgh'['abcd'.index(abcd)]


def square_type(g, alias):
    if alias in '0123456':
        return 'hallway'
    elif alias in abcdefghijklmnop:
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
