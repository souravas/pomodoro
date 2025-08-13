# Pomodoro Timer 

A beautiful command-line Pomodoro timer built with Python and Rich library. This timer helps you implement the Pomodoro Technique for improved productivity and focus.

## Features

- 🍅 Classic Pomodoro timing (25 minutes work + 5 minutes break)
- 🎨 Beautiful terminal interface with progress bars
- ⏱️ Real-time countdown with time remaining display
- 🔧 Customizable work and break durations
- 📊 Visual progress tracking
- 🎯 Clean, distraction-free interface

## Requirements

- Python 3.13+
- Rich library (for beautiful terminal output)

## Installation

1. Clone this repository:
```bash
git clone <repository-url>
cd pomodoro
```

2. Install dependencies using uv (recommended):
```bash
uv sync
```

Or using pip:
```bash
pip install rich>=14.0.0
```

## Usage

### Basic Usage

Run the timer with default settings (25 minutes work, 5 minutes break):
```bash
python main.py
```

Or with uv:
```bash
uv run python main.py
```

### Custom Durations

Specify custom work and break durations (in minutes):
```bash
python main.py -p 30 -b 10
```

This sets 30 minutes for work and 10 minutes for break.

### Command Line Options

- `-p, --pomodoro_duration`: Set work duration in minutes (default: 25)
- `-b, --break_duration`: Set break duration in minutes (default: 5)
- `-h, --help`: Show help message

### Examples

```bash
# Standard Pomodoro (25 min work, 5 min break)
python main.py

# Extended focus session (45 min work, 15 min break)
python main.py -p 45 -b 15

# Short bursts (15 min work, 3 min break)
python main.py -p 15 -b 3
```

## How It Works

1. **Work Phase**: The timer starts with your specified work duration
2. **Progress Display**: Shows a beautiful progress bar with:
   - Current phase name (Pomodoro/Break)
   - Visual progress bar
   - Percentage completion
   - Time remaining
3. **Break Phase**: Automatically transitions to break time after work completes
4. **Completion**: Displays a success message when both phases are done

## Development

This project uses:
- **uv** for dependency management
- **Rich** for terminal UI components
- **asyncio** for smooth countdown updates
- **argparse** for command-line interface

### Project Structure

```
pomodoro/
├── main.py           # Main application code
├── pyproject.toml    # Project configuration and dependencies
├── uv.lock          # Locked dependency versions
├── README.md        # This file
└── .python-version  # Python version specification
```

### Code Formatting

Format code using Black:
```bash
uv run black main.py
```

## The Pomodoro Technique

The Pomodoro Technique is a time management method developed by Francesco Cirillo:

1. **Choose a task** you want to work on
2. **Set the timer** for 25 minutes (one "Pomodoro")
3. **Work on the task** until the timer rings
4. **Take a short break** (5 minutes)
5. **Repeat** the process

After 4 Pomodoros, take a longer break (15-30 minutes).

## License

This project is open source. Feel free to use, modify, and distribute as needed.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Acknowledgments

- Built with [Rich](https://github.com/Textualize/rich) for beautiful terminal output
- Inspired by the Pomodoro Technique by Francesco Cirillo
