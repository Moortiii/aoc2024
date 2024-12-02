import re
from collections import Counter

from .lib.parsing import read_lines


def solve(input_file: str):
    lines = read_lines(input_file)
    left, right = [], []

    for line in lines:
        a, b = re.sub(string=line, pattern=r"\s+", repl=" ").split()
        left.append(int(a))
        right.append(int(b))

    counter = Counter(right)
    return sum([num * counter[num] for num in left])
