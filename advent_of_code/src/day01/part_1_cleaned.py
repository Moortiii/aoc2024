import re

from .lib.parsing import read_lines


def solve(input_file: str):
    lines = read_lines(input_file)
    left, right = [], []

    for line in lines:
        a, b = re.sub(string=line, pattern=r"\s+", repl=" ").split()
        left.append(int(a))
        right.append(int(b))

    return sum([abs(a - b) for a, b in zip(sorted(left), sorted(right))])
