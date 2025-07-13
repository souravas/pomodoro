import argparse
import sys
import asyncio
from rich.progress import track

async def main():
    pomodoro_duration, break_duration = parse_arguments()
    await countdown(pomodoro_duration, 'Pomodoro')
    await countdown(break_duration, 'Break')

async def countdown(seconds, name):
    for _ in track(range(seconds), description=f"[bold blue]{name}"):
        await asyncio.sleep(1)
    sys.stdout.write("\r\033[K")  # \r = go to start, \033[K = clear to end of line
    sys.stdout.flush()

def to_seconds(minutes):
    return minutes * 60

def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Pomodoro Timer"
    )
    parser.add_argument("pomodoro_duration", type=int, help="Duration")
    parser.add_argument("break_duration", type=int, help="Break")
    args = parser.parse_args()
    pomodoro_duration = args.pomodoro_duration
    break_duration = args.break_duration
    pomodoro_duration = to_seconds(pomodoro_duration)
    break_duration = to_seconds(break_duration)
    return pomodoro_duration, break_duration

if __name__ == "__main__":
    asyncio.run(main())
