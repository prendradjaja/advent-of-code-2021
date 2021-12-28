import sys
from grid import gridsource as grid
from extras import show


NEIGHBORHOOD_OFFSETS = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1),  (0, 0),  (0, 1),
    (1, -1),  (1, 0),  (1, 1),
]


def main():
    # Parse
    f = open(sys.argv[-1] if len(sys.argv) > 1 and sys.argv[-1] != '-' else 'in')
    rules = f.readline().rstrip('\n')
    f.readline()  # skip blank line
    raw_image = [line.rstrip('\n') for line in f.readlines()]

    # Validate
    assert set(rules) <= set('.#')
    assert len(rules) == 512

    steps = 2
    padding = steps + 2  # Does just steps + 1 work?
    image = Image(raw_image, padding)
    for i in range(steps):
        print(f'\rStep {i+1} of {steps}', end='')
        image.step(rules)
    print('\rAnswer:                    ')
    print(len([None for value in flatten(image.pixels) if value == '#']))


class Image:
    def __init__(self, raw_image, padding):
        self.padding = padding
        self.inner_height = len(raw_image)
        self.inner_width = len(raw_image[0])
        self.outer_height = self.inner_height + 2 * padding
        self.outer_width = self.inner_width + 2 * padding
        self.background = '.'

        self.pixels = []
        for _ in range(padding):
            row = ['.' for _ in range(self.outer_width)]
            self.pixels.append(row)
        for raw_row in raw_image:
            row = ['.' for _ in range(padding)] + list(raw_row) + ['.' for _ in range(padding)]
            self.pixels.append(row)
        for _ in range(padding):
            row = ['.' for i in range(self.outer_width)]
            self.pixels.append(row)


    def step(self, rules):
        new_pixels = [[None] * self.outer_width for _ in range(self.outer_height)]
        for r, row in enumerate(self.pixels):
            for c, _ in enumerate(row):
                neighborhood_value = self.neighborhood_value((r, c))
                new_pixels[r][c] = rules[neighborhood_value]
        self.pixels = new_pixels

        assert self.background in '.#'
        key = 0 if self.background == '.' else 511
        self.background = rules[key]


    def neighborhood_value(self, pos):
        result = ''
        for offset in NEIGHBORHOOD_OFFSETS:
            neighbor = grid.addvec(pos, offset)
            r, c = neighbor
            if self.in_bounds(neighbor):
                value = self.pixels[r][c]
            else:
                value = self.background
            result += '0' if value == '.' else '1'
        return int(result, 2)


    def in_bounds(self, pos):
        r, c = pos
        return 0 <= r < self.outer_height and 0 <= c < self.outer_width


def flatten(t):
    return [item for sublist in t for item in sublist]


if __name__ == '__main__':
    main()
