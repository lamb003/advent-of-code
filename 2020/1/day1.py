def part1(expenses: list, target: int) -> int:
    """
    Question: https://adventofcode.com/2020/day/1
    """
    expenses = set(expenses)
    for i, expense in enumerate(expenses):
        for _, other_expense in enumerate(expenses, i):
            if expense + other_expense == target:
                return expense * other_expense


def part2(expenses: list, target: int) -> int:
    expenses = set(expenses)
    for i, expense in enumerate(expenses):
        for _, other_expense in enumerate(expenses, i):
            if (target - expense - other_expense) in expenses:
                return expense * other_expense * (target - expense - other_expense)


if __name__ == "__main__":
    with open("input.txt") as _file:
        expenses = [int(line) for line in _file]
        print("part 1: ", part1(expenses, 2020))
        print("part 2: ", part2(expenses, 2020))
