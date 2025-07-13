"""
Pomodoro Timer

A command-line Pomodoro timer application built with Python and Rich library.
Implements the Pomodoro Technique for improved productivity and focus.

Author: Sourav
Date: July 2025
"""

import argparse
import asyncio
import sys
from typing import Tuple
from rich.console import Console
from rich.progress import Progress, BarColumn, TextColumn, TimeRemainingColumn

console = Console()

SECOND_MULTIPLIER = 60
LONG_BREAK_DURATION = 15
LONG_BREAK_POMODORO_COUNT = 4


async def main() -> None:
    console.print("[bold green]Started Pomodoro[/]")
    await start_pomodoro(*parse_arguments())
    console.print("[bold green]Pomodoro Ended![/]")


async def start_pomodoro(pomodoro_duration, break_duration):
    count = 0
    while True:
        await countdown(pomodoro_duration, "Pomodoro")
        count += 1
        console.print(f"[bold green]Pomodoro's Done : {count}[/]")
        await start_break(break_duration, count)
        try:
            pomodoro_duration = await fetch_user_input(pomodoro_duration, "Pomodoro")
            break_duration = await fetch_user_input(break_duration, "Break")
        except ValueError:
            console.print("[red]Quitting Pomodoro...[/]")
            break


async def fetch_user_input(duration: int, name: str) -> int:
    duration = ask(
        f"Enter next {name} duration (blank to keep current, q to quit): ",
        duration,
    )
    return duration


async def start_break(break_duration, count):
    if is_long_break(count):
        console.print("[bold green]Taking Long Break![/]")
        await countdown(
            LONG_BREAK_DURATION,
            "Break",
        )
    else:
        await countdown(
            break_duration,
            "Break",
        )


async def countdown(minutes: int, name: str) -> None:
    seconds = minutes * SECOND_MULTIPLIER
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
        type=lambda m: int(m),
        default=25,
        metavar="MINUTES",
        help="Duration of work session in minutes (default: 25)",
    )
    parser.add_argument(
        "-b",
        "--break_duration",
        type=lambda m: int(m),
        default=5,
        metavar="MINUTES",
        help="Duration of break session in minutes (default: 5)",
    )
    parser.add_argument(
        "-t",
        "--test",
        action="store_true",
        help="Enable test mode (use short 1-minute sessions)",
    )
    args = parser.parse_args()
    if args.test:
        update_test_values()
    return args.pomodoro_duration, args.break_duration


def update_test_values():
    global SECOND_MULTIPLIER
    global LONG_BREAK_DURATION

    SECOND_MULTIPLIER = 3
    LONG_BREAK_DURATION = 3


def ask(prompt: str, default: int) -> int:
    raw = input(f"\r{prompt}") or str(default)
    sys.stdout.write("\033[F\033[K")
    sys.stdout.flush()
    return int(raw)


def is_long_break(count):
    return count > 0 and count % LONG_BREAK_POMODORO_COUNT == 0


if __name__ == "__main__":
    asyncio.run(main())
