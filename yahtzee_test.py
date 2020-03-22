import unittest

from yahtzee import *

class YahtzeeTestCase(unittest.TestCase):
    def test_ones(self):
        self.assertEqual(2, ones([1, 1, 2, 3, 4]))
        self.assertEqual(3, ones([1, 1, 1, 4, 5]))

    def test_twos(self):
        self.assertEqual(4, twos([1, 1, 2, 2, 4]))
        self.assertEqual(6, twos([2, 1, 2, 2, 4]))

    def test_threes(self):
        self.assertEqual(3, threes([1, 1, 2, 3, 4]))

    def test_fours(self):
        self.assertEqual(8, fours([1, 4, 2, 3, 4]))

    def test_fives(self):
        self.assertEqual(10, fives([1, 4, 5, 3, 5]))

    def test_sixes(self):
        self.assertEqual(12, sixes([6, 6, 5, 3, 5]))

    def test_pair(self):
        self.assertEqual(8, pair([3, 3, 3, 4, 4]))

    def test_three_of_a_kind(self):
        self.assertEqual(9, three_of_a_kind([3, 3, 3, 4, 5]))
        self.assertEqual(0, three_of_a_kind([1, 2, 3, 4, 5]))

    def test_four_of_a_kind(self):
        self.assertEqual(8, four_of_a_kind([2, 2, 2, 2, 5]))

    def test_small_straight(self):
        self.assertEqual(15, small_straight([1, 2, 3, 4, 5]))
        self.assertEqual(0, small_straight([2, 3, 4, 5, 6]))

    def test_large_straight(self):
        self.assertEqual(20, large_straight([2, 3, 4, 5, 6]))
        self.assertEqual(0, large_straight([1, 2, 3, 4, 5]))

    def test_full_house(self):
        self.assertEqual(8, full_house([1, 1, 2, 2, 2]))
        self.assertEqual(0, full_house([4, 4, 4, 4, 4]))

    def test_yahtzee(self):
        self.assertEqual(50, yahtzee([3, 3, 3, 3, 3]))
        self.assertEqual(0, yahtzee([1, 3, 3, 3, 3]))

    def test_count_dice_values(self):
        result = count_dice([3, 3, 1, 4, 5])
        self.assertEqual([1, 0, 2, 1, 1, 0], result)

if __name__ == '__main__':
    unittest.main()
