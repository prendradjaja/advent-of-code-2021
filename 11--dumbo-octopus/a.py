import sys, itertools
from grid import gridsource as grid
from termcolor import colored


verbose = False


def main():
    def step():
        nonlocal total_flash_count, last_flashes
        last_flashes = []

        for pos in energy:
            energy[pos] += 1

        # emulating `do ... while(any_flashed)`
        first = True
        any_flashed = False
        while first or any_flashed:
            any_flashed = False
            first = False
            for pos in energy:
                if energy[pos] > 9:
                    energy[pos] = float('-inf')  # Prevent this octopus from flashing again
                    any_flashed = True
                    last_flashes.append(pos)
                    total_flash_count += 1
                    # Propagate energy
                    for r, c in grid.neighbors(pos, True):
                        if 0 <= r < 10 and 0 <= c < 10:
                            energy[(r, c)] += 1

        for pos in last_flashes:
            energy[pos] = 0


    def show():
        for r in range(10):
            row = ''
            for c in range(10):
                val = str(energy[(r, c)])
                if (r, c) in last_flashes:
                    val = colored(val, 'red')
                row += val
            print(row)
        print()


    ###########################################################################


    f = open(sys.argv[1] if len(sys.argv) > 1 else 'in')
    lines = [l.rstrip('\n') for l in f]

    # Parse
    energy = {}
    for r, line in enumerate(lines):
        for c, val in enumerate(line):
            val = int(val)
            energy[(r, c)] = val

    total_flash_count = 0
    last_flashes = []  # Positions of the flashes in just the last step

    if not verbose:
        for i in range(100):
            step()
        print(total_flash_count)
    else:
        print('Before any steps:')
        show()
        for i in range(10):
            step()
            print(f'After step {i+1}:')
            show()
        for j in range(9):
            for k in range(10):
                step()
                i += 1
            print(f'After step {i+1}:')
            show()
        print('Answer:')
        print(total_flash_count)


if __name__ == '__main__':
    main()
