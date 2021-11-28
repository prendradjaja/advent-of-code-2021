import sys
import collections as cl


def main():
    f = open(sys.argv[1] if len(sys.argv) > 1 else 'in')
    lines = [l.rstrip('\n') for l in f]
    g = get_rating(lines, True)
    e = get_rating(lines, False)
    print(g * e)

def get_rating(lines, is_most):
    for c in rangelen(lines[0]):
        umpth = get_umpth_common(lines, c, is_most)
        lines = [L for L in lines if L[c] == umpth]
        if len(lines) == 1:
            return int(lines[0], 2)

def get_umpth_common(lines, column, is_most):
    values = [line[column] for line in lines]
    most_common, count = cl.Counter(values).most_common(1)[0]
    if count * 2 == len(values):
        return str(int(is_most))
    elif is_most:
        return most_common
    else:
        return other(most_common)

def rangelen(lst):
    return range(len(lst))

def other(s):
    return '0' if s == '1' else '1'


if __name__ == '__main__':
    main()
