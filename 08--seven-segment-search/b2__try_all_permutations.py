import sys
import itertools

from b_common import is_solved


def solve(patterns_seen):
    for assignments in all_possibilities():
        if is_solved(assignments, patterns_seen):
            return assignments

solve.name = 'trying all permutations'


def all_possibilities():
    for perm in itertools.permutations('abcdefg'):
        yield { left: right for left, right in zip(perm, 'ABCDEFG') }
