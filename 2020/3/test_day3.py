import unittest

from day3 import part1, part2


class TestDay3(unittest.TestCase):
    data = [
        "..##.......",
        "#...#...#..",
        ".#....#..#.",
        "..#.#...#.#",
        ".#...##..#.",
        "..#.##.....",
        ".#.#.#....#",
        ".#........#",
        "#.##...#...",
        "#...##....#",
        ".#..#...#.#",
    ]

    def test_part1(self):
        expected = 7
        self.assertEqual(part1(self.data), expected)

    def test_part2(self):
        expected = 336
        self.assertEqual(part2(self.data), expected)
