import re

from .lib.parsing import read_lines


def solve(input_file: str):
    lines = read_lines(input_file)

    left_nums = []
    right_nums = []

    for line in lines:
        left, right = re.sub(string=line, pattern=r"\s+", repl=" ").split()
        left_nums.append(int(left))
        right_nums.append(int(right))

    left_nums = sorted(left_nums)
    right_nums = sorted(right_nums)

    dsts = []

    for a, b in zip(left_nums, right_nums):
        dsts.append(abs(a - b))

    return sum(dsts)
