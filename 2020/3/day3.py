from dataclasses import dataclass
import math

TREE = "#"
OPEN = "."


@dataclass
class Position:
    x: int
    y: int


@dataclass
class MovementPatern:
    dy: int
    dx: int


def get_value_from_map(_map: list, location: Position) -> str:
    try:
        row = _map[location.y]
        value = row[location.x]
        return value
    except IndexError:
        _map[location.y] = _map[location.y] * 2
        return get_value_from_map(_map, location)


def count_trees_for_movement_pattern(
    _map: list, movement_pattern: MovementPatern
) -> int:
    position = Position(x=0, y=0)
    number_of_trees = 0
    while position.y < len(_map) - 1:
        position.x += movement_pattern.dx
        position.y += movement_pattern.dy
        value_at_position = get_value_from_map(_map, position)
        if value_at_position == TREE:
            number_of_trees += 1
    return number_of_trees


def part1(_map: list) -> int:
    return count_trees_for_movement_pattern(_map, MovementPatern(dx=3, dy=1))


def part2(_map: list) -> int:
    movement_patterns = [
        MovementPatern(dx=1, dy=1),
        MovementPatern(dx=3, dy=1),
        MovementPatern(dx=5, dy=1),
        MovementPatern(dx=7, dy=1),
        MovementPatern(dx=1, dy=2),
    ]
    number_of_trees = []
    for movement_pattern in movement_patterns:
        number_of_trees.append(count_trees_for_movement_pattern(_map, movement_pattern))
    return math.prod(number_of_trees)


if __name__ == "__main__":
    with open("input.txt") as _file:
        _map = [line.strip() for line in _file]
        print("part 1: ", part1(_map))
        print("part 2: ", part2(_map))
