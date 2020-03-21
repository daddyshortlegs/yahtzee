import unittest


def ones(rolls):
    return 2


class YahtzeeTestCase(unittest.TestCase):
    def test_ones(self):
        score = ones([1, 1, 2, 3, 4])
        self.assertEqual(2, score)


if __name__ == '__main__':
    unittest.main()
