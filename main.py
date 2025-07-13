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
from rich.console import Console
from rich.progress import Progress, BarColumn, TextColumn, TimeRemainingColumn

from Config import Config

console = Console()
_config = None


async def main() -> None:
    console.print("[bold green]Started Pomodoro[/]")
    await start_pomodoro()
    console.print("[bold green]Pomodoro Ended![/]")


async def start_pomodoro():
    config = fetch_config()
    count = 0
    while True:
        await countdown(config.pomodoro_duration, "Pomodoro")
        count += 1
        console.print(f"[bold green]Pomodoro's Done : {count}[/]")
        await start_break(config.break_duration, count)
        try:
            config.pomodoro_duration = await fetch_user_input(
                config.pomodoro_duration, "Pomodoro"
            )
            config.break_duration = await fetch_user_input(
                config.break_duration, "Break"
            )
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
    config = fetch_config()
    if is_long_break(count):
        console.print("[bold green]Taking Long Break![/]")
        await countdown(
            config.long_break_duration,
            "Break",
        )
    else:
        await countdown(
            break_duration,
            "Break",
        )


async def countdown(minutes: int, name: str) -> None:
    config = fetch_config()
    seconds = minutes * config.second_multiplier
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


def parse_arguments() -> Config:
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
        return Config(
            pomodoro_duration=args.pomodoro_duration,
            break_duration=args.break_duration,
            second_multiplier=3,
            long_break_duration=3,
        )
    return Config(
        pomodoro_duration=args.pomodoro_duration,
        break_duration=args.break_duration,
    )


def ask(prompt: str, default: int) -> int:
    raw = input(f"\r{prompt}") or str(default)
    sys.stdout.write("\033[F\033[K")
    sys.stdout.flush()
    return int(raw)


def is_long_break(count):
    config = fetch_config()
    return count > 0 and count % config.long_break_pomodoro_count == 0


def fetch_config() -> Config:
    global _config
    if _config is None:
        _config = parse_arguments()
    return _config


if __name__ == "__main__":
    asyncio.run(main())
