from day1 import part1, part2
import unittest


class TestDay1(unittest.TestCase):
    data = [1721, 979, 366, 299, 675, 1456]

    def test_part1(self):
        expected = 514579
        self.assertEqual(part1(self.data, 2020), expected)

    def test_part2(self):
        expected = 241861950
        self.assertEqual(part2(self.data, 2020), expected)


if __name__ == "__main__":
    unittest.main()
