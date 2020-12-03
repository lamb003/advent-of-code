from day2 import part1, part2, Password
import unittest


class TestDay2(unittest.TestCase):
    data = [
        Password(policy_min=1, policy_max=3, policy_value="a", password="abcde"),
        Password(policy_min=1, policy_max=3, policy_value="b", password="cdefg"),
        Password(policy_min=2, policy_max=9, policy_value="c", password="ccccccccc"),
    ]

    def test_part1(self):
        expected = 2
        self.assertEqual(part1(self.data), expected)

    def test_part2(self):
        expected = 1
        self.assertEqual(part2(self.data), expected)

    def test_part2_additional_data(self):
        test_data = [
            Password(policy_min=1, policy_max=3, policy_value="a", password="abcde"),
            Password(policy_min=1, policy_max=3, policy_value="a", password="abade"),
            Password(policy_min=1, policy_max=2, policy_value="a", password="abade"),
            Password(policy_min=1, policy_max=2, policy_value="a", password="bade"),
            Password(policy_min=1, policy_max=2, policy_value="a", password="aaaaa"),
            Password(
                policy_min=1,
                policy_max=20,
                policy_value="a",
                password="xxxxxxxxxxxxxxxxxxxa",
            ),
        ]
        expected = 4
        self.assertEqual(part2(test_data), expected)


if __name__ == "__main__":
    unittest.main()
