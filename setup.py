import argparse
from datetime import datetime
import asyncio
import httpx

from config import Settings

settings = Settings()

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

    selected_date = f"day{str(args.day).zfill(2)}"

    async with httpx.AsyncClient() as client:
        client.cookies.set("session", settings.aoc_session_cookie)
        puzzle_input = (await client.get(
            f"https://adventofcode.com/{args.year}/day/{args.day}/input",
        )).text[:-1]

        # print(puzzle_input)

if __name__ == "__main__":
    asyncio.run(setup())
