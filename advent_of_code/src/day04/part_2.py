from .lib.parsing import read_lines


def is_valid_mas(row_idx: int, col_idx: int, matrix: list[list[str]]):
    if matrix[col_idx][row_idx] != "A":
        return 0

    if (
        row_idx >= 1
        and col_idx >= 1
        and row_idx < len(matrix[0]) - 1
        and col_idx < len(matrix) - 1
    ):
        valid_left = any(
            [
                (
                    matrix[col_idx + 1][row_idx + 1] == "S"
                    and matrix[col_idx - 1][row_idx - 1] == "M"
                ),
                (
                    matrix[col_idx + 1][row_idx + 1] == "M"
                    and matrix[col_idx - 1][row_idx - 1] == "S"
                ),
            ]
        )

        valid_right = any(
            [
                (
                    matrix[col_idx + 1][row_idx - 1] == "S"
                    and matrix[col_idx - 1][row_idx + 1] == "M"
                ),
                (
                    matrix[col_idx + 1][row_idx - 1] == "M"
                    and matrix[col_idx - 1][row_idx + 1] == "S"
                ),
            ],
        )

        if valid_left and valid_right:
            return 1

    return 0


def solve(input_file: str):
    lines = read_lines(input_file)

    matrix = list(map(list, lines))

    count = 0
    for row_idx in range(len(matrix[0])):
        for col_idx in range(len(matrix)):
            count += is_valid_mas(row_idx=row_idx, col_idx=col_idx, matrix=matrix)

    return count
