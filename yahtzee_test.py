import unittest

from yahtzee import *

class YahtzeeTestCase(unittest.TestCase):
    def test_ones(self):
        self.assertEqual(2, ones([1, 1, 2, 3, 4]))
        self.assertEqual(3, ones([1, 1, 1, 4, 5]))

    def test_twos(self):
        self.assertEqual(4, twos([1, 1, 2, 2, 4]))
        self.assertEqual(6, twos([2, 1, 2, 2, 4]))

    def test_threess(self):
        self.assertEqual(3, threes([1, 1, 2, 3, 4]))

if __name__ == '__main__':
    unittest.main()
