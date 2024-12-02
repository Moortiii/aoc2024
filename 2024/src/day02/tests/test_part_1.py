import os
import pathlib
import pytest
from lib.src.parsing import read_lines
from ..part_1 import solve

dir_path = pathlib.Path(os.path.dirname(os.path.realpath(__file__))).parent / "input"


def test_solve_part_1():
    examples = [
        ("example_1.txt", 2),
        ("example_2.txt", None),
        ("example_3.txt", None),
    ]

    # Verify that examples succeed before running on actual input
    for example in examples:
        filename, expected_example_output = example
        input_file = dir_path / "part_1" / filename

        lines = read_lines(input_file=input_file)
        if not lines:
            continue

        initial_solution__example_output = solve(input_file=input_file)

        # Don't print output unecessarily before solver has been written
        if initial_solution__example_output == "NotImplemented":
            pytest.skip(reason="Solver not implemented")

        # If we have a cleaned up version, ensure that the output matches our initial
        # solution for all of the examples
        if pathlib.Path(dir_path.parent / "part_1_cleaned.py").exists():
            from ..part_1_cleaned import solve as solve_clean
            
            cleaned_solution__example_output = solve_clean(input_file=input_file)
            assert (
                cleaned_solution__example_output == initial_solution__example_output
            ), "Output from cleaned up solution does not match initial solution"

        assert initial_solution__example_output == expected_example_output

    initial_solution_output = solve(dir_path / "part_1" / "input.txt")
    print("\nPart 1 solution:", initial_solution_output)

    # If we have a cleaned up version, ensure that the output matches our initial
    # solution for the full puzzle input
    if pathlib.Path(dir_path.parent / "part_1_cleaned.py").exists():
        from ..part_1_cleaned import solve as solve_clean

        cleaned_solution_output = solve_clean(dir_path / "part_1" / "input.txt")
        assert (
            cleaned_solution_output == initial_solution_output
        ), "Output from cleaned up solution does not match initial solution"
    
