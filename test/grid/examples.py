# For use with gridsource and gridcardinal
g = [
  'o.........',
  '.b........',
  '..........',
  '..a.......',
  '..........',
]

# For use with gridcartesian
def gcart(pos):
    """
    ^
    |.a.
    |...
    |b..
    o--->
    """
    if pos == (2, 3):
        return 'a'
    elif pos == (1, 1):
        return 'b'
    else:
        return '.'
