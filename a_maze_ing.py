import vars
import maze_utils
import maze_gen
import display
import subprocess
import time
import sys
import tty
import termios


def welcome_screen():
    subprocess.run(["clear"])
    for char in "\n\nHello":
        print(char, end="", flush=True)
        time.sleep(0.1)
    for _ in range(3):
        time.sleep(0.5)
        print(".", end="", flush=True)
    time.sleep(1)
    vars.WIDTH, vars.HEIGHT = maze_utils.get_dimensions()
    vars.START_POINT = (vars.COLUMNS - (vars.WIDTH + 1) * 4) // 2
    subprocess.run(["clear"])


def get_cursor_row() -> int:
    fd = sys.stdin.fileno()
    old = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        sys.stdout.write("\033[6n")
        sys.stdout.flush()
        response = ""
        while True:
            ch = sys.stdin.read(1)
            response += ch
            if ch == "R":
                break
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old)
    row = int(response[2:response.index(";")])
    return row

def main() -> None:
    welcome_screen()
    display.print_title()
    vars.MAZE_START_ROW = get_cursor_row()
    vars.MAZE_START_ROW = get_cursor_row()
    display.hide_cursor()
    display.display_closed_maze(vars.WIDTH, vars.HEIGHT)
    maze_g: maze_gen.MazeGenerator = maze_gen.MazeGenerator()
    maze = maze_g.generate(vars.WIDTH, vars.HEIGHT, on_carve=display.carve_wall)
    display.move_cursor_below_maze(maze)
    display.show_cursor()

main()
