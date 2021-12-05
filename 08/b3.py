import sys
import itertools
import util


def main():
    # Parse numbers.txt
    global number_to_segments, segments_to_number
    number_to_segments, segments_to_number = parse_numbers_file()

    f = open(sys.argv[1] if len(sys.argv) > 1 else 'in')
    lines = [l.rstrip('\n') for l in f]
    answer = 0
    for line in lines:
        # Parse
        patterns_seen, output_patterns = line.split('|')
        patterns_seen = patterns_seen.strip().split()
        output_patterns = output_patterns.strip().split()

        # Solve and decode
        assignments = solve(patterns_seen)
        number = decode_output(assignments, output_patterns)
        answer += number

    print(answer)


def solve(patterns_seen):
    patterns_seen = [sort_string(p) for p in patterns_seen]
    assignments = {}

    # *** can identify 1478
    one = util.one([p for p in patterns_seen if len(p) == 2])
    four = util.one([p for p in patterns_seen if len(p) == 4])
    seven = util.one([p for p in patterns_seen if len(p) == 3])
    eight = util.one([p for p in patterns_seen if len(p) == 7])

    # *** A (7-1)
    A = util.one(set(seven) - set(one))
    assignments[A] = 'A'

    # *** G (9-(7+4)) -- can identify 9 because it contains 4
    nine = util.one([p for p in patterns_seen if len(p) == 6 and set(p) > set(four)])
    G = util.one(set(nine) - (set(seven) | set(four)))
    assignments[G] = 'G'

    # *** E (8-9)
    E = util.one(set(eight) - set(nine))
    assignments[E] = 'E'

    # *** B (8-3-E) -- can identify 3 because it contains 1
    three = util.one([p for p in patterns_seen if len(p) == 5 and set(p) > set(one)])
    B = util.one(set(eight) - set(three) - {E})
    assignments[B] = 'B'

    # *** D (8-0) -- can identify 0 because it contains 1 and is not 9
    zero = util.one([p for p in patterns_seen if len(p) == 6 and set(p) > set(one) and p != nine])
    D = util.one(set(eight) - set(zero))
    assignments[D] = 'D'

    # *** C (8-6) -- can identify 6 because its not 0 or 9
    six = util.one([p for p in patterns_seen if len(p) == 6 and p != nine and p != zero])
    C = util.one(set(eight) - set(six))
    assignments[C] = 'C'

    # *** F -- it's the last one
    F = util.one(set('abcdefg') - set(assignments))
    assignments[F] = 'F'

    return assignments


def sort_string(s):
    return ''.join(sorted(s))


def decode_output(assignments, output_patterns):
    result = ''
    for pattern in output_patterns:
        result += str(decode_digit(assignments, pattern))
    return int(result)


def decode_digit(assignments, output_pattern):
    segments = (assignments[signal] for signal in output_pattern)
    segments = ''.join(sorted(segments))
    return segments_to_number[segments]


def parse_numbers_file():
    number_to_segments = {}
    segments_to_number = {}
    for line in open('numbers.txt'):
        number, segments = line.strip().split()
        number = int(number)
        number_to_segments[number] = segments
        segments_to_number[segments] = number
    return number_to_segments, segments_to_number


if __name__ == '__main__':
    main()
