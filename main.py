import argparse
import asyncio
from rich.console import Console
from rich.progress import Progress, BarColumn, TextColumn, TimeRemainingColumn

console = Console()


async def main():
    pomodoro_duration, break_duration = parse_arguments()
    await countdown(pomodoro_duration, "Pomodoro")
    await countdown(break_duration, "Break")
    console.print("[bold green]All done![/]")


async def countdown(seconds, name):
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


def parse_arguments():
    parser = argparse.ArgumentParser(description="Pomodoro Timer")
    parser.add_argument(
        "-p",
        "--pomodoro_duration",
        type=lambda m: int(m) * 60,
        default=25 * 60,
        help="Duration",
    )
    parser.add_argument(
        "-b",
        "--break_duration",
        type=lambda m: int(m) * 60,
        default=5 * 60,
        help="Break",
    )
    args = parser.parse_args()
    return args.pomodoro_duration, args.break_duration


if __name__ == "__main__":
    asyncio.run(main())
