import argparse
import time

def main():
    pomodoro_duration, break_duration = parse_arguments()
    countdown(pomodoro_duration)
    countdown(break_duration)

def countdown(seconds):
    for remaining in range(seconds, 0, -1):
        print(f"\rTime remaining: {remaining:2d} seconds", end="")
        time.sleep(1)
    print("End of time")

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
    main()
