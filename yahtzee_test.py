import unittest


def ones(rolls):
    return sum(filter(lambda roll: roll == 1, rolls))


def twos(rolls):
    return sum(filter(lambda roll: roll == 2, rolls))


class YahtzeeTestCase(unittest.TestCase):
    def test_ones(self):
        self.assertEqual(2, ones([1, 1, 2, 3, 4]))
        self.assertEqual(3, ones([1, 1, 1, 4, 5]))

    def test_twos(self):
        self.assertEqual(4, twos([1, 1, 2, 2, 4]))
        self.assertEqual(6, twos([2, 1, 2, 2, 4]))

if __name__ == '__main__':
    unittest.main()
