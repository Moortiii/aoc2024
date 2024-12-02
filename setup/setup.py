import argparse
import asyncio
import pathlib
import subprocess
import sys
import time
from datetime import datetime
from zoneinfo import ZoneInfo

import httpx
from config import Settings
from loguru import logger
from rich import print

settings = Settings()


def block_execution(day: int, year=2024, hours=6, minutes=0, seconds=0):
    """Block execution until the time has passed a target time

    Target: {year}-12-{day}T06:00:00 Europe/Oslo
    """

    def puzzle_released(current: datetime, target: datetime) -> bool:
        return current >= target

    target_time = datetime(
        year, 12, day, hours, minutes, seconds, tzinfo=ZoneInfo("Europe/Oslo")
    )
    _now = datetime.now(tz=ZoneInfo("Europe/Oslo"))

    # NOTE: The early check here is to avoid the "waiting" message and the empty
    #       cleanup-printif the puzzle has already been released.
    if puzzle_released(_now, target_time):
        return

    msg_template = (
        f"  Waiting for puzzle to be released @ "
        f"{target_time.strftime('%d.%b %H:%M:%S')} ... "
    )
    while not puzzle_released(_now, target_time):
        print(
            f"[bold][grey74]{msg_template}[/grey74][grey46]"
            f"{_now.strftime('%d.%b %H:%M:%S')}[/grey46][/bold]",
            end="\r",
        )
        time.sleep(0.5)
        _now = datetime.now(tz=ZoneInfo("Europe/Oslo"))

    print()


def start_vscode(project_path: pathlib.Path):
    """Starts VSCode in the project path and open relevant files

    Args:
        project_path (str): The path to the project to open
    """
    try:
        subprocess.run(
            (
                f"code --reuse-window "
                f"{project_path} "
                f"{project_path}/input/part_1/example_1.txt "
                f"{project_path}/input/part_2/example_1.txt "
                f"{project_path}/tests/test_part_1.py "
                f"{project_path}/part_1.py "
                f"{project_path}/part_2.py "
                f"{project_path}/tests/test_part_2.py "
            ),
            shell=True,
        )
    except Exception as err:
        logger.error(f"Failed to start VSCode: {err}")
        sys.exit(1)


async def setup():
    parser = argparse.ArgumentParser(
        prog="Advent of Code Generator",
        description="Generate template for solving Advent of Code problems",
        epilog="Happy solving!",
    )

    parser.add_argument(
        "-d",
        "--day",
        default=datetime.today().day,
        type=int,
        help="The day to generate a template for. Default: current date",
    )

    parser.add_argument(
        "-y",
        "--year",
        default=datetime.today().year,
        type=int,
        help="The year to generate a template for. Default: current year",
    )

    parser.add_argument(
        "-c",
        "--no-code",
        default=False,
        help="Run without starting VSCode. Default: false",
        action="store_true",
    )

    args = parser.parse_args()

    try:
        # Wait until 06:00:00 Europe/Oslo time
        block_execution(year=int(args.year), day=int(args.day), hours=6, minutes=0)
    except KeyboardInterrupt:
        logger.info("Exiting... ")
        sys.exit(0)

    date = f"{str(args.day).zfill(2)}"
    directory = f"{str(args.year)}/src/day{date}"

    if pathlib.Path(directory).is_dir():
        logger.warning(f"Project already exists at {directory}, not overwriting...")
    else:
        subprocess.run(f"cp -r ./template {directory}", shell=True)

        async with httpx.AsyncClient() as client:
            client.cookies.set("session", settings.aoc_session_cookie)
            puzzle_input = (
                await client.get(
                    f"https://adventofcode.com/{args.year}/day/{args.day}/input",
                )
            ).text[:-1]

        with open(f"{directory}/input/part_1/input.txt", "w") as f:
            f.write(puzzle_input)

        with open(f"{directory}/input/part_2/input.txt", "w") as f:
            f.write(puzzle_input)

    if not args.no_code:
        start_vscode(pathlib.Path(directory))

    subprocess.run(f"./run.sh {args.year} {date}", shell=True)


if __name__ == "__main__":
    asyncio.run(setup())
