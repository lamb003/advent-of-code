from collections import namedtuple
from operator import xor


Password = namedtuple(
    "Password", ["policy_min", "policy_max", "policy_value", "password"]
)


def part1(passwords: list) -> int:
    number_valid_passwords = 0
    for password in passwords:
        policy_value_occurances = password.password.count(password.policy_value)
        if password.policy_max >= policy_value_occurances >= password.policy_min:
            number_valid_passwords += 1
    return number_valid_passwords


def part2(passwords: list) -> int:
    number_valid_passwords = 0
    for password in passwords:
        position1 = password.password[password.policy_min - 1] == password.policy_value
        position2 = password.password[password.policy_max - 1] == password.policy_value
        if xor(position1, position2):
            number_valid_passwords += 1
    return number_valid_passwords


if __name__ == "__main__":
    with open("input.txt") as _file:
        passwords = []
        for line in _file:
            _policy, _password = line.split(":")
            _policy_numbers, _policy_value = _policy.split(" ")
            _policy_lower, policy_upper = _policy_numbers.split("-")
            passwords.append(
                Password(
                    policy_min=int(_policy_lower),
                    policy_max=int(policy_upper),
                    policy_value=_policy_value,
                    password=_password.strip(),
                )
            )
        print("part 1: ", part1(passwords))
        print("part 2: ", part2(passwords))
