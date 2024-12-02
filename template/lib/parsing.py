def read_lines(input_file: str, strip=True):
    with open(input_file) as f:
        if strip:
            return [line.strip() for line in f.readlines()]
        else:
            return [line for line in f.readlines()]


def read_numbers(input_file: str):
    with open(input_file) as f:
        return [int(num) for num in f.read().split(",")]
