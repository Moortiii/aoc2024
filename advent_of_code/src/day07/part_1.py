import re
from .lib.parsing import read_lines


def generate_expression(
    numbers: list[int],
    expression: str,
    expressions: list[str],
    operator: str | None = None,
):
    if not numbers:
        return expression

    number = numbers[0]

    if len(numbers) >= 1 and operator is not None:
        expression = f"{expression} {operator} {number}"
    else:
        expression = f"{expression} {number}"

    for operator in ["*", "+"]:
        retval = generate_expression(
            numbers[1:],
            expression=expression,
            expressions=expressions,
            operator=operator,
        )

        if retval is not None:
            expressions.append(retval.strip())


def calculate(expr: list[str], current_sum: int):
    if len(expr) == 0:
        return current_sum

    operator, number, *_ = expr
    current_sum = eval(f"{current_sum} {operator} {number}")
    return calculate(expr=expr[::][2:], current_sum=current_sum)


def solve(input_file: str):
    lines = read_lines(input_file)
    sums = []

    for line in lines:
        expected_output, numbers = line.split(": ")
        numbers = re.findall(r"(\d+)", numbers)
        numbers = list(map(int, numbers))

        expressions = []
        generate_expression(numbers, expression="", expressions=expressions)
        expressions = list(set(expressions))
        expressions = [expr.split(" ") for expr in expressions]

        for expression in expressions:
            _sum = calculate(expr=expression[1:], current_sum=expression[0])

            if _sum == int(expected_output):
                sums.append(int(expected_output))
                break

    return sum(sums)
