import sys


def main():
    f = open(sys.argv[1] if len(sys.argv) > 1 else 'in')
    lines = [l.rstrip('\n') for l in f]
    all_scores = []
    for line in lines:
        score, stack = get_score(line)
        if score == 0:
            total = 0
            for ch in reversed(stack):
                total *= 5
                total += get_points[get_other[ch]]
            all_scores.append(total)
    all_scores.sort()
    print(all_scores[len(all_scores) // 2])


def get_score(line):
    stack = []
    for ch in line:
        if ch in '([{<':
            stack.append(ch)
        else:
            expected_opener = get_other[ch]
            actual_opener = stack.pop()
            if actual_opener != expected_opener:
                return (get_points[ch], None)
    return (0, stack)


get_points = {  # Changed from part 1
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4,
}

get_other = {  # Finished (added "open -> close" cases) from part 1
    '(':')',
    '[':']',
    '{':'}',
    '<':'>',
    ')': '(',
    ']': '[',
    '}': '{',
    '>': '<',
}


if __name__ == '__main__':
    main()
