"""
Pomodoro Timer

A command-line Pomodoro timer application built with Python and Rich library.
Implements the Pomodoro Technique for improved productivity and focus.

Author: Sourav
Date: July 2025
"""

import argparse
import asyncio
from typing import Tuple
from rich.console import Console
from rich.progress import Progress, BarColumn, TextColumn, TimeRemainingColumn

console = Console()


async def main() -> None:
    pomodoro_duration, break_duration = parse_arguments()
    await countdown(pomodoro_duration, "Pomodoro")
    await countdown(break_duration, "Break")
    console.print("[bold green]All done![/]")


async def countdown(seconds: int, name: str) -> None:
    with Progress(
        TextColumn("[bold blue]{task.fields[name]}", justify="right"),
        BarColumn(),
        "[progress.percentage]{task.percentage:>3.0f}%",
        TimeRemainingColumn(),
        console=console,
        transient=True,
    ) as progress:
        task = progress.add_task("", name=name, total=seconds)
        for _ in range(seconds):
            await asyncio.sleep(1)
            progress.update(task, advance=1)


def parse_arguments() -> Tuple[int, int]:
    parser = argparse.ArgumentParser(
        description="Pomodoro Timer - A beautiful command-line productivity tool",
        epilog="Example: python main.py -p 25 -b 5 (25 min work, 5 min break)",
    )
    parser.add_argument(
        "-p",
        "--pomodoro_duration",
        type=lambda m: int(m) * 60,
        default=25 * 60,
        metavar="MINUTES",
        help="Duration of work session in minutes (default: 25)",
    )
    parser.add_argument(
        "-b",
        "--break_duration",
        type=lambda m: int(m) * 60,
        default=5 * 60,
        metavar="MINUTES",
        help="Duration of break session in minutes (default: 5)",
    )
    args = parser.parse_args()
    return args.pomodoro_duration, args.break_duration


if __name__ == "__main__":
    asyncio.run(main())
