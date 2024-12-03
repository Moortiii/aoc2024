import re
from .lib.parsing import read_lines


def solve(input_file: str):
    lines = read_lines(input_file)

    values = []

    mul_enabled = True

    for line in lines:
        instructions = re.findall("(do)\(\)|(don't)\(\)|mul\((\d+),(\d+)\)+", line)

        for instruction in instructions:
            do, dont, a, b = instruction

            if do:
                mul_enabled = True

            if dont:
                mul_enabled = False

            if mul_enabled and a and b:
                values.append(int(a) * int(b))

    return sum(values)
