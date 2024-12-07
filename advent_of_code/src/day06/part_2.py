from .lib.parsing import read_lines
from copy import deepcopy


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
    original_matrix = list(map(list, lines))
    position = None
    starting_position = None

    for _y, row in enumerate(original_matrix):
        for _x, col in enumerate(row):
            if col == "^":
                position = (_x, _y)
                starting_position = (_x, _y)

    original_x, original_y = starting_position
    obstacle_loop_count = 0

    for matrix_y, row in enumerate(original_matrix):
        for matrix_x, col in enumerate(row):
            # Can't place an obstacle on the starting position
            if original_x == matrix_x and original_y == matrix_y:
                continue

            current_dir = "UP"
            escaped = False
            position = starting_position
            x, y = position

            matrix = deepcopy(original_matrix)
            matrix[matrix_y][matrix_x] = "#"

            max_iterations = 50_000
            iterations = 0

            while iterations < max_iterations:
                iterations += 1
                x, y = position

                if x < 0:
                    escaped = True
                    break

                if y < 0:
                    escaped = True
                    break

                try:
                    current_tile = matrix[y][x]
                except IndexError:
                    escaped = True
                    break

                movement = get_movement(current_dir)

                if current_tile == "#":
                    position = (x - movement[0], y - movement[1])
                    current_dir = get_next_direction(current_dir)
                else:
                    matrix[y][x] = "X"
                    position = (x + movement[0], y + movement[1])

            if not escaped:
                obstacle_loop_count += 1

    return obstacle_loop_count
