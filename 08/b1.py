import sys
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
        answer += decode_output(assignments, output_patterns)

    print(answer)


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


def is_solved(assignments, patterns_seen):
    if len(assignments) != 7:
        return False
    representable_numbers = set()
    for pattern in patterns_seen:
        segments = (assignments[signal] for signal in pattern)
        segments = ''.join(sorted(segments))
        if segments not in segments_to_number:
            return False
        number = segments_to_number[segments]
        representable_numbers.add(number)
    return len(representable_numbers) == 10


def child_nodes(assignments):
    if len(assignments) == 7:
        return []
    else:
        left = 'abcdefg'[len(assignments)]
        right_options = sorted(set('ABCDEFG') - set(assignments.values()))
        return [(left, right) for right in right_options]


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
