import sys
from util import findints, transpose


def main():
    calls = [59,91,13,82,8,32,74,96,55,51,19,47,46,44,5,21,95,71,48,60,68,81,80,14,23,28,26,78,12,22,49,1,83,88,39,53,84,37,93,24,42,7,56,20,92,90,25,36,34,52,27,50,85,75,89,63,33,4,66,17,98,57,3,9,54,0,94,29,79,61,45,86,16,30,77,76,6,38,70,62,72,43,69,35,18,97,73,41,40,64,67,31,58,11,15,87,65,2,10,99]

    f = open(sys.argv[1] if len(sys.argv) > 1 else 'in')
    lines = [l.rstrip('\n') for l in f]
    cards = []
    curr = []
    for line in lines:
        if line:
            curr.append(findints(line))
        else:
            cards.append(Card(curr))
            curr = []

    for n in calls:
        for card in cards:
            card.call(n)
            if card.done():
                items = flatten(card.items)
                print(sum(x for x in items if x != None) * n)
                exit()

def flatten(t):
    return [item for sublist in t for item in sublist]



class Card:
    def __init__(self, items):
        self.items = items
        self.picked = [[False] * 5 for _ in range(5)]

    def call(self, n):
        for r, row in enumerate(self.items):
            for c, item in enumerate(row):
                if item == n:
                    # self.picked[r][c] = True
                    self.items[r][c] = None

    def done(self):
        for row in self.items:
            if all(item == None for item in row):
                return True
        for row in transpose(self.items):
            if all(item == None for item in row):
                return True

if __name__ == '__main__':
    main()
