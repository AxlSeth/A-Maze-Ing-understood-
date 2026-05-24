import shutil
import subprocess


COLUMNS = shutil.get_terminal_size().columns
ROWS = shutil.get_terminal_size().lines

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


def get_dimensions():
    while True:
        try:
            w = int(input("Enter maze's width: "))
            h = int(input("Enter maze's height: "))
            if not (1 <= h <= COLUMNS // 6 or 1 <= w <= ROWS//6):
               raise ValueError()
            return w, h
        except ValueError:
            subprocess.run(["clear"])
            print("Please input a valid number, don't be stupid.")
            continue

WIDTH, HEIGHT = get_dimensions()


MIN_WIDTH: int = len(PATTERN[0]) + 2
MIN_HEIGHT: int = len(PATTERN) + 2

START_POINT = (COLUMNS//2) - (WIDTH * 2)
