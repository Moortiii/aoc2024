from lib.src.parsing import read_lines


def check_all_within_threshold(numbers: list[int]):
    prev = numbers[0]
    results = []

    for number in numbers[1:]:
        results.append(
            number in [prev - 1, prev - 2, prev - 3, prev + 1, prev + 2, prev + 3]
        )
        prev = number

    return all(results)


def check_all_decreasing(numbers: list[int]):
    prev = numbers[0]
    results = []

    for number in numbers[1:]:
        results.append(number < prev)
        prev = number

    return all(results)


def check_all_increasing(numbers: list[int]):
    prev = numbers[0]
    results = []

    for number in numbers[1:]:
        results.append(number > prev)
        prev = number

    return all(results)


def check_safe(numbers: list[int]):
    return all(
        [
            check_all_within_threshold(numbers),
            any([check_all_decreasing(numbers), check_all_increasing(numbers)]),
        ]
    )


def solve(input_file: str):
    lines = read_lines(input_file)

    safe = 0

    for line in lines:
        numbers = [int(num) for num in line.split(" ")]

        is_safe = check_safe(numbers)

        if not is_safe:
            for i, _ in enumerate(numbers):
                numbers_copy = numbers[::]
                numbers_copy.pop(i)
                is_safe = check_safe(numbers_copy)

                if is_safe:
                    safe += 1
                    break
        else:
            safe += 1

    return safe
