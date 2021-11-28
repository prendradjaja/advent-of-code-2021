import unittest
from util import *

class TestMaybeInt(unittest.TestCase):
    def test_default_mode(self):
        self.assertEqual(12, maybeint('12'))
        self.assertEqual('yellow', maybeint('yellow'))
        with self.assertRaises(ValueError):
            maybeint('mixed12')

    def test_string_mode(self):
        mode = 'str'
        self.assertEqual(12, maybeint('12', mode))
        self.assertEqual('yellow', maybeint('yellow', mode))
        self.assertEqual('mixed12', maybeint('mixed12', mode))

    def test_int_mode(self):
        mode = 'int'
        self.assertEqual(12, maybeint('12', mode))
        self.assertEqual('yellow', maybeint('yellow', mode))
        self.assertEqual(12, maybeint('mixed12', mode))
        self.assertEqual(-12, maybeint('mixed-12', mode))

    def test_invalid_mode(self):
        mode = 'intt'
        self.assertEqual(12, maybeint('12', mode))
        self.assertEqual('yellow', maybeint('yellow', mode))
        with self.assertRaises(ValueError):
            maybeint('mixed12', mode)

class TestInts(unittest.TestCase):
    def test(self):
        self.assertEqual([12, 'yellow'], ints(['12', 'yellow']))

class TestFindInt(unittest.TestCase):
    def test(self):
        self.assertEqual(12, findint('mixed12'))

if __name__ == '__main__':
    unittest.main()
