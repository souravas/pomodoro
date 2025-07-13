from dataclasses import dataclass, field


@dataclass
class Config:
    pomodoro_duration: int
    break_duration: int
    long_break_duration: int = field(default=15)
    second_multiplier: int = field(default=60)
    long_break_pomodoro_count: int = field(init=False, default=4)
