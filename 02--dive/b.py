import sys


def main():
    f = open(sys.argv[1] if len(sys.argv) > 1 else 'in')
    lines = [l.rstrip('\n') for l in f]
    x = 0
    y = 0
    aim = 0
    for line in lines:
        word, d = line.strip().split()
        d = int(d)
        if word == 'forward':
            x += d
            y += aim * d
        elif word == 'down':
            aim += d
        elif word == 'up':
            aim -= d
        else:
            1/0
    print(x*y)

if __name__ == '__main__':
    main()
