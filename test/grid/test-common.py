import unittest
from grid import gridcustom
from examples import g, gcart

grid = gridcustom('ABCD', -1)

class TestCommon(unittest.TestCase):

    def test_add(self):
        self.assertEqual(
            grid.addvec((1, 2), (10, 20)),
            (11, 22))
        self.assertEqual(
            grid.addvec((1, 2, 3), (10, 20, 30)),

            (11, 22, 33))
    def test_mul(self):
        self.assertEqual(
            grid.mulvec((1, 2), 10),
            (10, 20))
        self.assertEqual(
            grid.mulvec((1, 2, 3), 10),
            (10, 20, 30))

    def test_index(self):
        g2d = [ [1, 2, 3],
                [4, 5, 6],
                [7, 8, 9], ]
        g3d = [g2d]
        self.assertEqual(6, grid.index(g2d, [1, 2]))
        self.assertEqual(6, grid.index(g3d, [0, 1, 2]))

    def test_setindex(self):
        g2d = [ [1, 2, 3],
                [4, 5, 6],
                [7, 8, 9], ]
        g3d = [g2d]
        grid.setindex(g2d, [1, 2], 0)
        self.assertEqual(0, grid.index(g2d, [1, 2]))
        grid.setindex(g3d, [0, 1, 2], -1)
        self.assertEqual(-1, grid.index(g3d, [0, 1, 2]))

    def test_absmanhattan(self):
        self.assertEqual(5, grid.absmanhattan([2, 3]))
        self.assertEqual(5, grid.absmanhattan([-2, 3]))
        self.assertEqual(5, grid.absmanhattan([-1, 1, 3]))

    def test_move_by_unitcvec(self):
        pos = (0, 0)
        pos = grid.move(pos, (1, 0), 3)
        pos = grid.move(pos, (0, 1), 2)
        self.assertEqual('a', grid.index(g, pos), 'Position is ' + str(pos))

if __name__ == '__main__':
    unittest.main()
