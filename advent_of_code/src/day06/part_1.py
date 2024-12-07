from pprint import pprint
from .lib.parsing import read_lines


def get_next_direction(current_dir: str):
    match current_dir:
        case "UP":
            return "RIGHT"
        case "RIGHT":
            return "DOWN"
        case "DOWN":
            return "LEFT"
        case "LEFT":
            return "UP"


def get_movement(current_dir: str):
    match current_dir:
        case "UP":
            return (0, -1)
        case "DOWN":
            return (0, 1)
        case "LEFT":
            return (-1, 0)
        case "RIGHT":
            return (1, 0)


def print_matrix(matrix):
    print("\n".join(["".join(row) for row in matrix]), "\n")


def solve(input_file: str):
    lines = read_lines(input_file)
    matrix = list(map(list, lines))

    print()

    position = None

    for y, row in enumerate(matrix):
        for x, col in enumerate(row):
            if col == "^":
                position = (x, y)

    max_iterations = 500000
    iterations = 0

    current_dir = "UP"

    x, y = position
    matrix[y][x] = "X"

    while iterations < max_iterations:
        iterations += 1
        x, y = position

        if x < 0:
            break

        if y < 0:
            break

        try:
            current_tile = matrix[y][x]
        except IndexError:
            break

        movement = get_movement(current_dir)

        if current_tile == "#":
            position = (x - movement[0], y - movement[1])
            current_dir = get_next_direction(current_dir)
        else:
            matrix[y][x] = "X"
            position = (x + movement[0], y + movement[1])

    count = 0

    for y, row in enumerate(matrix):
        for x, col in enumerate(row):
            if col == "X":
                count += 1

    return count
