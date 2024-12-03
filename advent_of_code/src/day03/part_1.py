import re
from .lib.parsing import read_lines


def solve(input_file: str):
    lines = read_lines(input_file)

    values = []

    for line in lines:
        instructions = re.findall("mul\((\d+),(\d+)\)+", line)

        for instruction in instructions:
            a, b = instruction
            values.append(int(a) * int(b))

    return sum(values)
