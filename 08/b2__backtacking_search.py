import sys

from b_common import is_solved


def solve(patterns_seen):
    return backtracking_search({}, patterns_seen)


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
        return []
    else:
        left = 'abcdefg'[len(assignments)]
        right_options = sorted(set('ABCDEFG') - set(assignments.values()))
        return [(left, right) for right in right_options]
