import shutil
import random

COLUMNS, LINES = shutil.get_terminal_size()

WALL_COLOR: str = random.choice(["\033[38;5;104m",
                                 "\033[38;5;110m",
                                 "\033[38;5;74m"])

OPPOSITES: dict[str, str] = {"n": "s",
                             "s": "n",
                             "e": "w",
                             "w": "e"}

PATTERN: list[list[int]] = [[0, 0, 1, 0, 0, 1, 1, 0],
                            [0, 1, 1, 0, 1, 0, 0, 1],
                            [1, 0, 1, 0, 0, 0, 1, 0],
                            [1, 1, 1, 1, 0, 1, 0, 0],
                            [0, 0, 1, 0, 1, 1, 1, 1]]

WIDTH, HEIGHT = 0, 0

MIN_WIDTH: int = len(PATTERN[0]) + 2
MIN_HEIGHT: int = len(PATTERN) + 2

START_POINT: int = 0

MAZE_START_ROW: int = 0
ANIM_SPEED: float = 0.02
