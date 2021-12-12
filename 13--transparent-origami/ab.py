import sys
from types import SimpleNamespace as obj


def main():
    f = open(sys.argv[1] if len(sys.argv) > 1 else 'in')
    dots, folds = f.read().strip().split('\n\n')
    dots = dots.strip().split('\n')
    folds = folds.strip().split('\n')

    dots = set(parse_dot(dot) for dot in dots)
    folds = [parse_fold(fold) for fold in folds]

    for i, fold in enumerate(folds):
        for dot in list(dots):
            x, y = dot
            if fold.is_x:
                if x > fold.coordinate:
                    new_x = 2 * fold.coordinate - x
                    dots.remove((x, y))
                    dots.add((new_x, y))
            else:
                if y > fold.coordinate:
                    new_y = 2 * fold.coordinate - y
                    dots.remove((x, y))
                    dots.add((x, new_y))
        if i == 0:
            print('Part 1:', len(dots))

    print('\nPart 2:')
    for y in range(6):
        line = ''
        for x in range(39):
            ch = '#' if (x, y) in dots else ' '
            line += ch
        print(line)


def parse_dot(dot):
    x,y = dot.split(',')
    return int(x), int(y)


def parse_fold(fold):
    coordinate = int(fold.split('=')[1])
    return obj(is_x='x' in fold, coordinate=coordinate)


if __name__ == '__main__':
    main()
