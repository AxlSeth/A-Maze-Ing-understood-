OPPOSITES: dict[str, str] = {"n":"s",
                             "s":"n",
                             "e":"w",
                             "w":"e"}


PATTERN: list[list[int]] = [[1,0,0,0,0,1,1,1,1],
                            [1,0,0,0,0,0,0,0,1],
                            [1,0,1,0,0,1,1,1,1],
                            [1,1,1,1,0,1,0,0,0],
                            [0,0,1,0,0,1,1,1,1]]
#center of the 42 pattern is [y=2, x=4]

MIN_WIDTH: int = len(PATTERN[0]) + 2
MIN_HEIGHT: int = len(PATTERN) + 2
#-------------------


class Cell():
    def __init__(self) -> None:
        self.walls: dict[str, int] = {"n": 1,
                                      "s": 1,
                                      "e": 1,
                                      "w": 1}
        self.is_checked: int = 0
        self.is_symbol: int = 0
        self.coords: list[int] = [0, 0]

    def open_path(self, side: str) -> None:
        self.walls[side] = 0


#------------------

def test(maze: list[list[Cell]]) -> None:
    for line in maze:
        for _ in line:
            print("x---", end="")
        print("\n")

#------------------


def gen_maze(width: int, height: int) -> list[list[Cell]]:

    maze: list[list[Cell]] = []
    if width < MIN_WIDTH or height < MIN_HEIGHT:
        raise ValueError
    for _ in range(height):
        row: list[Cell] = []
        for _ in range(width):
            column: Cell = Cell()
            row.append(column)
        maze.append(row)

    test(maze)
    return (maze)


if __name__ == "__main__":
    gen_maze(10, 15)
