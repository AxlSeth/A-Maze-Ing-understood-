import vars
import sys
import maze_gen
import time

def print_title():
    title = """
-- This is --

      ▄████████       ▄▄▄▄███▄▄▄▄      ▄████████  ▄███████▄     ▄████████      ▄█  ███▄▄▄▄      ▄██████▄ 
     ███    ███     ▄██▀▀▀███▀▀▀██▄   ███    ███ ██▀     ▄██   ███    ███     ███  ███▀▀▀██▄   ███    ███
   ███    ███     ███   ███   ███   ███    ███       ▄███▀   ███    █▀      ███▌ ███   ███   ███    █▀
               ███    ███ \033[91m▄ ▄\033[0m ███   ███   ███   ███    ███  ▀█▀▄███▀ ▄▄ ▄███▄▄▄     \033[91m▄ ▄\033[0m ███▌ ███   ███  ▄███
                   ▀███████████ \033[91m▀█▀\033[0m ███   ███   ███ ▀███████████   ▄███▀   ▀ ▀▀███▀▀▀     \033[91m▀█▀\033[0m ███▌ ███   ███ ▀▀███ ████▄
     ███    ███     ███   ███   ███   ███    ███ ▄███▀         ███    █▄      ███  ███   ███   ███    ███
     ███    ███     ███   ███   ███   ███    ███ ███▄     ▄█   ███    ███     ███  ███   ███   ███    ███
    ███    █▀       ▀█   ███   █▀    ███    █▀   ▀████████▀   ██████████     █▀    ▀█   █▀    ████████▀

    """
    for line in title.splitlines():
        print(line.center(vars.COLUMNS - 2))
        time.sleep(0.2)
    print("\n")
    print(("(P) Play    (R) Regenerate maze    (C) Change colors    (Q) Quit").center(vars.COLUMNS), end="\n"*2)


def display_maze(maze: list[list[maze_gen.Cell]]) -> None:                     
    height: int = len(maze)
    width: int = len(maze[0])

    for y in range(height):
        for x in range(width):
            if x == 0:
                print(" " * vars.START_POINT, end="")
            print(f"{vars.WALL_COLOR}██", end="")
            if maze[y][x].walls["n"] == 1:
                print("██", end="")
            else:
                print("  ", end="")
        print("██")

        for x in range(width):
            if x == 0:
                print(" " * vars.START_POINT, end="")
            if maze[y][x].walls["w"] == 1:
                if maze[y][x].is_pattern == 1:
                    print(f"{vars.WALL_COLOR}██\033[96m██\033[0m", end="")
                else:
                    print(f"{vars.WALL_COLOR}██  ", end="")
            else:
                print("    ", end="")
        print("██")

    for x in range(width):
        if x == 0:
            print(" " * vars.START_POINT, end="")
        print("██", end="")
        if maze[height - 1][x].walls["s"] == 1:
            print("██", end="")
        else:
            print("    ", end="")
    print("██")

def display_closed_maze(width: int, height: int) -> None:
    for y in range(height):
        for x in range(width):
            if x == 0:
                print(" " * vars.START_POINT, end="")
            print(f"{vars.WALL_COLOR}████", end="")
        print("██")

        for x in range(width):
            if x == 0:
                print(" " * vars.START_POINT, end="")
            print(f"{vars.WALL_COLOR}██  ", end="")
        print("██")

    for x in range(width):
        if x == 0:
            print(" " * vars.START_POINT, end="")
        print(f"{vars.WALL_COLOR}████", end="")
    print("██")

def carve_wall(y: int, x: int, direction: str) -> None:
    # Each cell occupies 2 terminal rows and 4 terminal columns.
    # Terminal rows and columns are 1-indexed in ANSI escape codes.

    col_base: int = vars.START_POINT + (x * 4) + 1  # 1-indexed left edge of this cell

    if direction == "n":
        # The north wall slot is the RIGHT half of the top row of cell (y, x).
        # top row = MAZE_START_ROW + (y * 2), right half starts 2 cols into the cell.
        term_row: int = vars.MAZE_START_ROW + (y * 2)
        term_col: int = col_base + 2
        sys.stdout.write(f"\033[{term_row};{term_col}H  ")

    elif direction == "s":
        # South wall = north wall of the cell below (y+1, x).
        term_row = vars.MAZE_START_ROW + ((y + 1) * 2)
        term_col = col_base + 2
        sys.stdout.write(f"\033[{term_row};{term_col}H  ")

    elif direction == "w":
        # West wall is the LEFT half of the body row of cell (y, x).
        term_row = vars.MAZE_START_ROW + (y * 2) + 1
        term_col = col_base
        sys.stdout.write(f"\033[{term_row};{term_col}H  ")

    elif direction == "e":
        # East wall = west wall of the cell to the right (y, x+1).
        col_base_right: int = vars.START_POINT + ((x + 1) * 4) + 1
        term_row = vars.MAZE_START_ROW + (y * 2) + 1
        term_col = col_base_right
        sys.stdout.write(f"\033[{term_row};{term_col}H  ")

    sys.stdout.flush()
    time.sleep(vars.ANIM_SPEED)


def move_cursor_below_maze(maze: list[list[maze_gen.Cell]]) -> None:
    maze_end_row: int = vars.MAZE_START_ROW + (len(maze) * 2) + 1
    sys.stdout.write(f"\033[{maze_end_row};0H")
    sys.stdout.flush()

def hide_cursor() -> None:
    sys.stdout.write("\033[?25l")
    sys.stdout.flush()

def show_cursor() -> None:
    sys.stdout.write("\033[?25h")
    sys.stdout.flush()
