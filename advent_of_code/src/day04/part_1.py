from .lib.parsing import read_lines


def get_xmas_count(row_idx: int, col_idx: int, matrix: list[list[str]]):
    count = 0

    if col_idx - 3 >= 0:
        output = "".join(
            [
                matrix[col_idx - 3][row_idx],
                matrix[col_idx - 2][row_idx],
                matrix[col_idx - 1][row_idx],
                matrix[col_idx][row_idx],
            ]
        )

        if output == "XMAS":
            count += 1

        output = "".join(
            [
                matrix[col_idx - 3][row_idx],
                matrix[col_idx - 2][row_idx],
                matrix[col_idx - 1][row_idx],
                matrix[col_idx][row_idx],
            ]
        )[::-1]

        if output == "XMAS":
            count += 1

    if row_idx - 3 >= 0:
        output = "".join(
            [
                matrix[col_idx][row_idx - 3],
                matrix[col_idx][row_idx - 2],
                matrix[col_idx][row_idx - 1],
                matrix[col_idx][row_idx],
            ]
        )

        if output == "XMAS":
            count += 1

        output = "".join(
            [
                matrix[col_idx][row_idx - 3],
                matrix[col_idx][row_idx - 2],
                matrix[col_idx][row_idx - 1],
                matrix[col_idx][row_idx],
            ]
        )[::-1]

        if output == "XMAS":
            count += 1

    if row_idx - 3 >= 0 and col_idx - 3 >= 0:
        output = "".join(
            [
                matrix[col_idx - 3][row_idx - 3],
                matrix[col_idx - 2][row_idx - 2],
                matrix[col_idx - 1][row_idx - 1],
                matrix[col_idx][row_idx],
            ]
        )

        if output == "XMAS":
            count += 1

        output = "".join(
            [
                matrix[col_idx - 3][row_idx - 3],
                matrix[col_idx - 2][row_idx - 2],
                matrix[col_idx - 1][row_idx - 1],
                matrix[col_idx][row_idx],
            ]
        )[::-1]

        if output == "XMAS":
            count += 1

    if row_idx - 3 >= 0 and col_idx + 3 < len(matrix):
        output = "".join(
            [
                matrix[col_idx + 3][row_idx - 3],
                matrix[col_idx + 2][row_idx - 2],
                matrix[col_idx + 1][row_idx - 1],
                matrix[col_idx][row_idx],
            ]
        )

        if output == "XMAS":
            count += 1

        output = "".join(
            [
                matrix[col_idx + 3][row_idx - 3],
                matrix[col_idx + 2][row_idx - 2],
                matrix[col_idx + 1][row_idx - 1],
                matrix[col_idx][row_idx],
            ]
        )[::-1]

        if output == "XMAS":
            count += 1

    return count


def solve(input_file: str):
    lines = read_lines(input_file)
    matrix = list(map(list, lines))

    counts = []

    for row_idx in range(len(matrix[0])):
        for col_idx in range(len(matrix)):
            counts.append(
                get_xmas_count(row_idx=row_idx, col_idx=col_idx, matrix=matrix)
            )

    return sum(counts)
