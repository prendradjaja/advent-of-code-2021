import sys


def main():
    f = open(sys.argv[1] if len(sys.argv) > 1 else 'in')
    lines = [l.rstrip('\n') for l in f]
    result = 0
    for line in lines:
        result += get_score(line)
    print(result)



def get_score(line):
    stack = []
    for ch in line:
        if ch in '([{<':
            stack.append(ch)
        else:
            expected_opener = get_other[ch]
            actual_opener = stack.pop()
            if actual_opener != expected_opener:
                return get_points[ch]
    return 0


get_points = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}

get_other = {
    ')': '(',
    ']': '[',
    '}': '{',
    '>': '<',
}






if __name__ == '__main__':
    main()
