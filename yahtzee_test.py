import unittest


def ones(rolls):
    ones = filter(lambda roll: roll == 1, rolls)
    return sum(ones)


class YahtzeeTestCase(unittest.TestCase):
    def test_ones(self):
        self.assertEqual(2, ones([1, 1, 2, 3, 4]))
        self.assertEqual(3, ones([1, 1, 1, 4, 5]))


if __name__ == '__main__':
    unittest.main()
