"""
Embarrassing: Backtracking is useful when you can eliminate partial solutions
as impossible (will never lead to a valid solution) before completing them
(which eliminates subtrees from your search). I'm not sure if this is possible
for this problem (TODO: Figure this out), but I didn't do it at all :) So this
is just brute force with extra steps -- and the runtime reflects this.
"""

import sys

from b_common import is_solved


abcdefg_string = 'abcdefg'
ABCDEFG_set = set('ABCDEFG')


def solve(patterns_seen):
    return backtracking_search({}, patterns_seen)

solve.name = 'backtracking search'


def backtracking_search(assignments, patterns_seen):
    if is_solved(assignments, patterns_seen):
        return assignments
    for left, right in child_nodes(assignments):
        assignments[left] = right
        solution = backtracking_search(assignments, patterns_seen)
        if solution:
            return solution
        del assignments[left]


def child_nodes(assignments):
    if len(assignments) == 7:
        return
    else:
        left = abcdefg_string[len(assignments)]
        right_options = sorted(ABCDEFG_set - set(assignments.values()))
        for right in right_options:
            yield (left, right)
