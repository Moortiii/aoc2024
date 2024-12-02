# Advent of code

Repository for Advent of Code solutions for 2024, including necessary setup scripts. Most importantly from 2023 we've switched from `Poetry` to `uv`.

## Included features

- [x] Run tests automatically
- [x] Get output from scripts
- [x] Get output from tests
- [x] Start VSCode automatically
- [x] Support multiple task examples
- [x] Fetch puzzle output automatically
- [x] Shared dependencies across all tasks
- [x] Countdown until task is ready for fetching
- [x] Check if examples have content before running them
- [x] Only run on puzzle input if examples are succeeding
- [x] Script the creation of template for a given year and day
- [ ] Submit flag on request
- [ ] Get feedback from flag submission
- [ ] Encrypt puzzle input using SOPS, or fetch from private repository, to prevent storing them in git, ref: https://adventofcode.com/2024/about "Can I copy/redistribute parts of Advent of Code?"
- [ ] Send the input through an LLM and ask it to fetch the examples (example_1.txt), and the expected output, e.g. `4` automatically
