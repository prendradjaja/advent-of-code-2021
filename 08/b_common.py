_number_to_segments = {}
_segments_to_number = {}
for line in open('numbers.txt'):
    number, segments = line.strip().split()
    number = int(number)
    _number_to_segments[number] = segments
    _segments_to_number[segments] = number


def is_solved(assignments, patterns_seen):
    if len(assignments) != 7:
        return False
    representable_numbers = set()
    for pattern in patterns_seen:
        segments = (assignments[signal] for signal in pattern)
        segments = ''.join(sorted(segments))
        if segments not in _segments_to_number:
            return False
        number = _segments_to_number[segments]
        representable_numbers.add(number)
    return len(representable_numbers) == 10


def decode_output(assignments, output_patterns):
    result = ''
    for pattern in output_patterns:
        result += str(decode_digit(assignments, pattern))
    return int(result)


def decode_digit(assignments, output_pattern):
    segments = (assignments[signal] for signal in output_pattern)
    segments = ''.join(sorted(segments))
    return _segments_to_number[segments]


