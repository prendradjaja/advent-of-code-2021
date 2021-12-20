def _use_block_0(self, rules):
    new_pixels = [[None] * self.outer_width for _ in range(self.outer_height)]
    for r, row in enumerate(self.pixels):
        for c, _ in enumerate(row):
            neighborhood_value = self.neighborhood_value((r, c))
            new_pixels[r][c] = rules[neighborhood_value]
    # new_pixels[self.padding + 2][self.padding + 2] = '?'
    return new_pixels
def _use_block_1(background, rules):
    assert background in '.#'
    key = 0 if background == '.' else 511
    return rules[key]

import fileinput, collections, collections as cl, itertools, itertools as it, math, random, sys, re, string, functools
from grid import gridsource as grid, gridcustom # *, gridsource, gridcardinal, gridplane
from util import *
def main():
    f = open(sys.argv[-1] if len(sys.argv) > 1 and sys.argv[-1] != '-' else 'in')
    rules = f.readline().rstrip('\n')
    assert set(rules) <= set('.#')
    assert len(rules) == 512
    # rules = '#' + rules[1:-1] + '.'
    assert len(rules) == 512
    f.readline()  # ignore blank line
    raw = [line.rstrip('\n') for line in f.readlines()]
    # raw = ['#.#', '.#.', '###']
    padding = 4
    image = Image(raw, padding)
    image.show()
    image.step(rules)
    image.show()
    image.step(rules)
    image.show()
    print(len([None for value in flatten(image.pixels) if value == '#']))
def other(pixel):
    assert pixel in '.#'
    return '#' if pixel == '.' else '.'
def to_digit(pixel):
    assert pixel in '.#'
    return '0' if pixel == '.' else '1'
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
            row = ['.' for i in range(self.outer_width)]
            self.pixels.append(row)
        for raw_row in raw_image:
            row = []
            for _ in range(padding):
                row.append('.')
            for pixel in raw_row:
                row.append(pixel)
            for _ in range(padding):
                row.append('.')
            self.pixels.append(row)
        for _ in range(padding):
            row = ['.' for i in range(self.outer_width)]
            self.pixels.append(row)
    def step(self, rules):
        self.pixels = _use_block_0(self, rules)
        background = self.background
        self.background = _use_block_1(background, rules)
    def neighborhood_value(self, pos):
        interesting = False
        r, c = pos
        if r == self.padding + 0 and c == self.padding + 0:
            interesting = True
            interesting = False
        result = ''
        neivecs = [
                (-1, -1), (-1, 0), (-1, 1),
                (0, -1),  (0, 0),  (0, 1),
                (1, -1),  (1, 0),  (1, 1) ]
        for offset in neivecs:
            neighbor = grid.addvec(pos, offset)
            r, c = neighbor
            if self.in_bounds(neighbor):
                value = self.pixels[r][c]
                if interesting:
                    print(value)
            else:
                value = self.background
            result += to_digit(value)
        if interesting:
            print(result)
        return int(result, 2)
    def show(self):
        border_width = self.outer_width + 4
        border_height = self.outer_height + 4
        border_inner_width = self.outer_width + 2
        border_inner_height = self.outer_height + 2
        print(self.background * border_width)
        print(self.background + (' ' * border_inner_width) + self.background)
        for row in self.pixels:
            print(self.background + ' ', end='')
            print(''.join(row), end='')
            print(' ' + self.background, end='')
            print()
        print(self.background + (' ' * border_inner_width) + self.background)
        print(self.background * border_width)
    def in_bounds(self, pos):
        r, c = pos
        return 0 <= r < self.outer_height and 0 <= c < self.outer_width
    # def count_lit(self):
    #     return 
if __name__ == '__main__':
    main()
