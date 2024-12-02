# Advent of code 2024

Repository for Advent of Code solutions for 2024, including necessary setup scripts.

```
   Advent of Code 2024!
           ___
         _[___]_  _
          ( " )  [_]
      '--(`~:~`)--|'
        / `-:-' \ |
   __.--\   :   /--.
 .'`     '-----'    '-...
/________________________\
```

(ASCII Art inspired by examples at: https://ascii.co.uk/art/snowman)

### Example: How to run

```bash
uv run setup/setup.py --day 3
```

This will print the following:

```
Waiting for puzzle to be released @ 03.Dec 06:00:00 ... 02.Dec 10:38:25
```

Which halts execution until the puzzle has been released, at which point it will start VSCode with the correct windows and pre-populate the input files with the puzzle input.

There are also the following options available, i.e. for testing:

```bash
uv run setup/setup.py --help
usage: Advent of Code Generator [-h] [-d DAY] [-y YEAR] [-c] [-b]

Generate template for solving Advent of Code problems

options:
  -h, --help       show this help message and exit
  -d, --day DAY    The day to generate a template for. Default: current date
  -y, --year YEAR  The year to generate a template for. Default: current year
  -c, --no-code    Run without starting VSCode. Default: false
  -b, --no-block   Run without waiting for execution. Default: false

Happy solving!
```

## Roadmap

This is a work in progress:

- [x] Run tests automatically
- [x] Get user output from solvers
- [x] Get user routput from tests
- [x] Start VSCode automatically with windows in correct order
- [x] Support multiple task examples
- [x] Fetch puzzle output automatically
- [x] Shared dependencies across all tasks
- [x] Countdown until task is ready for fetching
- [x] Check if examples have content before running them
- [x] Only run solver(s) on puzzle input if all examples are succeeding
- [x] Script the creation of a template for a given year and day
- [ ] Submit flag via API on-demand and "start" task 2
- [ ] Get feedback from flag submission, e.g. "Your input is too high"
- [ ] Save feedback from flag submissions, e.g. "Your input was: `...`, Feedback from API: `...` to a logfile.
- [ ] Encrypt puzzle input using SOPS, or fetch from private repository, to prevent storing them in git, ref: https://adventofcode.com/2024/about "Can I copy/redistribute parts of Advent of Code?"
- [ ] Send the input through an LLM and ask it to fetch the examples (example_1.txt), and the expected output, e.g. `4` automatically

### Previous repositories

In order to preserve history of how the template evolves over time, I create a new repository every year. Previous repositories can be found here:

- 2020: https://github.com/Moortiii/aoc-2020/
- 2022: https://github.com/Moortiii/aoc-2022/
- 2023: https://github.com/Moortiii/aoc2023
