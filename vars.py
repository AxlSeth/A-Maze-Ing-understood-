import shutil


WIDTH: int = 30
HEIGHT: int = 20

COLUMNS = shutil.get_terminal_size().columns

SYMBOL = "##"

OPPOSITES: dict[str, str] = {"n": "s",
                             "s": "n",
                             "e": "w",
                             "w": "e"}

PATTERN: list[list[int]] = [[0, 0, 1, 0, 0, 0, 1, 1, 0],
                            [0, 1, 1, 0, 0, 1, 0, 0, 1],
                            [1, 0, 1, 0, 0, 0, 0, 1, 0],
                            [1, 1, 1, 1, 0, 0, 1, 0, 0],
                            [0, 0, 1, 0, 0, 1, 1, 1, 1]]

MIN_WIDTH: int = len(PATTERN[0]) + 2
MIN_HEIGHT: int = len(PATTERN) + 2

START_POINT = (COLUMNS//2) - (WIDTH * 2)
