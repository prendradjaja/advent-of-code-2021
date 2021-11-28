import unittest
from grid import gridplane as grid
from examples import g, gcart

class TestPlane(unittest.TestCase):

    def test_move_by_name(self):
        pos = (0, 0)
        pos = grid.move(pos, 'U', 3)
        pos = grid.move(pos, 'R', 2)
        self.assertEqual('a', gcart(pos), 'Position is ' + str(pos))
        pos = grid.move(pos, 'D', 2)
        pos = grid.move1(pos, 'L')
        self.assertEqual('b', gcart(pos), 'Position is ' + str(pos))

    def test_rotation(self):
        pos = (0, 0)
        curdir = grid.tovec['U']

        # Can rotate R
        pos = grid.move(pos, curdir, 3)
        curdir = grid.rot(curdir, 'R')
        pos = grid.move(pos, curdir, 2)
        self.assertEqual('a', gcart(pos), 'Position is ' + str(pos))

        # Can rotate L
        curdir = grid.rot(curdir, 'L')
        curdir = grid.rot(curdir, 'L')
        pos = grid.move1(pos, curdir)
        curdir = grid.rot(curdir, 'L')
        pos = grid.move(pos, curdir, 2)
        self.assertEqual('b', gcart(pos), 'Position is ' + str(pos))

if __name__ == '__main__':
    unittest.main()
