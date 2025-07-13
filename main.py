import argparse
import asyncio
from rich.progress import track

async def main():
    pomodoro_duration, break_duration = parse_arguments()
    await countdown(pomodoro_duration, 'Pomodoro')
    await countdown(break_duration, 'Break')

async def countdown(seconds, name):
    for _ in track(range(seconds), description=f"[bold blue]{name}"):
        await asyncio.sleep(1)

def to_seconds(minutes):
    return minutes * 60

def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Pomodoro Timer"
    )
    parser.add_argument("pomodoro_duration", type=int, help="Duration")
    parser.add_argument("break_duration", type=int, help="Break")
    args = parser.parse_args()
    return to_seconds(args.pomodoro_duration), to_seconds(args.break_duration)

if __name__ == "__main__":
    asyncio.run(main())
