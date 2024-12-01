import re
from collections import defaultdict
from lib.src.parsing import read_lines


def solve(input_file: str):
    lines = read_lines(input_file)

    left_nums = []
    right_nums = defaultdict(int)

    for line in lines:
        left, right = re.sub(string=line, pattern=r"\s+", repl=" ").split()
        left_nums.append(int(left))
        right_nums[int(right)] += 1

    similarity = []

    for number in left_nums:
        similarity.append(number * right_nums[number])

    return sum(similarity)