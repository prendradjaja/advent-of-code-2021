import sys
from util import findints, transpose


def main():
    f = open(sys.argv[1] if len(sys.argv) > 1 else 'in')
    calls, *cardnums = f.read().strip().split('\n\n')
    calls = findints(calls)

    cards = []
    curr = []
    for text in cardnums:
        for line in text.strip().split('\n'):
            curr.append(findints(line))
        cards.append(Card(curr))
        curr = []

    won = set()

    for n in calls:
        for card in cards:
            card.call(n)
            if card.done():
                items = flatten(card.items)
                if card not in won:
                    print(sum(x for x in items if x != None) * n)
                won.add(card)
    print('The last line of output above is the answer')

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

