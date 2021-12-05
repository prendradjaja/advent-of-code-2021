"""
Solve with three different methods. The answer should be the same each time.
"""

import sys
import time

import b1__handwritten_deduction as b1
import b2__backtacking_search as b2
import b3__try_all_permutations as b3

from b_common import decode_output


def main():
    f = open(sys.argv[1] if len(sys.argv) > 1 else 'in')
    lines = [l.rstrip('\n') for l in f]

    solvers = [b1.solve, b2.solve, b3.solve]

    max_length = max(len(solve.name) for solve in solvers)

    for solve in solvers:
        method = solve.name.ljust(max_length)
        answer = 0
        start = time.time()
        for line in lines:
            # Parse
            patterns_seen, output_patterns = line.split('|')
            patterns_seen = patterns_seen.strip().split()
            output_patterns = output_patterns.strip().split()
            # Solve and decode
            assignments = solve(patterns_seen)
            answer += decode_output(assignments, output_patterns)
        end = time.time()
        print(f'Answer via {method} = {answer}    (Elapsed time: {end - start:0.3f}sec)')


if __name__ == '__main__':
    main()
