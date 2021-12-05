import sys

import b1__handwritten_deduction as b1
import b2__backtacking_search as b2
import b3__try_all_permutations as b3

from b_common import decode_output


def main():
    f = open(sys.argv[1] if len(sys.argv) > 1 else 'in')
    lines = [l.rstrip('\n') for l in f]

    print('Answer: (Repeated three times: Should be the same each time)')

    for solve in [b1.solve, b2.solve, b3.solve]:
        answer = 0
        for line in lines:
            # Parse
            patterns_seen, output_patterns = line.split('|')
            patterns_seen = patterns_seen.strip().split()
            output_patterns = output_patterns.strip().split()
            # Solve and decode
            assignments = solve(patterns_seen)
            answer += decode_output(assignments, output_patterns)
        print(answer)


if __name__ == '__main__':
    main()
